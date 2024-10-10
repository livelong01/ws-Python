"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:  #primeiro, pus != "" (vazio), mas como vazio é falsy, bastava n por nada, como o professor.
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome :
            print("Seu nome contém espaços")
    else:
            print("Seu nome NÃO contém espaços")

    quantidadeLetras = len(nome)

    print(f'Seu nome tem {quantidadeLetras} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}') #O professor fez com indice negativo, o ultimo sempre é -1! #vai da ultima letra -1, ate o fim ( n pus nada indicando ate o fim) fiz assim:"nome[len(nome)-1:]""
else:
    print("Desculpe, você deixou campos vazios.")    








