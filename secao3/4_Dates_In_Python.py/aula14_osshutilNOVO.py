# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join('\\temp', 'ws-Python', 'treino')
NOVA_PASTA = os.path.join('\\temp', 'ws-Python', 'NOVA_PASTA')

# shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EitA')  # renomeia / mover


'''
Resumo da Aula
Nesta aula, você aprendeu como usar os módulos os e shutil para manipular
arquivos e pastas. Aqui estão as operações mais importantes:

Copiar arquivos e pastas:

shutil.copy copia arquivos individuais.
shutil.copytree copia pastas inteiras, incluindo subpastas e arquivos.
Apagar arquivos e pastas:

os.unlink remove arquivos.
shutil.rmtree apaga pastas de forma recursiva.
Mover e renomear:

shutil.move pode mover ou renomear arquivos/pastas.
os.rename também renomeia arquivos/pastas.
Exemplo Prático
O exemplo copia uma pasta inteira (PASTA_ORIGINAL) para NOVA_PASTA,
depois a renomeia para NOVA_PASTA_EitA. Se a pasta NOVA_PASTA já existe,
o parâmetro dirs_exist_ok=True permite a cópia sem erros.

Desafio
Crie um script que:

Apague todos os arquivos .log de uma pasta específica.
Mova os arquivos .txt para uma nova pasta.
Renomeie a pasta para "Meus_Textos".
Boa sorte! 🚀
'''
