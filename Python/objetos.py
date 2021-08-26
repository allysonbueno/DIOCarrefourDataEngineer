var1 = "Hello"
var2 = "World"
a = "Allyson"
b = "Bueno"
sequence = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
texto = "Texto Qualquer Lorem Ipsum"


concat = var1 + " " + var2
print (concat)
print (a[0])
print (a[1])
print (a[2])

concat2 = a + " " + b
print (concat2)
print (concat2[0:8])
print (concat2[0:])

tamanho = len(concat2)
print (tamanho)

letra = sequence[12]
print (letra)

print(sequence.lower())

sequence = sequence + "\n" + a + "\n" + b + "\n"
print(sequence.strip())  #remove caracteres especiais

print(sequence.split()) #converte sequencia em lista

lista1 = texto.split()
print(lista1)
lista1 = texto.split("r")
print(lista1)

busca = texto.find("Lo")
print(busca)
print(texto[busca:])

busca = texto.replace("Texto","Palavra")
print(busca)


