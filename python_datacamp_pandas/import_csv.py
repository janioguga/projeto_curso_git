import pandas as pd

oms = pd.read_csv('/Users/jgustavo/Desktop/Observatorio ciência/observacoes_correcao_site/atualizacoes/COVID19-web.csv')
oms.info()
print(oms.columns)
print(oms.shape)
print(oms.describe)
print(oms.index)

# for lab, row in oms.iterrows():
#     oms.loc[lab, 'nova coluna'] = str(row['Source Register'])
#     print(oms.columns[['nova coluna']])

#print (oms)
# for val in oms:
#      print(oms)
#  for lab, row in oms.iterrows():
#      print(lab + ': ' + row['Source Register])
        
    # print(row)

#print(oms.loc[[1, 10, 100, 1000]])
import numpy as np

oms_teste = (oms.loc[[2, 10, 100, 100, 2100, 19], ['Last Refreshed on', 'Countries', 'Public title']])
china = np.logical_not(oms_teste == 'China')
print(china)
# print(oms_teste['Countries'] == 'China')
oms_testes = oms_teste[['Countries']]
print('Oms teste é:\n{}'.format(oms_testes))
for China in oms_testes:
    print('chung lee')

z = 9
if z % 2 == 0:
    print('z é divizível por 2 : ')
elif z % 3 == 0:
    print('z é divizível por 3: ')
else:
    print(str(z) + ': não é divizível por 2 e por 3 !')
# area = 9
# if (area < 9):
#     print("small")
# elif (area < 12):
#     print("medium")
# else:
#     print("large")

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15:
    print("big place!")
elif area > 10:
    print('medium size, nice!')
else:
    print("pretty small.")
error = 50
while error > 1:
    error = error / 4
    print('O valor é: {}'.format(error))

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
import numpy as np
peso = [100, 73, 80, 60, 76]
alt = [1.50, 1.60, 1.90, 1.30, 1.20]
np.peso = np.array([100, 73, 80, 60, 76])
np.alt = np.array([1.50, 1.60, 1.90, 1.30, 1.20])
x = np.peso * np.alt / np.alt**2

print('Seu Peso Gordo é: {} '.format(x))
for val in x:
    print('Impedância: ' + str(round(val)))

for height in alt:
    print(height)

for index, height in enumerate(alt):
    print('index ' + str(index) + ": " + str(height))
for d in 'family':
    print(d.capitalize())
fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    print("Pessoa " + str(index + 1) + ": " + str(height) + ' metros')

world = { "afghanistan":30.55,
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print('País: ' + key + " -- " + str(value) + ' GDP')




#
# def escrever_texto (teste1.txt, texto):
#     arquivo = open(teste1.txt, 'w')
#     arquivo.write(texto)
#     arquivo.close()
# def atualizar_texto(teste1, texto):
#     arquivo = open(teste1, 'a')
#     arquivo.write((oms.loc[[1, 10, 10, 100], ['Last Refreshed on', 'Countries', 'Public title']]))
#     arquivo.close()
# def ler_texto(teste1, texto):
#     arquivo = open(teste1, 'r')
#     nome_arquivo = arquivo.read()
#     print(nome_arquivo)
