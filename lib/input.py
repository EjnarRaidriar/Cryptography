def input_option() -> int:
    _option = ''
    while True:
        print("Choose an option:")
        print("Encrypt: 1")
        print("Decrypt: 2")
        print("Exit: 0")
        _option = input("Option -> ")
        print()
        try:
            _option = int(_option)
        except ValueError:
            print("Invalid option!\n")
            continue
        if _option != 1 and _option != 2 and _option != 0:
            print("Invalid option!\n")
            continue
        else:
            if _option == 1:
                print("Option: Encrypt\n")
            elif _option == 2:
                print("Option: Decrypt\n")
            else:
                print("Exit")
                exit(0)
            return int(_option)


def input_7_letter_key() -> str:
    _key = ''
    while True:
        _key = input("Key -> ")
        print()
        err = 0
        if not _key.isalpha():
            print("Key must contain only Romanian letters!")
            err += 1
        if len(_key) < 7:
            print("Key must be at least 7 characters long!")
            err += 1
        if err == 0:
            _key = _key.upper()
            return _key
        print()


def input_message(only_char: bool = False) -> str:
    while True:
        _message = input("Message -> ")
        if only_char and not _message.replace(' ', '').isalpha():
            print('Only values a-z and A-Z are allowed!')
            print()
        else:
            break
    print()
    return _message
