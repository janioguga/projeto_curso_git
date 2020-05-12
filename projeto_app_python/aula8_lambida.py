# a lambida é uma função anonima para simplificar o dodigo
#vamos fazer o mesmo exercício do codigo contador

contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']

print('Contador de letras da lista de animais: {} ' .format(contador_letras(lista_animais)))

#lambda serve para funçoes mais simples
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(8,4))
#dicionario de funcoes lambda

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b : a - b,
    'multiplicação' : lambda a, b: a * b,
    'Divisão': lambda a, b: a / b
}
print(type(calculadora))
soma = calculadora['soma']
multiplicação = calculadora['multiplicação']
subtracao = calculadora ['subtração']
print('A soma é: {} ' .format(soma(5,10)))
print('A multiplicação é: {} '.format(multiplicação(10,2)))



