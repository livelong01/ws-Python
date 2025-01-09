# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

# data = datetime(2024, 4, 20, 20, 3, 52)
# print(data)


data_str = '2024/04/20 20:03:52'
data_str_frmt = '%Y/%m/%d %H:%M:%S'
data2 = datetime.strptime(data_str, data_str_frmt)
print(data2)

data_str2 = '11/12/2024'
data_str2_fmt = '%d/%m/%Y'
data3 = datetime.strptime(data_str2, data_str2_fmt)
print(data3)


data1 = datetime.strptime("17/04/2020 08:00:00", '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime("17/04/2020 09:00:00", '%d/%m/%Y %H:%M:%S')
data3 = datetime.strptime("17/04/2020 10:00:00", '%d/%m/%Y %H:%M:%S')


def escolha(opcao):
    while True:
        try:
            n = int(input(opcao))
        except (ValueError, TypeError):
            print('DIGITE UMA OPÇÃO VÁLIDA')
            continue
        except (KeyboardInterrupt):
            print('usuario n digitou nada')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu_horarios(lista):
    cabecalho('Horários disponíveis para reunião do DA')

    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())
    opc = escolha('Qual sua opção? ')
    return opc


# menu_horarios(['opcao', '2', '3'])
while True:
    resposta = menu_horarios([data1.time(), data2.time(), data3.time(),
                              'Nenhum dos horários'],)
    # resposta = menu_horarios(['1 ','2','3','Nenhum dos horários'],)
    if resposta == 1:
        print(f' Só posso ás {data1.time()} horas ')
        break
    elif resposta == 2:
        print(f' Só posso ás {data2.time()} horas')
        break
    elif resposta == 3:
        print(f'Só posso às {data3.time()} horas')
        break
    elif resposta == 4:
        print("Usuário saiu do programa.")
        break
    else:
        print('digite uma opção valida!')
