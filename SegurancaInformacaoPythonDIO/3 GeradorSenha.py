import random, string

tamanho = int(input('Quantidade de caracteres: '))

# chars = string.ascii_letters + string.digits + '!@#$%&*()-=+'
# chars = string.ascii_lowercase + string.digits + '!@#$%&*()-=+'
chars = string.ascii_uppercase + string.digits + '!@#$%&*()-=+'

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))

