# para inserir o input -  para que o usuario interaga
# o int na frente transforma o valor do input num inteiro para nao dar erro

a = int(input('Entre com o valor de a para calcular: '))
b = int(input('Entre com o valor de b para calcular: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Divisao: {divisao}'
      '\nMultiplicacao: {multiplicacao}'
      '\nSoma: {soma}' 
      '\nResto {resto} '.format(divisao=divisao,
                                multiplicacao=multiplicacao,
                                soma=soma,
                                resto=resto))

print(resultado)





# como saber o tipo da variavel
# como mudar o tipo de variavel
# como concatenar as variaveis
# print(type(soma))
# soma = str(soma)
# print(type(soma))

#print('soma:' + str(soma))
# outra forma de imprimir um valor usando o .format
#print('soma: {} ' .format(soma))
# coloco as chaves dentro da string
# posso colocar na mesma linha todas as impressoes

#print('soma: {} subtracao {}' .format(soma, subtracao))
# dentro das chaves podemos descrever valor para tirar a ordem dentro do format
# com isso eu passo o valor dentro do format. dentro desta formula




#print('subtracao: ' + str(subtracao))
#print('multiplicacao: ' + str(multiplicacao))
#print(int(divisao))
# x = '1'
# soma2 = int(x) + 1
# print(soma2)


