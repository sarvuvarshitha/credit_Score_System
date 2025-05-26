def xor_strings(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def round_function(data, key):
    return xor_strings(data, key)

def feistel_encrypt(plain_text, key, rounds=4):
    if len(plain_text) % 2 != 0:
        plain_text += ' '

    half = len(plain_text) // 2
    left, right = plain_text[:half], plain_text[half:]

    for i in range(rounds):
        temp = right
        right = xor_strings(left, round_function(right, key))
        left = temp

    return left + right

def feistel_decrypt(cipher_text, key, rounds=4):
    half = len(cipher_text) // 2
    left, right = cipher_text[:half], cipher_text[half:]

    for i in range(rounds):
        temp = left
        left = xor_strings(right, round_function(left, key))
        right = temp

    return left + right
