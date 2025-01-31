# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela.',
    # type=str, #tipo do argumento
    metavar='STRING',
    # default='Olá Mundo', #"valor padrao"
    required=False,  # o valorpadrao n funciona qd ta true, pq ele requer o argumento
    # nargs='+') #recebe mais de um valor
    action='append',  # recebe mais de um valor de uma vez
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Voce nao passou o valor de b')
    print(args.basic)
else:
    print('o valor de basic: ', args.basic)

print(args.verbose)
