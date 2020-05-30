import shutil

def escrever_arquivo(texto):
    arquivo = open('notax.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualiza_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_nota(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)

    for x in aluno_nota:
        lista_media = []
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(aluno)
        print(lista_notas)
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

# def copia_arquivo (nome_arquivo):
#
#     shutil.copy(nome_arquivo, '/Users/jgustavo/Desktop/programacao/teste')
# # def move_arquivo(nome_arquivo):
# #     shutil.move(nome_arquivo, '/Users/jgustavo/Desktop/notax.txt')

if __name__ == '__main__':

    print(escrever_arquivo('notax.txt'))
    lista_media = media_nota('notax.txt')
    print(lista_media)
    # aluno = 'Pedro,10,10,10,9\n'
    # atualiza_arquivo('notax.txt', aluno)