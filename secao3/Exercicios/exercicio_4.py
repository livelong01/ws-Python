#exercicios de funcao lambda

# Sua função lambda aqui
soma = lambda x, y: x + y
soma(2,3) #5
# Teste: use soma(3, 5) e veja o resultado.

#---------------------
# # Crie uma função lambda chamada 'par' que verifica se um número é par
par = lambda x : x%2 == 0
par(7)
print(par(7), par(2))
#---------------------
# Crie uma função lambda chamada 'multiplicar_por_10' que retorna o valor multiplicado por 10
multiplicar_por_10 = lambda x: x*10
print(multiplicar_por_10(4))
#---------------------
# Crie uma função lambda chamada 'comprimento' que retorna o comprimento de uma string
comprimento = lambda comprimento: len(comprimento)
print(comprimento('cavalo'))
#---------------------
# Crie uma função lambda chamada 'quadrado' que retorna o quadrado do número
quadrado = lambda x: x**2
print(quadrado(5))
#---------------------
# Crie uma função lambda chamada 'primeiro_caracter' que retorna o primeiro caractere de uma string
primeiro_caracter = lambda primeiro: primeiro[0]
print(primeiro_caracter('cavalo'))
#---------------------
# Crie uma função lambda chamada 'maior' que retorna o maior de dois números
maior = lambda x, y: x if x>y else y # RETORNA X, SE X FOR MAIOR QUE Y E CASO CONTRARIO RETORNA Y
print(maior(10,15))
#---------------------
# Crie uma função lambda chamada 'maiusculas' que retorna a string em letras maiúsculas
maiusculas = lambda string: string.upper()
print(maiusculas('jonathan'))
#---------------------
# Crie uma função lambda para filtrar os números positivos de uma lista
numeros = [-1, 2, -3, 4, -5]
# Use a função lambda junto com a função filter para fazer isso
positivos = list(filter(lambda x: x > 0, numeros))  # CRIA UMA LISTA, COM UM FILTRO, DE UM LADO A FUNCAO LAMBDA ANALISA CADA ITEM DA LISTA, DO OUTRO, A LISTA "numeros"
print(positivos)
#---------------------
# Crie uma função lambda chamada 'divisivel_por_5' que verifica se um número é divisível por 5
divisivel_por_5 = lambda x: x%5 == 0
print(divisivel_por_5(3), divisivel_por_5(15))

