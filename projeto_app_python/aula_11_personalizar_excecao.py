
class Error (Exception):
    pass
class Inputerror(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise Inputerror('Nota deve ser menor que 10')
        elif x < 0:
            raise Inputerror ("Nota deve ser maior que 0")
        break
    except ValueError:
        print('Valor inválido, deve-se colocar apenas números!')
    except Inputerror as ex:
        print(ex)


