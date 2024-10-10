# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    
    return total
result_mult = multiplicacao(1,2,3,4,5)
print(result_mult)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return f'O {numero} é par!'
    return f'O {numero} é impar!'

print(par_impar(5))
print(par_impar(6))

