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

# arquivo = open(caminho_arquivo, 'w')
# '''
# w, = cria arquivo

# '''
# #SEMPRE FECHAR ARQUIVO!!!
# arquivo.close()


#(context manager)Uma forma de abrir e fechar automaticamente, é usando o "with open"

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
         ) # mais usado para escrever ITERAVEIS.
    # arquivo.seek(0,0) #mover pro topo do arquivo, nao se utiliza mt.
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # para o print n pular linha 
    print(arquivo.readline().strip()) #retorna sem espaços e quebras de linha do texto.
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip()) #tirar a quebra de linha a mais.

print('#'* 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    #Linha 1
    #Linha 1
    print('lendo')
    