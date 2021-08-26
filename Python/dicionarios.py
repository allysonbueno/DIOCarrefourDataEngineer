dicionario = {"Allyson": "allysonbueno@gmail.com",
    "Julia": "juliacrpaixao@gmail.com",
    "Maria Luzia": "maludopapai@gmail.com",    
    }

print(dicionario['Allyson'])

for chave in dicionario:
    print(dicionario[chave])

for chave in dicionario:
    print(chave + " - " + dicionario[chave])    

for chave in dicionario.items():
    print(chave)

for chave in dicionario.values():
    print(chave)

for chave in dicionario.keys():
    print(chave)