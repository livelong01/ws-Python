"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

letras = 'rail'
lista = []
while True:
    print('Selecione uma opção: ')
    escolha = input('[i]nserir [a]pagar [l]istar [r]esetar: ').lower()

    if len(escolha)>1 or escolha not in letras :
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Escolha uma opção válida!')
    elif escolha == 'i': 
        os.system('cls' if os.name == 'nt' else 'clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif escolha == 'a':
        try:
            indice = int(input('Escolha um indice para apagar: '))
            lista.pop(indice)
        except IndexError:
            print('Digite um número de indice existente.')
        except ValueError:
            print('Digite um numero inteiro')
        except Exception:
            print('Erro desconhecido')
    elif escolha == 'l':
        if lista != []:
            os.system('cls' if os.name == 'nt' else 'clear')
            for indice, produto in enumerate(lista):
                print(indice, produto)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Nada para listar')
    elif escolha == 'r':
        lista.clear()


