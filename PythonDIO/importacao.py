from MetFunClass_Televisao import Televisao
from MetFuncClass_Calculadora1 import Calculadora
from contadorLetras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5,10)
    print(calculadora.soma())
    lista= ['Subaru','Toyota']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra: {}'.format(total_letras))

    print(teste())