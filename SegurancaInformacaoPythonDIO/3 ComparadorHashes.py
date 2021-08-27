import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160') # gera o hash do arquivo
hash2.update(open(arquivo2, 'rb').read()) # r - read b - binary leitura no modo binario

def mostraHexDigest(hexDig, nomeArquivo):
    print('O hash do arquivo {nomeArquivo} é: ', str(hexDig))  # hexdigest resume o hash em hexadecimal e mostra o hash

if hash1.digest() != hash2.digest():  # digest - resume os dados passados pelo update
    print(f'O arquivo: {arquivo1} é DIFERENTE do arquivo: {arquivo2}')
    nomeArquivo = 'a.txt'
    hexDig = hash1.hexdigest()
    mostraHexDigest(hexDig, nomeArquivo)
else:
    print(f'O arquivo: {arquivo1} é IGUAL do arquivo: {arquivo2}')
    nomeArquivo = 'b.txt'
    hexDig = hash1.hexdigest()
    mostraHexDigest(hexDig, nomeArquivo)