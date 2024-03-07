import base64

def dec(password):
    dec_byte = base64.b64decode(password)
    res = dec_byte.decode()
    print(res)


passwd = input("Enter password to decrypt: ")
dec(passwd)