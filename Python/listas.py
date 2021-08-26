listaString = ["um","dois","tres"]
listaNumeros = [1,2,3,4,5,6]
listaMista = ["String",True,1.99]

print(listaString)
print(listaNumeros)
print(listaMista)

print(listaString[2])

for item in listaNumeros:
    print(item)

listaString.append("quatro")    

var = 7
if var in listaNumeros:
    print(var, "Esta na na lista")
else:
    print(var, "Não esta na na lista")

del listaNumeros[3:]
print(listaNumeros)

print(listaString)
del listaString[:]
print(listaString)

listaAleatoria = [112,54,258,300,1,517,89,35]
listaAleatoria.sort()
print(listaAleatoria)
listaAleatoria.sort()