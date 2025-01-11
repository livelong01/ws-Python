# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula21.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av B, 3A'},
]

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Luiz Otávio', 'Av B, 3A']
# ]

# with open(CAMINHO_CSV, 'w', encoding='UTF8', newline='') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']  # tmb funciona com lista.
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         # print(cliente.values())
#         # escritor.writerow(cliente.values())
#         escritor.writerow(cliente)

# FORMA FACIL COM DICCIONARIO:

with open(CAMINHO_CSV, 'w', encoding='UTF8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas  # field name é obrigatorio.
    )
    escritor.writeheader()  # cabeçalho

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# e TEM O MESMO RESULTADO NO FINAL!
