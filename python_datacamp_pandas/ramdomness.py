# criando um dado (dice)
import numpy as np
np.random.seed(123)
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
# rolando os dados
step = 50
dice = np.random.randint(1, 7)

if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)
print(dice)
print(step)

#Cara e coroa usando random walk
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
    print('Seu resultado é: ', outcomes)
