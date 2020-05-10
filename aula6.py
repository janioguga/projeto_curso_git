conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
#fazendo intercecao
conjunto_interceccao = conjunto.intersection(conjunto2)
print('Intercecção: {} '.format(conjunto_interceccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença: {} ' .format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença 2: {} '.format(conjunto_diferenca2))
# diferença simétrica: tudo que não tem nos dois. aquilo que só tem no a e so tem no b
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica de 1 para 2:  {} '. format(conjunto_diff_simetrica))
#   conjunto_a.difference(conjunto_b)

#verificando subset de conjuntos (subconjuntos)
conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_c = conjunto_a .difference(conjunto_b)
print(conjunto_c)

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Conjunto Sub-set: {} '.format(conjunto_subset))
# lembrar que as funçoes chama-se sempre como '.algumacoisa'
#usando a funçao superset
conjunto_superset = conjunto_a .issuperset(conjunto_b)
print('Conjunto Super-set: {} '.format(conjunto_superset))
# transformando lista em conjunto com elementos repetidos
lista = ['cachorro', 'gato', ' leão', 'macaco', 'gato']
conjunto_animais = set(lista)
print(conjunto_animais)
#converter novamente para lista
lista_animais = list(conjunto_animais)
print(lista_animais)
#se tem uma lista que tem duplicidade, transforma em conjunto e depois transforma em lista novamente.
# lembrar que {} representa conjunto, [] representa lista, () representa lista



# no conjunto a característica é a {}
# conjunto = {1, 2, 3, 4}
# print(type(conjunto)) imprimindo o tipo do conjunto
# conjunto.add(5) // adicionando o elemento 5 no conjunto
# conjunto.discard(1) retirando o elemento 1 do conjunto
#
# print(conjunto)
# conjunto de elementos que só pode ter elementos único
te = {10, 20, 30, 100, 290, 56}
print('Número dos conjuntos originais: {} '.format(te))
te.discard(100)
print('Número do discarte no conjunto: {} ' .format(te))    
# funçao .discard() deve indicar o numero a ser excluido indicando ele no conjunto

