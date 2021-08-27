from threading import Thread
import time

# def carro1(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro1: ', trajeto)
#         trajeto += velocidade

# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto += velocidade

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        # print('Carro: ', piloto, trajeto)
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto : {} Km: {}\n'.format(piloto, trajeto))

# carro1(10)
# carro2(20)

t_carro1 = Thread(target=carro, args=[1, 'Jez'])
t_carro2 = Thread(target=carro, args=[2, 'Allan'])

t_carro1.start()
t_carro2.start()
