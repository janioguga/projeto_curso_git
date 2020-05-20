import numpy as np
altura = [1.56, 1.78, 1.89]
peso = [76, 80, 90]
np_altura = np.array(altura)
np_peso = np.array(peso)
bmi = np_peso / np_altura ** 2
print('O peso corporal da família é: {} '.format(bmi))
print(type(peso))
print(bmi[np.logical_and(bmi > 23, bmi < 26)])
print(np.logical_and(bmi > 23, bmi < 26))

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
multiplicacao = np_mat * 2
soma = np_mat + np.array([10, 10])
soma_mat = np_mat + np_mat
print(soma_mat)
#o "multiplicaçao", multiplicou cada elemento por 2
# o soma pegou o numero no array e somou com o np_mat original
# o "soma_mat" somou as duas listas, elemento por elemento.
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
print(np.median(x))
print(np.mean(x))

import matplotlib.pyplot as plt

year = [1958, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#Adicionando dados no gráfico
year = [1800, 1850, 1900] + year
pop = [1.0, 1.252, 1.659] + pop

import numpy as np
np_year = np.array(year)
np_pop = np.array(pop)
np_pop = np_pop * 2
# continent = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
# color = ['red', 'green', 'blue', 'green', 'yellow', 'black']
# dict = {
#     'Asia':'red',
#     'Europe':'green',
#     'Africa':'blue',
#     'Americas':'yellow',
#     'Oceania':'black'
# }
# col = dict
plt.scatter(pop, year, s = np_pop,)
#custumization
plt.xticks([1, 2, 3, 5, 6],
            ['1m', '2m', '3 m', '5 m', '6 m'])
plt.title('Gráfico de crescimento populacional')
plt.xlabel('População em milhares')
plt.ylabel('Ano')
# plt.text(1900, 'China')
# plt.text(2000, 'Brasil')
plt.grid(True)
plt.show()

# Aula sobre dicionários
#Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
#Use ind_ger to access the capital of Germany from the capitals list. Print it out.

countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
europe = {'spain': 'madrid', 'france':'paris', 'germany': 'berlin', 'norway': 'oslo'}
print(europe.keys())
# chamo o nome do dicionario e a fechadura(valor1) para saber valor2
print(europe['norway'])

ind_ger = countries.index('germany')
print(capitals[ind_ger])
# gero o index numa lista e imprimo na outra.


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print(['italy' in europe])

# Add poland to europe
europe['poland'] = 'warsaw'
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = { 'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data
del(europe['norway'])
# Print europe
print(europe)
print(['norway' in europe])
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = {
            'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
            'drives_right': [True, False, False, False, True, True, True],
            'car_per_cap': [809, 731, 588, 18, 200, 70, 45]
}
cars = pd.DataFrame(my_dict)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = (row_labels)



print(cars)


