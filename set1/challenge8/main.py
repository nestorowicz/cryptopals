import sys

def calculate_score(ciphertext):
    hist = {}
    for i in range(0, len(ciphertext), 32):
        key = ciphertext[i:i+32]
        hist[key] = hist.get(key, 0) + 1
    return sum([ hist[key] - 1 for key in hist ])

def main():
    input_lines = sys.stdin.buffer.read().decode('ascii').splitlines()
    scores = [ calculate_score(ciphertext) for ciphertext in input_lines ]
    print(sorted(zip(input_lines, scores), key=lambda x:x[1], reverse=True)[0])

main()
