class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

# criando a classe em que o padrão é a televisão desligada
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            self.canal +=1

    def diminui_canal(self):
        if self.ligada:
            self.canal -=1


# criar uma variável para instanciar a classe Televisao
televisao = Televisao()
print('Televisão está ligada: {} ' .format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {} '.format(televisao.canal))
televisao.aumenta_canal()
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.aumenta_canal()
print('Canal: {} '.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))

