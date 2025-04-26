import base64

inputText = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
inputBytes = bytes.fromhex(inputText)
print(f"plain text = {inputBytes.decode('ascii')}")
inputB64 = base64.b64encode(inputBytes)
print(inputB64)
