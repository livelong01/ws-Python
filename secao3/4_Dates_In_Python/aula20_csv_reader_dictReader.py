# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula19_csv2.csv'

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
        # print(linha[1])  # pode pegar apenas o indice tmb.


# OUTRA FORMA DE LER É COM O DICT!

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor2 = csv.DictReader(arquivo)

    for linha in leitor2:
        print(linha)
        # print(linha['Nome']) #pode chamar so o Nome, etc.
