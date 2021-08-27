import ctypes

pasta = input('Caminho da Pasta (ex. C:/Dell) : ')

atributo_ocultar = 0x02

# OCULTAR UM ARQUIVO
# retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print('Arquivo Ocultado!')
else:
    print('Arquivo NÃO Ocultado!')