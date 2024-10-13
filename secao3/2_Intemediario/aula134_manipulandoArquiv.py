# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = r"C:\\temp\\ws-Python\\" # ou vc inverte as barras ou poe 2 barras, normalmente colocam 2.
caminho_arquivo += "aula116.txt"

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: #w apaga o arquivo e reescreve por CIMA.
    #encoding='utf8'// serve pra deixar a codificacao do win, a mesma do vscode, UTF-8, que aceita acentuacao do Portugues.
    arquivo.write('Atenção!\n') # nao aparece a acentuacao
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
         )

'''
o "a+" permite vc escrever o arquivo, ele n apaga e reesscreve por CIMA
ele vai pra ultima linha e escreve abaixo dela. Cada vez que 
voce reeativar o codigo, ele reescreve mais abaixo repetidamente.
'''

# with open(caminho_arquivo, 'b') as arquivo: #w apaga o arquivo e reescreve por CIMA.
     #MODO BINARIO


import os

# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo) #AMBOS APAGAM O ARQUIVO.

#RENOMEAR:
# os.rename(caminho_arquivo, 'aula116-2.txt')