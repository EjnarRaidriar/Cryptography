alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def alphPermutation(key: int, alph: str) -> str:
    start = slice(key, 26)
    end = slice(key)
    if alph != '':
        return alph[start] + alph[end]
    return alphabet_string[start] + alphabet_string[end]


def cryptogram(crypt: str) -> str:
    alph = list(alphabet_string)
    crypt = list(crypt.upper())
    e = list()
    for ch in crypt:
        if ch not in e:
            e.append(ch)
    for ch in list(alph):
        if ch in e:
            alph.remove(ch)
    e += alph
    return "".join(e)


def encrypt(message: str, key: int, s_key: str) -> str:
    e_alph = list(alphPermutation(key, cryptogram(s_key)))
    e = list(message)
    for m_i, m_ch in enumerate(e):
        for a_i, a_ch in enumerate(list(alphabet_string)):
            if m_ch == a_ch:
                e[m_i] = e_alph[a_i]
    return "".join(e)


def decrypt(message: str, key: int, s_key: str) -> str:
    e_alph = list(alphPermutation(key, cryptogram(s_key)))
    d = list(message)
    for m_i, m_ch in enumerate(d):
        for a_i, a_ch in enumerate(e_alph):
            if m_ch == a_ch:
                d[m_i] = alphabet_string[a_i]
    return "".join(d)


run = True
while run:
    option = ''
    while True:
        print('Choose option:')
        option = str(input('[encrypt e / decrypt d / exit 0]: '))
        if option not in ('encrypt', 'e', 'decrypt', 'd', 'exit', '0'):
            print('Unknown option!')
            continue
        else:
            break
    if option == '0' or option == 'exit':
        exit()

    input_key = ''
    while True:
        print('Input first key (integer of 1 to 25)')
        input_key = input('First key: ')
        if not input_key.isnumeric():
            print('Key must be an integer')
            continue
        input_key = int(input_key)
        if 1 <= input_key <= 25:
            print('Key accepted')
            break
        else:
            print('Value must be in range from 1 to 25!')

    input_second_key = ''
    while True:
        print('Input second key of at least 7 latin letters or empty to skip')
        input_second_key = input('Second key:')
        if input_second_key == '':
            print('Proceeding without second key')
            break
        err_count = 0
        if not input_second_key.isalpha():
            print('Key must contain only latin letters!')
            err_count += 1
        if len(input_second_key) < 7:
            print('Key must be at least 7 letters long!')
            err_count += 1
        if err_count > 0:
            continue
        else:
            print('Second key accepted')
            break

    input_message = ''
    while True:
        input_message = input('Input message \n')
        if any(not char.isalpha() for char in input_message):
            print('Message should not contain only english alphabet letters!')
            continue
        else:
            print('Message accepted')
            break

    converted_message = input_message.upper().replace(' ', '')
    if option == ('e' or 'encrypt'):
        print('Encrypted message:')
        print(encrypt(converted_message, input_key, input_second_key))
    if option == ('d' or 'decrypt'):
        print('Decrypted message:')
        print(decrypt(converted_message, input_key, input_second_key))


