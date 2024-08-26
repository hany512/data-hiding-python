import numpy as np
import pywt
import wave
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class audiodwt:

    @staticmethod
    def encrypt_audio(audio_data, key):
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        encrypted_audio, _ = cipher.encrypt_and_digest(pad(audio_data, AES.block_size))
        return nonce, encrypted_audio


    @staticmethod
    def decrypt_audio(encrypted_audio_data, key, nonce):
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_audio = unpad(cipher.decrypt(encrypted_audio_data), AES.block_size)
        return decrypted_audio



    @staticmethod
    def audio_to_binary(audio_file, flag, key):
        if not audio_file:
            binary_flag = ''.join(format(ord(char), '08b') for char in flag)
            return binary_flag

        with wave.open(audio_file, 'rb') as wav:
            audio_params = wav.getparams()
            params_data = ''.join(format(param, '032b') for param in audio_params[:3])  # Store first 3 parameters
            audio_data = wav.readframes(wav.getnframes())

        nonce, encrypted_audio_data = audiodwt.encrypt_audio(audio_data, key)
        message = nonce + encrypted_audio_data + flag.encode()
        binary_audio = params_data + ''.join(format(byte, '08b') for byte in message)
        return binary_audio


    @staticmethod
    def hide_audio_in_image(image, binary_audio, color_channel):
        coeffs = pywt.dwt2(image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        subbands = [HH, HL, LH]
        idx = 0
        for subband in subbands:
            for i in range(subband.shape[0]):
                for j in range(subband.shape[1]):
                    if idx < len(binary_audio):
                        int_value = int(subband[i, j])
                        int_value = (int_value & ~1) | int(binary_audio[idx])
                        subband[i, j] = float(int_value)
                        idx += 1
                    else:
                        break

        stego_image = np.copy(image)
        stego_image[:, :, color_channel] = pywt.idwt2((LL, (LH, HL, HH)), 'haar')
        return stego_image


    @staticmethod
    def binary_to_audio(binary_audio, key):
        audio_params = [int(binary_audio[i: i+32], 2) for i in range(0, 96, 32)]  # Extract first 3 audio parameters
        audio_params.append(0)
        audio_params.extend(['NONE', 'not compressed'])

        binary_data = binary_audio[96:]
        nonce = bytearray(int(binary_data[i: i+8], 2) for i in range(0, 16 * 8, 8))
        encrypted_audio_data = bytearray(int(binary_data[i: i+8], 2) for i in range(16 * 8, len(binary_data), 8))
        decrypted_audio_data = audiodwt.decrypt_audio(encrypted_audio_data, key, nonce)

        return decrypted_audio_data, tuple(audio_params)


    @staticmethod
    def extract_audio_from_image(stego_image, color_channel, flag, key):
        coeffs = pywt.dwt2(stego_image[:, :, color_channel], 'haar')
        LL, (LH, HL, HH) = coeffs

        subbands = [HH, HL, LH]
        binary_audio = ""
        for subband in subbands:
            binary_audio += "".join([str(int(round(pixel)) & 1) for row in subband for pixel in row])

        binary_flag = audiodwt.audio_to_binary("", flag, key)
        flag_pos = binary_audio.find(binary_flag)
        binary_audio = binary_audio[:flag_pos]

        extracted_audio = audiodwt.binary_to_audio(binary_audio, key)
        return extracted_audio

