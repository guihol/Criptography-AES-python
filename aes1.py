"""primeiro passo é adquirir a biblioteca Crypto cipher,ela é instalada no terminal da ide ou no próprio prompt de comando.
depois de instalado a biblioteca basta exportar o modo de criptografia que deseja usar,no nosso caso é o AES(tambem é necessario
verificar se a biblioteca comporta o meio de criptografia que voce deseja usar)."""
from Crypto.Cipher import AES

"""o metodo de criptografia utilizado é o AES128 que é um metodo de criptografia binario,como são suportados apenas 2 bytes(16bits)
é necessario criar uma funçao para completar a str que se deseja criptografar para q ela seja sempre multiplo de 16bits e possa ser
criptografada.Usando a função padding fazemos q toda str seja completada por '\0' que é um caracter nulo e n interfere na 
criptografia"""
def padding(str):
    while(len(str) % 16 != 0):
        str+=b'\0'
    return str

def encryptor(keyb):
    """iv é o modo como a mensagem de criptgrafia ira se formar visualmente"""
    IV = 16 * b'\x00'
    """definimos o modo de criptografia que sera utilizado pela biblioteca"""
    mode = AES.MODE_CBC
    """criando o comando encryptor e decryptor utilizando a bliblioteca do cryptocipher e escolhendo o aes.new podemos executar 
    a funçao de criptografia utilizando a chave,o modo e a maneira que o texto sera apresentado a partir das variaveis que ja
     criamos"""
    encryptor = AES.new(keyb, mode, IV=IV)
    text = input("digite o texto q deseja criptografar")
    """utilizamos o comando encode no texto a ser criptografado para que ele se adeque a chave e ao python que não aceita certos tipos
    de caracteres e formas de sintaxe"""
    textb = text.encode()
    """utilizamos a funçao padding q criamos no inicio para q o texto seja compativel com a quantidade caracteres q bites permitidos
    dentro desta forma de criptografia"""
    textb2 = padding(textb)
    """criamos uma variavel q vai receber o texto e atraves do próprio comando do python .encrypt ultilizando o meio de criptografia 
    q nós ja definimos ira criptografar a mensagem"""
    ciphertext = encryptor.encrypt(textb2)
    """criamos uma variavel q vai receber o texto e atraves do próprio comando do python .decrypt ultilizando o meio de criptografia 
    q nós ja definimos ira descriptografar a mensagem """
    print("Texto:", textb2.decode("utf-8"))
    print("Texto encripitado:", ciphertext)
    return ciphertext

def decryptor(ciphertext,keyb):
    """iv é o modo como a mensagem de criptgrafia ira se formar visualmente"""
    IV = 16 * b'\x00'
    """definimos o modo de criptografia que sera utilizado pela biblioteca"""
    mode = AES.MODE_CBC
    """criando o comando encryptor e decryptor utilizando a bliblioteca do cryptocipher e escolhendo o aes.new podemos executar 
    a funçao de criptografia utilizando a chave,o modo e a maneira que o texto sera apresentado a partir das variaveis que ja
     criamos"""
    decryptor = AES.new(keyb, mode, IV=IV)
    """criamos uma variavel q vai receber o texto e atraves do próprio comando do python .encrypt ultilizando o meio de criptografia 
    q nós ja definimos ira criptografar a mensagem"""
    decrypedtext = decryptor.decrypt(ciphertext)
    """apos executar o processo basta mostrar o resultado"""
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
        ciphertext=encryptor(keyb)
        decryptor(ciphertext,keyb)

    return

if __name__ =="__main__":
    main()
