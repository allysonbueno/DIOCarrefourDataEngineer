lista = [1,3,5,7,'texto']
lista_animal = ('cachorro','gato','galinha','porco','elefante') ### TUPLA USA () E É IMUTAVEL

# print(lista)

# if 'lobo' in lista_animal:
#     print('Lobo localizado')
# else:
#     a = input('Lobo não localizado - Deseja inserir o animal? S/N: ')
#     while a not in ['S','N']:
#         a = input('Resposta invalida - Tente Novamente: ')    
#     if a == 'S':
#         lista_animal.append('lobo')
#         print(lista_animal)
#     else:
#         print(lista_animal)

# retira o ultimo
lista_animal1 = list(lista_animal)
print('Vai retirar o ' + lista_animal1.pop() + ' : ' + str(lista_animal1))

print('Vai retirar o animal na posicao 1: ' + lista_animal1.pop(1))

lista_animal1.remove('galinha')
print('Vai retirar o animal com nome galinha: ' + str(lista_animal1))

lista_animal2 = list(lista_animal)
print(lista_animal) ## observe que a lista original muda
lista_animal2.sort()
print('Sort: ' + str(lista_animal2))
