'''
Desafio
Crie um script que:

Liste todos os arquivos em um diretório e subdiretórios.
Exiba o tamanho formatado de cada arquivo.
Mostre apenas os 3 maiores arquivos (com caminho completo e tamanho).
💡 Dica: Utilize uma lista para armazenar os arquivos e seus tamanhos,
depois ordene-a com sorted.
'''
import math
import os


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:

    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = tamanho_em_bytes / potencia

    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('\\temp', 'ws-Python', 'treino')
print(caminho)
arquivos_tamanhos = []

# Percorre os arquivos no diretório
for root, dirs, files in os.walk(caminho):
    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        tamanho = os.stat(caminho_completo).st_size
        arquivos_tamanhos.append((caminho_completo, tamanho))

# Ordena a lista do maior para o menor tamanho
arquivos_tamanhos.sort(key=lambda x: x[1], reverse=True)

# Seleciona os 3 maiores arquivos
maiores_arquivos = arquivos_tamanhos[:3]

print("Os 3 maiores arquivos são:")
for arquivo, tamanho in maiores_arquivos:
    print(f"{arquivo} - {formata_tamanho(tamanho)}")
