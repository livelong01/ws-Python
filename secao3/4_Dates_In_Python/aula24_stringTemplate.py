# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path
import json


CAMINHO_ARQUIVO = Path(__file__).parent / 'aula24.txt'
locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    # val = numero, symbol = mostr R$, pq ele poe no final e n é bom.
    # grouping = true, pra por o ponto no local correto no brasil.
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Joao',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

print(json.dumps(dados, indent=2, ensure_ascii=False))
''' RESULTADO:
{
  "nome": "Joao",
  "valor": "R$ 1.234.456,00",
  "data": "28/12/2022",
  "empresa": "O. M.",
  "telefone": "+55 (11) 7890-5432"
}
'''
# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor}no dia $data.
# Caso deseje cancelar o serviço, entre em contato com a $empresa
# pelo telefone $telefone.

# Atenciosamente,

# ${empresa},
'''
# template = string.Template(texto)
# print(template.substitute(dados))  # PROBLEMA: ela dá erro se umas das
#  variaveis nao existir.
# print(template.safe_substitute(dados)) #ele envia sem alocar a variavel(PIOR)


# '''  # RESULTADO DO PRINT:
# Prezado(a) Joao,

# Informamos que sua mensalidade será cobrada no
# valor de R$ 1.234.456, 00 no dia 28/12/2022.
# Caso deseje cancelar o serviço, entre em contato com a O. M.
# pelo telefone + 55 (11) 7890-5432.

# Atenciosamente,

# O. M.,

# caso queira seu proprio delimitador... (nao aconselhado)


class MyTemplate(string.Template):
    delimiter = '%'  # VAI SER % ao inves do padrao: $


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados,))
