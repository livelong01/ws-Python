# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
import locale
from dateutil.relativedelta import relativedelta

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

prestacoes = 16666.67
fmt = '%d/%m/%Y'

while True:
    try:
        valor_emprestimo = float(input('Qual o valor do empréstimo? '))
    except ValueError:
        raise TypeError('Por favor, insira um número válido '
                        '(inteiro ou decimal).')
    try:
        tempo_pagamento = int(input('Em quantos anos será pago?'))
    except ValueError:
        raise TypeError('Por favor, insira um número válido (inteiro)')
    meses = tempo_pagamento * 12
    prestacoes = valor_emprestimo/(meses)
    emprestimo_formatado = locale.currency(prestacoes,
                                           grouping=True, symbol=True)
    print(emprestimo_formatado)

    dia = '0'
    mes = '0'
    ano = '0'

    try:
        while len(dia) != 2:
            dia = input('Qual dia do pagamento '
                        '(escreva com dois digitos e até 31, ex: 02)? ')
        while len(mes) != 2:
            mes = input('Qual mês do pagamento '
                        '(escreva com dois digitos e até 12, ex: 02)?')
        while len(ano) != 4:
            ano = input('Qual ano do pagamento '
                        '(escreva com quatro digitos, ex: 2018)?')
    except ValueError:
        raise TypeError('Por favor, insira um número válido (inteiro)')

    data_sem_formatacao = f'{ano}-{mes}-{dia}'
    data_formatacao = datetime.strptime(data_sem_formatacao, '%Y-%m-%d')
    data_formatada = data_formatacao.strftime(fmt)

    # print(data_formatada.strftime)
    print(f'Resumo: O emprestimo foi de {emprestimo_formatado},\
feito em {data_formatada}')

    delta = relativedelta(months=1)

    for indice in range(meses):
        print(f'{data_formatada} Parcela Nº{indice+1}: {emprestimo_formatado}')
        data_formatacao += delta
        data_formatada = data_formatacao.strftime(fmt)
