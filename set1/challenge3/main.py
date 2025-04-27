exec(open("../lib.py").read())

input_bytes = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
decoded = bruteforce_singlebyte_xor(input_bytes)[0]
assert decoded == bytes("Cooking MC's like a pound of bacon", 'ascii')
