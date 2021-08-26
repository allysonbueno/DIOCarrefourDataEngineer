# conjunto = {"Mitsubishi Lancer", "Gol GTS", "Honda HRV", "Ford Ka", "Honda Biz","Honda PCX","Fiat Uno"}

# conjunto.add("Gol GTI")
# conjunto.discard("Honda HRV")

# print(conjunto)

conjunto1 = {1,2,3,4,5,6}
conjunto2 = {6,7,8,9,10}

conjuntoUniao = conjunto1.union(conjunto2)
# print(conjuntoUniao)

conjuntoInterseccao = conjunto1.intersection(conjunto2)
# print(conjuntoInterseccao)

conjuntoDiferenca = conjunto1.difference(conjunto2)
# print(conjuntoDiferenca)

conjuntoDifSimetrica = conjunto1.symmetric_difference(conjunto2)
# print(conjuntoDifSimetrica)

# subconjunto
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

# converter lista para conjunto - tirar duplicidade
lista_animal = ('cachorro','gato','galinha','porco','elefante','porco') 
conjunto_animais = set(lista_animal)
print(conjunto_animais)

lista_animal2 = list(conjunto_animais)
print(lista_animal2)

