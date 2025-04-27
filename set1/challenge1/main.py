import base64

input_bytes = bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
print(f"input bytes = {input_bytes}")
print(f"base64 encoded = {base64.b64encode(input_bytes)}")
