import base64

def enc(password):
    enc_byte = base64.b64encode(password.encode())
    print(enc_byte)

passwd=input("Enter your password : ")
enc(passwd)