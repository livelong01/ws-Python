# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# ALT + \/ OU ALTA + /\ move a linha pra cima ou baixo. sem copiar.



# def recursiva(inicio=0, fim = 4):
#     #CASO BASE
#     print(inicio, fim)
#     if inicio >= fim:
#         return fim
    
#     #caso recursivo:
#     #contar até chegar ao final.
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva()) ## stackoverflow: Ele deixa muita coisa na pilha, em espera e quebra pra n quebrar o pc.

# def factiorial(n):
#     if n <= 1:
#         return 1
#     return n * factiorial(n-1)

# print(factiorial(1000))


y=1
for x in range(4):
    y += y * (x + 1)

print(y)