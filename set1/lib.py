import string 

# source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
letter_frequency_en = {
    'a': 0.0812, 'b': 0.0149, 'c': 0.0271, 'd': 0.0432, 'e': 0.1202, 'f': 0.0230,
    'g': 0.0203, 'h': 0.0592, 'i': 0.0731, 'j': 0.0010, 'k': 0.0069, 'l': 0.0398,
    'm': 0.0261, 'n': 0.0695, 'o': 0.0768, 'p': 0.0182, 'q': 0.0011, 'r': 0.0602,
    's': 0.0628, 't': 0.0910, 'u': 0.0288, 'v': 0.0111, 'w': 0.0209, 'x': 0.0017,
    'y': 0.0211, 'z': 0.0007
}
letter_frequency_en = { ord(char): letter_frequency_en[char] for char in letter_frequency_en }

def build_histogram(input_bytes):
    histogram = {}
    for byte in input_bytes.lower():
        histogram[byte] = histogram[byte] + 1 if byte in histogram else 1
    for byte in histogram:
        histogram[byte] = histogram[byte] / len(input_bytes)
    return histogram

def xor_by_key(input_bytes, key):
    return bytes([ input_byte ^ key for input_byte in input_bytes ])

def score_english(input_bytes):
    """Returns a score as a float."""
    histogram = build_histogram(input_bytes)
    result = 0
    for char in string.ascii_lowercase:
        char = ord(char)
        freq = histogram[char] if char in histogram else 0
        result += abs(letter_frequency_en[char] - freq)
    for byte in histogram:
        if byte not in letter_frequency_en and byte not in [ord("'"), ord(" ")]:
            result += 10
    return result


def bruteforce_singlebyte_xor(input_bytes):
    xored = [ xor_by_key(input_bytes, byte) for byte in range(0, 256) ]
    scored = [ (text, score_english(text)) for text in xored ]
    scored_sorted = sorted(scored, key=lambda x: x[1])
    return scored_sorted[0]
