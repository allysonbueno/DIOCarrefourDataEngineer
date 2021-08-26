def dobro(x):
    return x*2

valor = 3
print(dobro(valor))

# map é usado para fazer isso a varios valores
valor = [1,2,3,4,5,6,7,8,9]

#Errado:
print(dobro(valor))

#Correto:
print(map(dobro, valor)) #só mostra endereço de memória

#apresentando sequencia 1 a 1
valorDobrado = map(dobro, valor)
for v in valorDobrado:
    print(v)

#valores em uma linha só
valorDobradoLista = map(dobro, valor)
valorDobradoLista = list(valorDobradoLista)
print(valorDobradoLista)