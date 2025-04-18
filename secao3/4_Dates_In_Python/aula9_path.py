# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('\\temp', 'ws-Python', 'arquivo.txt')
print(caminho)
diretorio, arquivo = (os.path.split(caminho))
diretorio_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(diretorio)
print(arquivo)
print(diretorio_arquivo)
print(extensao_arquivo)
print(os.path.exists(caminho))  # ver se o caminho existe.
print(os.path.abspath('.'))  # pwd, mostra o local atual do arquivo.
print(os.path.basename(caminho))  # pega a parte final do endereço
print(os.path.basename(diretorio))  # nesse caso "ws-python"
print(os.path.dirname(caminho))  # mostra tudo menos a extersao.
print(os.path.getsize(
    "\\Users\\jonat\\Videos\\vlc-record-2024-05-13-20h09m20s-FL FILMES PREMIUM-.mp4"))
