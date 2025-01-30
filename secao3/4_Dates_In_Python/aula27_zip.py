# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile
# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_27_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula27_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula27_descompactado'
print(CAMINHO_RAIZ)
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(11, CAMINHO_ZIP_DIR)


# parte 2: da aula (USANDO O ZIP)
# CRIANDO UM ZIP E ADICIONANDO ARQUIVOS
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            print(file)
            zip.write(os.path.join(root, file), file)  # file dps da virgula
            # serve para eu por o arquivo sem o caminho das pastas completas.
            # que é a forma padrao do zip.write.

# LENDO ARQUIVOS DE UM ZIP.
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# DESEMPACOTANDO(extraindo) ARQUIVOS DO ZIP EM UM LOCAL ESPECF.
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
