valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}

resultado_par = valida_numero['par', (3)]

resultado_impar = valida_numero['impar', (4)]
#print(valida_numero)
class resultado:

    if resultado_par:
        print('Seu número é par! {} '.format(resultado_par))
    else:
        print('Seu número é impar {}'.format(resultado_impar))





