''' Calculadora com while '''

while True:
    resultado = None
    num1 = input('Digite o primeiro numero: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Escolha o operador: [/], [//], [*], [**], [%], [+], [-] ')
    
    numeros_validos = None
    try:
        num1 = float(num1)
        num2 = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados sao inválidos.')
        continue

    operadores_permitidos = '+/-*//%**'

    if operadores_permitidos not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador)>2:
        print('Digite apenas um operador.')
        continue


    if operador == "/":
        resultado = num1/num2
    elif operador == "//":
        resultado = num1//num2
    elif operador == "*":
        resultado = num1*num2
    elif operador == "**":
        resultado = num1**num2
    elif operador == "%":
        resultado = num1%num2
    elif operador == "+":
        resultado = num1+num2
    elif operador == "-":
        resultado = num1-num2
    else: 
        print("Nunca deveria chegar aqui!")
        continue
        
    print(f'O resultado de {num1} {operador} {num2} = {resultado:.2f}')

    sair = input('Quer sair? [s]: ').lower().startswith('s')

    if sair is True:
        break