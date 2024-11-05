from lib.input import *
from ViginereCipher import *

while True:
    option = input_option()
    key = input_7_letter_key()
    message = input_message(only_char=True)
    cipher = VigenereCipher(key)
    if option == 1:
        encrypted_message = cipher.encrypt(message)
        print("Encrypted Message:")
        print("\033[96m" + encrypted_message + "\033[0m")

    if option == 2:
        decrypted_message = cipher.decrypt(message)
        print("Decrypted Message:")
        print("\033[96m" + decrypted_message + "\033[0m")

    if option == 0:
        break

    
