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
# Para evitar que ao importar o modulo, o console imprima os valores que não estejam na
# classe, o melhor é colocar o método main como abaixo. O main so imprime
# quando é chamado pelo próprio arquivo
# Importante quando tiver testando um codigo, para a impressao nao aparecer
# no módulo mas pode ficar para teste do método do prprio arquivo.


if __name__ == '__main__':
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
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))

