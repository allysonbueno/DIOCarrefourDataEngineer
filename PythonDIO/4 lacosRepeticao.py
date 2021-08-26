# regra = 'Utilize o range 0-10. Tente novamente: '

# a = int(input('Primeiro Bimestre: '))
# if a > 10:
#     a = int(input(regra))
# b = int(input('Segundo Bimestre: '))
# if b > 10:
#     b = int(input(regra))
# c = int(input('Terceiro Bimestre: '))
# if c > 10:
#     c = int(input(regra))
# d = int(input('Quarto Bimestre: '))
# if d > 10:
#     d = int(input(regra))

# media = ( a + b + c + d) / 4

# print('Media: {}'.format(media))

# a = int(input('Digite um numero: '))


# for num in range(101):    
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('numero {} primo'.format(num))

#while
nota = int(input('Informe a nota: '))
while nota > 10:
    nota = int(input('Utilize o range 0-10: '))

regra = 'Utilize o range 0-10. Tente novamente: '

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input(regra))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input(regra))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input(regra))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input(regra))

media = ( a + b + c + d) / 4

print('Media: {}'.format(media))

# a = 1
# while a <= 10:
#     print(a)
#     a += 1
 
