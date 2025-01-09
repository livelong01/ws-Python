# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('\\temp', 'ws-Python', 'treino')
print(caminho)
counter = count()

for root, dirs, files in os.walk(caminho):  # mostra os caminhos.
    the_counter = next(counter)
    print(the_counter, 'pasta atual', root)

    for dir_ in dirs:  # mostra todas as pastas e as dentro destas.
        print('     ', the_counter, 'Dir: ', dir_)

    for file_ in files:  # mostra todas as pastas e as dentro destas.
        caminho_completo_arquivo = os.path.join(root, file_)
        print('     ', the_counter, 'Files: ', caminho_completo_arquivo)
        os.unlink(caminho_completo_arquivo)  # não use isso (VAI APAGAR TUDO
        # DENTRO DAS PASTAS (OS ARQUIVOS))


''' RESUMO DA AULA.
A função os.walk é utilizada em Python para navegar recursivamente por
estruturas de diretórios. Ela retorna uma sequência de tuplas contendo:

root: O caminho do diretório atual sendo processado.
dirs: Uma lista de subdiretórios presentes no diretório atual.
files: Uma lista de arquivos presentes no diretório atual.
O código apresentado utiliza os.walk para:

Exibir o caminho do diretório atual (root).
Listar os subdiretórios encontrados (dirs).
Listar os arquivos encontrados (files) e seus caminhos completos.
Adicionalmente, o código usa itertools.count para contar quantos
diretórios foram processados.
'''
