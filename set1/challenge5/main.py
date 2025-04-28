import itertools

def encrypt_rotating_xor(phrase, key):
    key_bytes = itertools.cycle(key)
    return bytes([ byte ^ next(key_bytes) for byte in phrase ])

def main():
    text = b"""Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal"""
    key = b'ICE'
    for line in text.splitlines():
        ciphertext = encrypt_rotating_xor(line, key)
        print(ciphertext.hex())

main()
