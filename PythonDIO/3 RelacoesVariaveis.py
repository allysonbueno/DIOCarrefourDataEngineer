# a = int(input('Digite um valor: '))
# b = int(input('Digite um valor: '))
# c = int(input('Digite um valor: '))

# if a > b and a > c:
#     print('Maior numero é {}'.format(a))
# elif b > a and b > c:
#     print('Maior numero é {}'.format(b))
# else:
#     print('Maior numero é {}'.format(c))

# print('Fim')

# a = int(input('Digite valor 1: '))
# b = int(input('Digite valor 2: '))

# resto_a = a % 2
# resto_b = b % 2

# if resto_a  == 0 or resto_b == 0:
#     print("Numero par digitado")
# else:
#     print("Nenhum numero par digitado")

regra = 'Utilize o range 0-10. Tente novamente: '

a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input(regra))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input(regra))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input(regra))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input(regra))

media = ( a + b + c + d) / 4

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media: {}'.format(media))
# else:    
#     print('Utilize 0 a 10')
print('Media: {}'.format(media))