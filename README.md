from Crypto.Cipher import AES
def padding(str):
    while(len(str) % 16 != 0):
        str+=b'\0'
    return str

def encryptor(keyb):
    IV = 16 * b'\x00'
    mode = AES.MODE_CBC
    encryptor = AES.new(keyb, mode, IV=IV)
    text = input("digite o texto q deseja criptografar")
    textb = text.encode()
    textb2 = padding(textb)
    ciphertext = encryptor.encrypt(textb2)
    print("Texto:", textb2.decode("utf-8"))
    print("Texto encripitado:", ciphertext)
    return ciphertext


def decryptor(ciphertext, keyb):
    IV = 16 * b'\x00'
    mode = AES.MODE_CBC
    decryptor = AES.new(keyb, mode, IV=IV)
    decrypedtext = decryptor.decrypt(ciphertext)
    print("Texto encripitado:", ciphertext)
    print(decrypedtext.decode("utf-8"))
    """o .decode(utf-8) serve para converter o texto em um encode legivel"""
    return


def main():
    print("vc deseja encriptar ou descriptografar")
    entrada = input("encriptograr/descriptografar(e/d)")
    generatekey = str(input("digite uma chave de 16 caracteres sendo eles letras ou numeros"))
    keyb = generatekey.encode()
    if (entrada == "e"):
        encryptor(keyb)
    else:
        ciphertext = encryptor(keyb)
        decryptor(ciphertext, keyb)

    return


if __name__ == "__main__":
    main()
