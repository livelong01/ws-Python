# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('\\temp', 'ws-Python', 'treino')
print(caminho)
counter = count()

for root, dirs, files in os.walk(caminho):  # mostra os caminhos.
    the_counter = next(counter)
    print(the_counter, 'pasta atual', root)

    for dir_ in dirs:  # mostra todas as pastas e as dentro destas.
        print('     ', the_counter, 'Dir: ', dir_)

    for file_ in files:  # mostra todas as pastas e as dentro destas.
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo) #FORMA 1
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size  # FOrma n2, usando STATS
        print('     ', the_counter, 'Files: ', file_, formata_tamanho(tamanho))
        # os.unlink(caminho_completo_arquivo)


'''
Resumo da Aula
Nesta aula, você aprendeu sobre como obter dados detalhados sobre arquivos,
como o tamanho em bytes, usando as funções os.path.getsize e os.stat.
Além disso, utilizou-se uma função personalizada, formata_tamanho, para
converter tamanhos de arquivos em formatos mais legíveis, como KB, MB, ou GB.

Principais Conceitos
os.path.getsize:

Retorna o tamanho de um arquivo em bytes.
Útil para verificar rapidamente o tamanho de um arquivo.
os.stat:

Oferece informações detalhadas sobre um arquivo, como:
Tamanho em bytes (st_size).
Data de criação/modificação (st_ctime, st_mtime).
Permissões.
É mais completo que os.path.getsize.
Função formata_tamanho:

Formata o tamanho do arquivo para uma unidade mais compreensível.
Converte bytes em KB, MB, GB, etc., utilizando logaritmos.
Exemplo de Código Simplificado
Abaixo, um exemplo de como usar os.stat e os.path.getsize para listar
tamanhos de arquivos:

python
Copiar código
import os
import math

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacoes = ["B", "KB", "MB", "GB", "TB"]
    indice = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice
    tamanho_formatado = tamanho_em_bytes / potencia
    return f"{tamanho_formatado:.2f} {abreviacoes[indice]}"

# Caminho do diretório
caminho = os.path.join('temp', 'ws-Python', 'treino')

# Percorre os arquivos e exibe informações
for root, dirs, files in os.walk(caminho):
    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        
        # Obtendo tamanhos
        tamanho_getsize = os.path.getsize(caminho_completo)  # Método 1
        tamanho_stat = os.stat(caminho_completo).st_size    # Método 2

        # Exibindo o tamanho formatado
        print(f"Arquivo: {file_}")
        print(f"  Tamanho (getsize): {formata_tamanho(tamanho_getsize)}")
        print(f"  Tamanho (stat): {formata_tamanho(tamanho_stat)}")
Utilidades Práticas
Análise de espaço em disco: Identificar arquivos que consomem muito
espaço.
Organização de arquivos: Listar e categorizar arquivos por tamanho.
Backup ou limpeza: Encontrar arquivos grandes para backup ou exclusão.
Monitoramento de logs: Verificar tamanhos de arquivos de log para
evitar que cresçam demais.
Exemplo de Aplicação Prática
Vamos supor que você queira listar todos os arquivos maiores que 10 MB em
uma pasta:

python
Copiar código
limite_tamanho = 10 * 1000**2  # 10 MB

for root, dirs, files in os.walk(caminho):
    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        tamanho = os.stat(caminho_completo).st_size

        if tamanho > limite_tamanho:
            print(f"Arquivo grande encontrado: {file_} -
                    {formata_tamanho(tamanho)}")
'''
