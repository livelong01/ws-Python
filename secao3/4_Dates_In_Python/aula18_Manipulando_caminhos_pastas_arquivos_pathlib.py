# aula do youtune.
from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(caminho_projeto.absolute())  # C:\temp\ws-Python

caminho_arquivo = Path(__file__)
# c:\temp\ws-Python\secao3\4_Dates_In_Python.py\
# aula18_Manipulando_caminhos_pastas_arquivos_pathlib.py
print(caminho_arquivo)
print(caminho_arquivo.parent)  # pega apenas o diretorio. (sem o arquivo)
# c:\temp\ws-Python\secao3\4_Dates_In_Python

# pega apenas o diretorio. (sem o arquivo)
print(caminho_arquivo.parent.parent)  # vai entrando nas paster anteriores.
# c:\temp\ws-Python\secao3

# vai entrando nas paster anteriores.
print(caminho_arquivo.parent.parent.parent.parent)
# c:\temp

print(caminho_arquivo.parent.parent.parent.parent.parent)
# c:\
# ATÉ CHEGAR NA RAIZ.

ideias = caminho_arquivo.parent / 'ideias'
print(ideias)  # cria o ccaminho (nao o diretorio de fato.)
# c:\temp\ws-Python\secao3\4_Dates_In_Python\ideias

print(ideias / 'arquivo.txt')
# c:\temp\ws-Python\secao3\4_Dates_In_Python\ideias\arquivo.txt

print(Path.home() / 'Desktop')  # pegar o desktop ou home.

# TUDO FICA EM MEMORIA, N CRIA NADA. SÓ GERA O CAMINHO.

# PARA CRIAR O ARQUIVO :

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch()  # agora vai criar o arquivo no desktop
print(arquivo)
# arquivo.write_text('''
# Olá amigo!
#                    tudo bem?
#                    quanto tempo nao nos vemos!''')
# print(arquivo.read_text())  # PARA LER O ARQUIVO
# arquivo.unlink() # APAGAR O ARQUIVO.

# caminho_arquivo2 = Path.home() / 'Desktop' / 'arquivo.txt'

# with caminho_arquivo2.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo2.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Python é Legal'
caminho_pasta.mkdir(exist_ok=True)  # cria uma PASTa
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)  # cria uma subpasta

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey!\n <b>Hello<\r>')

outro_arquivo = caminho_pasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey!\b')

# transtornos que podem ser causados!

# caminho_pasta.rmdir()
# caminho_pasta.unlink()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file{i}.txt'
    file.touch()

    # if file.is_file() se é um arquivo
    if file.exists():  # se ele existe.
        # if file.dir() se é um diretorio
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta) #apaga tudo recursivamente!


def rmtree_(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree_(file, False)  # recursao (funcao dentro da propria funcao)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
