import numpy as np
import pywt
from PIL import Image
from Crypto.Cipher import AES


class imagedwt:

    @staticmethod
    def pad_key(key):
        return key.ljust(32, b'\0')[:32]

    @staticmethod
    def aes_encrypt(data, key):
        key = imagedwt.pad_key(key)
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, _ = cipher.encrypt_and_digest(data)
        length = len(data).to_bytes(4, byteorder='big')
        return nonce + length + ciphertext
    

    @staticmethod
    def aes_decrypt(data, key):
        key = imagedwt.pad_key(key)
        nonce = data[:16]
        length = int.from_bytes(data[16:20], byteorder='big')
        ciphertext = data[20:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_data = cipher.decrypt(ciphertext)
        return decrypted_data[:length]


    @staticmethod
    def image_to_binary(image_file, aes_key=None):
        image_data = np.array(Image.open(image_file))
        dimensions = image_data.shape
        dimensions_data = ''.join(format(d, '016b') for d in dimensions)
        flattened_image_data = image_data.flatten()

        if aes_key is not None:
            flattened_image_data = imagedwt.aes_encrypt(flattened_image_data.tobytes(), aes_key)

        binary_image = dimensions_data + ''.join(format(byte, '08b') for byte in flattened_image_data)
        return binary_image


    @staticmethod
    def hide_image_in_image(cover_image, binary_image, color_channel):
        coeffs = pywt.dwt2(cover_image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        subbands = [HH, HL, LH]
        idx = 0
        for subband in subbands:
            for i in range(subband.shape[0]):
                for j in range(subband.shape[1]):
                    if idx < len(binary_image):
                        int_value = int(subband[i, j])
                        int_value = (int_value & ~1) | int(binary_image[idx])
                        subband[i, j] = float(int_value)
                        idx += 1
                    else:
                        break

        stego_image = np.copy(cover_image)
        stego_image[:, :, color_channel] = pywt.idwt2((LL, (LH, HL, HH)), 'haar')
        return stego_image


    @staticmethod
    def binary_to_image(binary_image, aes_key=None):
        dimensions = [int(binary_image[i: i+16], 2) for i in range(0, 48, 16)]
        binary_data = binary_image[48:]
        image_data = bytearray(int(binary_data[i: i+8], 2) for i in range(0, len(binary_data), 8))

        if aes_key is not None:
            image_data = imagedwt.aes_decrypt(image_data, aes_key)

        # print(f"Dimensions: {dimensions}")
        # print(f"Image data length: {len(image_data)}")
        # print(f"Expected data size: {dimensions[0] * dimensions[1] * dimensions[2]}")

        return np.frombuffer(image_data, dtype=np.uint8).reshape(dimensions)


    @staticmethod
    def extract_image_from_image(stego_image, color_channel, aes_key=None):
        coeffs = pywt.dwt2(stego_image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        subbands = [HH, HL, LH]
        binary_image = ""
        for subband in subbands:
            binary_image += "".join([str(int(round(pixel)) & 1) for row in subband for pixel in row])

        extracted_image = imagedwt.binary_to_image(binary_image, aes_key)
        return extracted_image
