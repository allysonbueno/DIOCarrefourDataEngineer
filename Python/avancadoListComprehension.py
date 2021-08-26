x = [1,2,3,4,5,6,7,8,9]
y = []

# for i in x:
#     y.append(i**2) # lista de x foi pra i e resulta no quadrado de cada 1
# print(x)
# print(y)

#list comprehension:
x = [1,2,3,4,5,6,7,8,9]
y = [i**2 for i in x]
#y = [valorAAdicionar laço condição]
z = [i for i in x if i%2==1] #para imprimir numeros impares

print(x)
print(y)
print(z)