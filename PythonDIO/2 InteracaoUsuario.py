a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
5
2
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