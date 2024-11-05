class VigenereCipher:
    def __init__(self, key: str):
        self.__romanian_uppercase = [
            "A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H", "I", "Î", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
            "S", "Ș", "T", "Ț", "U", "V", "W", "X", "Y", "Z"
        ]
        self.__keys = self.__str_to_int_list(key)
        self.__key_len = len(self.__keys)
        self.__alph_len = len(self.__romanian_uppercase)

    def __str_to_int_list(self, string: str) -> list:
        int_str = list()
        for ch in string.upper():
            for index, letter in enumerate(self.__romanian_uppercase):
                if ch == letter:
                    int_str.append(index)
        return int_str

    def __int_list_to_str(self, int_list) -> str:
        text = str()
        for value in int_list:
            for index, letter in enumerate(self.__romanian_uppercase):
                if index == value:
                    text += letter
        return text

    def encrypt(self, message: str) -> str:
        int_message = self.__str_to_int_list(message)
        encrypted_int_message = list()
        for index, value in enumerate(int_message):
            encrypted_int_message.append((value + self.__keys[index % self.__key_len]) % self.__alph_len)
        return self.__int_list_to_str(encrypted_int_message)

    def decrypt(self, message: str) -> str:
        int_cipher = self.__str_to_int_list(message)
        decrypted_int_cipher = list()
        for index, value in enumerate(int_cipher):
            decrypted_int_cipher.append((value - self.__keys[index % self.__key_len]) % self.__alph_len)
        return self.__int_list_to_str(decrypted_int_cipher)
