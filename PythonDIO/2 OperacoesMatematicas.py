a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print('soma: ' + str(soma))
# print('soma com format: {}'.format(soma))
# print('Soma: {} / Subtracao: {}'.format(soma, subtracao))
# print('Soma: {sum} / Subtracao: {sub}'.format(sum=soma, sub=subtracao))
resultado = ('Soma: {sum}'
            '\nSubtracao: {sub}'
            '\nMultiplicação: {mult}'
            '\nDivisão: {div}'
            '\nResto: {rest}'.format(sum=soma, 
                                    sub=subtracao, 
                                    mult = multiplicacao, 
                                    div = divisao, 
                                    rest = resto))
print(resultado)                                    
# print(subtracao)
# print('subtracao: ' + str(subtracao))
# print(multiplicacao)
# print(divisao)
# print(type(divisao))
# print(int(divisao))
# print(resto)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)
