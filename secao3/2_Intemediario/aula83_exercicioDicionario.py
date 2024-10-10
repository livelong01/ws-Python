

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opcoes' : ['1', '2', '3', '4'],
        'Resposta' : '4'
    },
    {
       'Pergunta' : 'Quanto é 5 x 5? ',
       'Opcoes' : ['25' , '55', '10' , '51'] , 
       'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10 / 2? ',
        'Opcoes' : ['4' , '5', '2' , '1'] , 
        'Resposta' : '5',
    }
]

# def questionario():
# print(perguntas[0]['Opcoes'][0]) #Quanto é 2+2?
nota=0
for chave in perguntas: #faz um for pra acessar os dados do dicionario
    opcao=''

    print("Pergunta: ", chave['Pergunta']) #acessa a perguntas do dicionario 'Pergunta'
    print()
    print('Opções: ')
    opcoes = chave['Opcoes'] #acessa as oopcoies de resposta do questionario
    for i, valores in enumerate(opcoes): #esse for cria um enumarate, pra n precisar usar o "i+=1" e entra na lista das opcoes.
        print(f'{i}) {valores}')
        i+=1

    opcao = input('Escolha uma opção: ')

    acertou = False #Inicia com falso, para ser alterado caso a pessoa acerte.
    opcao_int = None #inicia como None, para mudar, caso a pessoa digite uma opcao valida.
    qtd_opcoes = len(opcoes) # tamanho da qtd das opcoes, para saber se a pessoa digitou um numero valido.

    if opcao.isdigit():# verifica se é um numero
        opcao_int=int(opcao)

    if opcao_int is not None:# se for numero( e nao um None )
        if opcao_int >=0 and opcao_int< qtd_opcoes:  #se esta entre as opcoes possiveis.
            if opcoes[opcao_int] == chave['Resposta']: # se o que a pessoa digitou é igual a resposta
                acertou = True 
    if acertou: # se acertou mudou para TRUE printa acertou e soma 1 na nota!
        nota +=1
        print('Acertou ✅ ')
        print()
    else:
        print('Errou ❌')
        print()

print(f'Voce acertou {nota}' 
      '\n de 3 perguntas.')
    
    
        
