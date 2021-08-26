# Gerenciando e criando exceções customizadas com try, except, else e finally


lista = [1,10]
arquivo = open('copiados/teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não divide por zero')
except IndexError:
    print('Fora do Index')
# except:
#     print('Erro desconhecido')
# except BaseException as ex:
#     print('Erro Desconhecido. Erro: {}'.format(ex))
except ArithmeticError:
    print('Erro aritmetico')
else:
    print('Tudo ok')
finally:
    arquivo.close()
    print('Sempre executa - Arquivo fechado')