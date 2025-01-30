# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
print(argumentos)
qtd_argumentos = len(argumentos)
# print(qtd_argumentos)

if qtd_argumentos <= 1:
    print("Voce nao passou argumentos")
else:
    try:
        print(f'voce passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com o argumento {argumentos[1]}')
        print(f'Faça outra coisa com o argumento {argumentos[2]}')
    except IndexError:
        print("Faltam argumentos")

if len(sys.argv) < 3:
    print("Uso: python script.py nome cor")
else:
    nome = sys.argv[1]
    cor = sys.argv[2]
    print(f"{nome}, sua cor favorita é {cor}!")
