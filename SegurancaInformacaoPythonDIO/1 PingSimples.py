import os # biblioteca OS (SO)
import time

def ping():
    print("#" * 60)
    ip_ou_host = input("Digite o IP ou host: ")
    os.system('ping -n 6 {}'.format(ip_ou_host))

def pingMultiplo(parametro):
    with open(parametro) as file:
        dump = file.read()
        dump = dump.splitlines()
        for ip in dump:
            print('Verificando ip: ', ip)
            print('-' * 60)
            os.system('ping -n 2 {}'.format(ip))
            print('-' * 60)
            time.sleep(2)

if __name__ == '__main__':
   # ping()
   # pingMultiplo()

   arquivo = 'hosts.txt'
   print('Abrindo {}'.format(arquivo))
   pingMultiplo(arquivo)

