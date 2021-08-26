lista1 = [1,2,3,4,5]
lista2 = ["Arroz","Feijao", "Açucar","Shampoo","Carne"]

lista3 = [19.99,12.50,8.90,13.19,39.90]

# compacta as 2 listas como se fosse uma unica lista 
# usando o laço for

for numero, nome, valor in zip(lista1, lista2,lista3):
    print(numero, nome, valor)
