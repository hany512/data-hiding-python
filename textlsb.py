from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class text:
    @staticmethod
    def encrypt_text(text_data, key, iv):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(text_data) + padder.finalize()

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data

    @staticmethod
    def decrypt_text(encrypted_text_data, key, iv):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        decrypted_padded_data = decryptor.update(
            encrypted_text_data) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(
            decrypted_padded_data) + unpadder.finalize()

        return decrypted_data

    @staticmethod
    def hide_data_in_image(cover_image, secret_data, flag):
        secret_data += flag
        cover_pixels = cover_image.load()
        secret_data_index = 0
        secret_data_bit_index = 0

        for i in range(cover_image.size[0]):
            for j in range(cover_image.size[1]):
                pixel = cover_pixels[i, j]
                new_pixel = []
                for k in range(3):
                    if secret_data_index >= len(secret_data):
                        new_pixel.append(pixel[k])
                    else:
                        secret_data_byte = secret_data[secret_data_index]
                        secret_data_bit = (secret_data_byte >> (
                            7 - secret_data_bit_index)) & 1
                        new_pixel.append((pixel[k] & ~1) | secret_data_bit)
                        secret_data_bit_index += 1
                        if secret_data_bit_index == 8:
                            secret_data_bit_index = 0
                            secret_data_index += 1
                cover_pixels[i, j] = tuple(new_pixel)
        return cover_image

    @staticmethod
    def extract_data_from_image(stego_image, flag):
        extracted_data = bytearray()
        stego_pixels = stego_image.load()
        flag_index = 0
        current_byte = 0
        secret_data_bit_index = 0

        for i in range(stego_image.size[0]):
            for j in range(stego_image.size[1]):
                for k in range(3):
                    if flag_index >= len(flag):
                        return bytes(extracted_data[:-len(flag)])
                    current_byte = (current_byte << 1) | (
                        stego_pixels[i, j][k] & 1)
                    secret_data_bit_index += 1
                    if secret_data_bit_index == 8:
                        secret_data_bit_index = 0
                        extracted_data.append(current_byte)
                        flag_index = flag_index + \
                            1 if current_byte == flag[flag_index] else 0
                        current_byte = 0
        return bytes(extracted_data)

