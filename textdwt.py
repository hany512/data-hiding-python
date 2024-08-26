import numpy as np
import pywt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image

class textdwt:

    @staticmethod
    def encrypt_text(text_data, key):
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        encrypted_text = cipher.encrypt(pad(text_data.encode(), AES.block_size))
        return nonce, encrypted_text


    @staticmethod
    def decrypt_text(encrypted_text_data, key, nonce):
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_text = unpad(cipher.decrypt(encrypted_text_data), AES.block_size).decode('ISO-8859-1')

        return decrypted_text


    @staticmethod
    def text_to_binary(text, flag, key):
        if not text:
            binary_flag = ''.join(format(ord(char), '08b') for char in flag)
            return binary_flag

        nonce, encrypted_text_data = textdwt.encrypt_text(text, key)
        message = nonce + encrypted_text_data + flag.encode()
        binary_text = ''.join(format(byte, '08b') for byte in message)
        return binary_text



    @staticmethod
    def hide_text_in_image(image, binary_text, color_channel):
        coeffs = pywt.dwt2(image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        idx = 0
        for i in range(HH.shape[0]):
            for j in range(HH.shape[1]):
                if idx < len(binary_text):
                    HH_int = int(HH[i, j])
                    HH_int = (HH_int & ~1) | int(binary_text[idx])
                    HH[i, j] = float(HH_int)
                    idx += 1
                else:
                    break

        stego_image = np.copy(image)
        stego_image[:, :, color_channel] = pywt.idwt2((LL, (LH, HL, HH)), 'haar')
        return stego_image

    
    @staticmethod
    def binary_to_text(binary_text, key):
        nonce = bytearray(int(binary_text[i: i + 8], 2) for i in range(0, 16 * 8, 8))
        encrypted_text_data = bytearray(int(binary_text[i: i + 8], 2) for i in range(16 * 8, len(binary_text), 8))
        decrypted_text = textdwt.decrypt_text(encrypted_text_data, key, nonce)
        return decrypted_text


    @staticmethod
    def extract_text_from_image(stego_image, color_channel, flag, key):
        coeffs = pywt.dwt2(stego_image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        binary_text = "".join([str(int(round(pixel)) & 1) for row in HH for pixel in row])

        binary_flag = textdwt.text_to_binary("", flag, key)
        flag_pos = binary_text.find(binary_flag)
        binary_text = binary_text[:flag_pos]

        extracted_text = textdwt.binary_to_text(binary_text, key)
        return extracted_text


def main():
    # Load cover image
    cover_image = Image.open('34.jpg')
    cover_image = np.array(cover_image)

    # Input text and flag
    with open('file.txt', 'r') as f:
        secret_text = f.read().strip()
    flag = "FLAG_END"

    # Generate a random AES key
    key = get_random_bytes(32)

    # Convert text to binary format
    binary_text = textdwt.text_to_binary(secret_text, flag, key)

    # Hide text in the cover image
    stego_image = textdwt.hide_text_in_image(cover_image, binary_text, 0) # 0 for R, 1 for G, 2 for B
    # Save the stego image
    stego_image = Image.fromarray(stego_image)
    stego_image.save('stego_image.png')

    # Load stego image
    stego_image = Image.open('stego_image.png')
    stego_image = np.array(stego_image)

    # Extract text from stego image
    extracted_text = textdwt.extract_text_from_image(stego_image, 0, flag, key)  # 0 for R, 1 for G, 2 for B
    print("Extracted text:", extracted_text)

    # Save extracted text to a file
    with open('extracted_text.txt', 'w') as f:
        f.write(extracted_text)

if __name__ == "__main__":
    main()