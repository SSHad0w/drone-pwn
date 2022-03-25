hex_string = "0x616263"[2:]
#Slice string to remove leading `0x`


bytes_object = bytes.fromhex(hex_string)
#Convert to bytes object


ascii_string = bytes_object.decode("ASCII")
#Convert to ASCII representation

print(ascii_string)