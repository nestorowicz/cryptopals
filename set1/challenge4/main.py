import fileinput

exec(open('../lib.py').read())

def main():
    lines = list(bytes.fromhex(line.strip()) for line in open('4.txt'))
    decoded_scored = [ bruteforce_singlebyte_xor(line) for line in lines ]
    decoded_sorted = sorted(decoded_scored, key=lambda x: x[1])
    assert decoded_sorted[0][0] ==  b'Now that the party is jumping\n'

main()
