listaMercado = ["Arroz", "Feijao", "Açucar",
    "Shampoo","Carne"]

for i in range(len(listaMercado)):   #len pega o vetor e range mede o tamanho da lista
    print(i, listaMercado[i])

print("Enumerate:")
# funcao enumerate
for i, nome in  enumerate(listaMercado):
    print(i, "-", nome)
