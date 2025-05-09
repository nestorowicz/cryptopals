import base64
import itertools
import sys

exec(open('../lib.py').read())

def determine_keysizes(ciphertext, n):
    keysizes = range(2, 41)
    scores = { keysize: 0 for keysize in keysizes }
    for n in keysizes:
        for i in range (0, 10, 2):
            a = ciphertext[i*n:(i+1)*n]
            b = ciphertext[(i+1)*n:(i+2)*n]
            scores[n] += calculate_edit_distance(a, b) / n
        scores[n] /= 10 / 2

    return sorted(keysizes, key=lambda x: scores[x])[:n]

def score_block(input_bytes):
    input_letters = bytes([ byte for byte in input_bytes if ord('a') <= byte <= ord('z') ])
    histogram = build_histogram(input_letters)
    return sum([ max(letter_frequency_en[char] - histogram.get(char, 0), 0) for char in letter_frequency_en ])

def guess_key(block):
    keyset = range(0, 255)
    scores = { key: score_block(xor_by_key(block, key)) for key in keyset }
    return sorted(keyset, key=lambda x: scores[x])[0]

def to_blocks(ciphertext, keysize):
    return [ [ ciphertext[i] for i in range(x, len(ciphertext), keysize) ] for x in range(0, keysize) ]

def decrypt_repeating_xor(input_bytes, key):
    key_iter = itertools.cycle(key)
    return bytes([ byte ^ next(key_iter) for byte in input_bytes ])

def break_repeating_xor(ciphertext):
    keysizes = determine_keysizes(ciphertext, 3)
    for keysize in keysizes:
        blocks = to_blocks(ciphertext, keysize)
        guessed_key = bytes([ guess_key(block) for block in blocks ])
        decoded_bytes = decrypt_repeating_xor(ciphertext, guessed_key)
        print(f"Guessed key: {guessed_key.hex()} ({guessed_key.decode('ascii')})")
        print(f"Decoded text:\n{decoded_bytes.decode('ascii')}\n")

def main():
    f = sys.stdin.buffer.read()
    ciphertext = base64.b64decode(f)
    plain_text = break_repeating_xor(ciphertext)

main()
