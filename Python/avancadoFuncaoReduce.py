# A função reduce, disponível no módulo built-in functools, 
# serve pra "reduzir" um iterável (como uma lista) a um único valor.

# É um paradigma um pouco mais comum em linguagens funcionais, mas que 
# também é bastante útil em linguagens imperativas/orientadas a objetos 
# como o Python.

from functools import reduce

def soma(x , y):
    return x+y

lista = [1,2,5,10,20,50]

soma = reduce(soma, lista)
print(soma)