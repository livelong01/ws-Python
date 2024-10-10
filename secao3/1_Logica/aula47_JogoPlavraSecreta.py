"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

#PALAVRA SECRETA E MONTADA
palavra_secreta = 'perfume'.lower()
palavra_montada = ''
#INDICE PARA N DE TENTATIVAS
contador = 0

#while para o jogo rodar infinitamente.
while True:
    
    #reset da palavra secreta 
    palavra_pronta = len(palavra_secreta) * '*'

    #segundo while para verificar se vc venceu
    while palavra_pronta != palavra_secreta: 
        letra_digitada = input('Digite uma letra: ').lower()

        contador += 1
        #verificador de problemas (numeros e >2 letras)
        if letra_digitada.isdigit() == True:
             print('Números são inválidos!') 
             continue
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra!')
            continue
            #iterador da palavra secreta
        if letra_digitada in palavra_secreta:
            palavra_montada = ''
            #mostra a letra digitada se for encontrada na palavra sec
            for i in palavra_secreta:
                if i == letra_digitada:
                    palavra_montada += i
                else:
                    palavra_montada += '*'
        #cria um indice pra guardar as letras e acumular eleas ao serem descobertas
            for j in range(len(palavra_montada)):
                if palavra_montada[j] != '*':
                    palavra_pronta = palavra_pronta[:j] + palavra_montada[j] + palavra_pronta[j+1:]
                
        #printa o resultado atual DA PALAVRA ex: ***a***
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Palavra formatada {palavra_pronta}')
    #limpa o terminal e sai do primeiro while, qd palav sec == palavra pronta.
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('PARABENS, VOCE GANHOU!')
    print(f'A palavra formatada: {palavra_secreta}')
    print(f'TENTATIVAS {contador}!')
    #recomeça, tudo de novo!

    #############forma do professor ##############

#     palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0
      
    
    



