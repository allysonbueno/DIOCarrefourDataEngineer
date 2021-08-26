# Aprenda a utilizar informações de data, horário e relacionar datas diferentes
from datetime import date, time, datetime, timedelta
from time import strftime


def retorna_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')

def retorna_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def retorna_datetime():
    data_atual = datetime.now()
    print(str(data_atual) + ' -> ' +
        data_atual.strftime('%d/%m/%Y') + ' -> ' +
        data_atual.strftime('%c'))
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(str(data_criada) + ' -> ' + strftime('%c'))
    data_string = '22/08/2021 13:53:15'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(data_convertida.weekday())
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    retorna_date()
    retorna_time()
    retorna_datetime()