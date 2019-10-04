from Crypto.Cipher import AES
def padding(str):
    while(len(str) % 16 != 0):
        str+=b'\0'
    return str
key = b'0213456789abcdef'
IV = 16 * b'\x00'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)
decryptor = AES.new(key, mode, IV=IV)
text=input("digite o texto q deseja criptografar")
textb=text.encode()
textb2=padding(textb)
ciphertext = encryptor.encrypt(textb2)
decrypedtext = decryptor.decrypt(ciphertext)
print("Texto:", textb2.decode("utf-8"))
print("Texto encripitado:", ciphertext)
print(decrypedtext.decode("utf-8"))