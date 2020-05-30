lista = [1, 10]

#forca um erro
try:
    arquivo = open('notax.txt', 'r')
    texto = arquivo.read()
    divisao = 10/0
    numero = (lista[0])
    

except ZeroDivisionError:
    print('não é possível dividir por 0')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro {} '.format(ex))
else:
    print('Executa quando nao tem exceçao')
finally:
    print('sempre executa')
    print('fechando o arquivo')
    arquivo.close()
