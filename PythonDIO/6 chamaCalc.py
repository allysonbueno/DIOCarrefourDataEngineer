# função retorna valor
# metodo não retorna (def)

class Calculadora:
    # def __init__(self):
    #      pass ## não faz nada, pra nao ficar vazio
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def resto(self, valor_a, valor_b):
        return valor_a % valor_b

# instancia classe
calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.divisao(4,2))
print(calculadora.multiplicacao(3,3))