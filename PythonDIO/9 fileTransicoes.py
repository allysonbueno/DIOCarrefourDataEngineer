import shutil
# Gere, copie, mova, escreva e leia informações de arquivos externos
    # arquivo = open('teste.txt', 'w')
    # arquivo = open('teste.txt', 'a')
    # arquivo.write('Primeira Escrita')
    # arquivo.write('\nSegunda Linha')
    # arquivo.write('\nTerceira Linha')
    # arquivo.close()

def escrever_arquivo(texto):
    diretorio = 'C:/Estudos/PythonDIO/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        # print(aluno)
        # print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        # print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Estudos/PythonDIO/copiados/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Estudos/PythonDIO/copiados/')

if __name__ == '__main__':
    escrever_arquivo('Primeira Linha.\n')
    # atualizar_arquivo('Segunda Linha.\n')
    # atualizar_arquivo('Terceira Linha.\n')
    # ler_arquivo('teste.txt')

    # atualizar_arquivo('notas.txt', aluno)
    # aluno = 'João, 8, 7, 6, 5'
    # aluno = '\nJezz, 9, 9, 10, 9'
    # aluno = '\nAllan, 5, 6, 7, 5'
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # copia_arquivo('notas.txt')
    move_arquivo('notas.txt')


