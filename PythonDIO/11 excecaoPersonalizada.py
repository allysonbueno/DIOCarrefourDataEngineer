class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digita um numero 0-10: '))
        print(x)
        if x > 10:
            raise InputError('Nota acima de 10!')
        elif x < 0:
            raise InputError('Nota abaixo de 0!')
        break
    except ValueError:
        print('Valor invalido.')
    except InputError as ex:
        print(ex)