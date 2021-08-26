from functools import reduce
# Pergunta 1:
# Dada a seguinte lista:
from typing import DefaultDict


lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [i for i in lista if i%2==1]

def dobro(i):
    if i%2 == 0:
        return i        

lista2 = filter(dobro, lista)



x = [1, 2, 3]
y = [i for i in x if i % 2 == 0]
 
print(y)