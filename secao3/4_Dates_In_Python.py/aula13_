# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join('\\temp', 'ws-Python', 'treino')
NOVA_PASTA = os.path.join('\\temp', 'ws-Python', 'NOVA_PASTA')

# cria uma nova pasta com essa direcao.'NOVA_PASTA'
# exist_ok , serve para criar pasta mesmo, uma ja existindo (substitui!)
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            # serve para recriar as pastas, pois da erro, por n encontra-las
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        # print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            # ELE substitui no texto, pasta original, por nova pasta
            # com isso corrige o caminho da pasta.
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

'''
Resumo da Aula
Nesta aula, aprendemos como copiar arquivos e diretórios usando as bibliotecas
os e shutil no Python. Isso é útil para criar backups ou organizar dados
em novos locais de forma programada.

Principais Conceitos
os.makedirs:

Cria pastas, mesmo se já existirem, usando o parâmetro exist_ok=True.
shutil.copy:

Copia arquivos de um local para outro, preservando os dados.
os.walk:

Percorre diretórios de forma recursiva, listando pastas e arquivos.
Exemplo Simplificado
Aqui está um exemplo básico de como copiar todos os arquivos de uma pasta para
outra:

python
Copiar código
import os
import shutil

# Diretórios
pasta_origem = 'caminho/da/origem'
pasta_destino = 'caminho/do/destino'

# Cria a pasta de destino se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Copia arquivos
for root, dirs, files in os.walk(pasta_origem):
    for file_ in files:
        origem = os.path.join(root, file_)
        destino = os.path.join(pasta_destino, file_)
        shutil.copy(origem, destino)
Utilidades Práticas
Backup automático: Copiar arquivos importantes para outro local.
Organização de dados: Mover arquivos para pastas específicas.
Recriar estruturas: Criar uma cópia exata de diretórios e arquivos.
Aplicação Prática com Estruturas
Neste exemplo, preservamos a estrutura de subpastas ao copiar arquivos:

python
Copiar código
import os
import shutil

# Caminhos
origem = 'caminho/origem'
destino = 'caminho/destino'

# Cria a pasta de destino
os.makedirs(destino, exist_ok=True)

# Recria a estrutura de diretórios
for root, dirs, files in os.walk(origem):
    for dir_ in dirs:
        nova_pasta = os.path.join(
            root.replace(origem, destino), dir_)
        os.makedirs(nova_pasta, exist_ok=True)

    # Copia os arquivos
    for file_ in files:
        origem_arquivo = os.path.join(root, file_)
        destino_arquivo = os.path.join(
            root.replace(origem, destino), file_)
        shutil.copy(origem_arquivo, destino_arquivo)
'''
