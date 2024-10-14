# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
def adicionar(string, lista_tarefas):
    lista_tarefas.append(string)
    return lista_tarefas

def mostrar(lista_tarefas):
     print('TAREFAS: ')
     for tarefa in lista_tarefas:
          print(tarefa)

def desfazer(lista_tarefas, lista_desfazer):
    return adicionar(lista_tarefas.pop(), lista_desfazer)


lista_geral = []
lista_desfazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    main_string = input("Digite uma tarefa ou comando: ")
    if main_string.lower() == "listar":
        print()
        if lista_geral:
            mostrar(lista_geral)
        else:
            print('Nada a listar')
        print()
    elif main_string.lower() == "desfazer":
        print()
        if lista_geral:
            desfazer(lista_geral, lista_desfazer)
            mostrar(lista_geral)
        else:
            print('Nada a desfazer')
        print()
        
    elif main_string.lower() == "refazer":
        print()
        if lista_desfazer:
            desfazer(lista_desfazer, lista_geral)
            mostrar(lista_geral)
        else:
            print('Nada a refazer')
        print()
    elif main_string.lower() == 'clear':
        os.system('cls')           
    else:
        print()
        adicionar(main_string, lista_geral)
        mostrar(lista_geral)
        print("❤🙌🤦‍♀️😎")
