from Crypto.Cipher import AES

"""é uma criptografia que funciona com binarios,então a chave de criptografia precisa ter sempre 2 bytes (16 bits)
para fazer a criptografia,por isso eu defini a funçaõ pedding com multiplos de 16 tanto pra chave quanto pro texto a ser criptografado"""
def padding(str):
    while(len(str) % 16 != 0):
        str+=b'\0'
    return str

"""primeira funçao é a de encriptar o texto"""
def encryptor(keyb):
    IV = 16 * b'\x00'
    mode = AES.MODE_CBC
    encryptor = AES.new(keyb, mode, IV=IV)
    """para criptografar a mensagem precisa se dar entrada com o diretório de onde a mensagem esta salva na memória do computador """
    filename = input("digite o nome do arquivo q vc quer encriptografar")
    """o comando open serve para abrir o arquivo no local que foi dado pelo input"""
    f = open(filename, "rb")
    """f.read serve para ler o conteudo do arquivo aberto"""
    filedata = f.read();
    """utilizamos a função padding para q o tamanho do texto seja coerente com a capacidade de criptografia"""
    textb2 = padding(filedata)
    """usamos a variavel ciphertext com o camando encryptor que ja definimos como modo de criptografia"""
    ciphertext = encryptor.encrypt(textb2)
    # Escrevendo no arquivo
    """o programa cria um novo arquivo com a extenção ".enc" em seu final para defini-lo como um arquivo encriptado"""
    f = open(filename + ".enc", "wb")
    """o programa sub-escreve o arquivo com a mensagem criptografada"""
    f.write(ciphertext)
    """o comando close serve apenas para encerrar o processo sem q nenhum comando desnecessario seja executado"""
    f.close()
    return ciphertext

"""segunda função é a de decriptar o arquivo"""
def decryptor (keyb):
    IV = 16 * b'\x00'
    mode = AES.MODE_CBC
    """para decriptografar é preciso dar entrada com o local de onde esta salvo o arquivo criptografado"""
    filename = input("digite o nome do arquivo q vc quer decriptografar")
    """o comando open serve para abrir o arquivo no local que foi dado pelo input"""
    f = open(filename, "rb")
    """encryptedtext lê o conteudo do arquivo"""
    encryptedtext = f.read();
    """a variavel decryptor serve para definir a maneira como a mensagem sera decriptada ultilizando o metodo aes"""
    decryptor = AES.new(keyb, mode, IV=IV)
    decrypedtext = decryptor.decrypt(encryptedtext)
    print("Texto encripitado:", encryptedtext)
    print("Texto decripitado:", decrypedtext)
    """é criado um novo arquco com a extensão ".dec" para diferenciar dos outros arquivos"""
    f = open(filename+".dec", "wb")
    """o conteudo do arquivo.dec é transcrito pela mensagem decodificada e pronta para ser lida"""
    f.write(decrypedtext)
    """o comando close serve apenas para encerrar o processo sem q nenhum comando desnecessario seja executado"""
    f.close()
    return

"""definido a funçao main para a execução do programa"""
def main():
    print("vc deseja encriptar ou descriptografar")
    entrada = input("encriptograr/descriptografar(e/d)")
    generatekey = str(input("digite uma chave de 16 caracteres sendo eles letras ou numeros"))
    keyb = generatekey.encode()
    if (entrada == "e"):
        encryptor(keyb)
    else:
        decryptor( keyb)

    return


if __name__ == "__main__":
    main()
