
try:
    divisao = 10 / 0
except ArithmeticError:
    erro = 'Houve um erro ao realizar uma operação aritmética'
except Exception:
    erro = 'Ocorreu um erro desconhecido'
else:
    erro = False
finally:
    if erro:
        print(erro)
    else:
        print(divisao)