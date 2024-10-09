def rail_fence(plain_text, key):
    cipher_text = ''
    for i in range(key):
        j = i
        while j < len(plain_text):
            cipher_text += plain_text[j]
            if i == 0 or i == key - 1:
                j += 2 * key - 2
            else:
                if j + 2 * (key - i - 1) < len(plain_text):
                    cipher_text += plain_text[j + 2 * (key - i - 1)]
                j += 2 * key - 2
    return cipher_text


def cesar(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + key - 65) % 26 + 65)
    return cipher_text


def decode_rail_fence(cipher_text, key):
    plain_text = ''
    for i in range(key):
        j = i
        while j < len(cipher_text):
            plain_text += cipher_text[j]
            if i == 0 or i == key - 1:
                j += 2 * key - 2
            else:
                if j + 2 * (key - i - 1) < len(cipher_text):
                    plain_text += cipher_text[j + 2 * (key - i - 1)]
                j += 2 * key - 2
    return plain_text


if __name__ == '__main__':
    pt = input('Enter plaintext (rail-fence) : ')
    # key = int(input('Enter key (rail-fence) : '))
    print('Ciphertext (rail-fence) :', rail_fence(pt, 6))
