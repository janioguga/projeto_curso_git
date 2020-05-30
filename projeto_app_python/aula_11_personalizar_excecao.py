
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

bandas_metal = ['Iron Maiden', 'Angra', 'Slayer', 'Megadeth', 'Krisiun']
nova_banda = 'Caetano Veloso'
if nova_banda not in bandas_metal:
  raise InputError('{} não é metal!'.format(nova_banda))



