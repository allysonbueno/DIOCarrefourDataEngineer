"""
r = read
w = write
a = both
r+ = r+w
w+ = apaga arquivo anterior
a+ =  r+w atualiza arquivo atual
"""
# -*- coding: utf-8 -*-

#arquivo = open("arquivo.txt")

#w = open("C:/Estudos/Python/arquivo2.txt", "w") #argumento w - write
#w = open("C:/Estudos/Python/arquivo.txt", "w") #w - write e sobrepoe o arquivo.txt criado 

#w = open("C:/Estudos/Python/arquivo2.txt", "a") #argumento  a - open e adiciona conteudo no arquivo


#print(arquivo) dá erro
#linha = arquivo.readline()
#linhas = arquivo.readlines()
#textoCompleto = arquivo.read()

#print(linha)
#print(linhas)
#print(textoCompleto)"""

#w.write("Arquivo criado\n")

#w.close()

w = open("C:/Estudos/Python/arquivo1.txt", "a") 
#w.write("Linha 3\n")
w.close()

arquivo = open("C:/Estudos/Python/arquivo1.txt")
#texto = arquivo.read()
print(arquivo.read())