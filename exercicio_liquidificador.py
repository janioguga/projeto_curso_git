class Mixer:
    def __init__(self):
        self.power = False
        self.velocidade = int(input('Insira a velocidade: '))

    def velocidade_on (self):
        if self.power:
            self.ligada = True

        else:
            self.power = True
    def velocidade_1 (self):
        if self.power:
            self.velocidade = self.velocidade

    def velocidade_2 (self):
        if self.power:
            self.velocidade = 2


    # def velocidade_z (self):
    #     if self.power:
    #         self.velocidade +=1
    #     else:
    #         self.velocidade -=1

mixer = Mixer()
mixer.power
mixer.velocidade_1()
print('Velocidade do Mixer: {} '.format(mixer.velocidade))



