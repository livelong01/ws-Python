import os
import json

def adicionar(string, lista_tarefas):
    lista_tarefas.append(string)
    return lista_tarefas

def mostrar(lista_tarefas):
     print('TAREFAS: ')
     for tarefa in lista_tarefas:
          print(tarefa)

def desfazer(lista_tarefas, lista_desfazer):
    return adicionar(lista_tarefas.pop(), lista_desfazer)

def ler(lista_geral, caminho_arquivo):
    try:
        dados = []
        with open(caminho_arquivo, 'r', encoding= 'utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo nao existe')
        salvar(lista_geral, caminho_arquivo)
    return dados

def salvar(lista_geral, caminho_arquivo):
    dados = lista_geral
    with open(caminho_arquivo, 'w', encoding= 'utf8') as arquivo:
            dados = json.dump(lista_geral, arquivo, indent=2, ensure_ascii= False )
    return dados


CAMINHO_ARQUIVO = "aula119.json"
lista_geral = ler([], CAMINHO_ARQUIVO)
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
        print()
    salvar(lista_geral, CAMINHO_ARQUIVO )
