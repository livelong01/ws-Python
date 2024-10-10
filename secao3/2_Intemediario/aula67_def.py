'''
Introducao as funcoes (def) em python
Funcoes sao trechos de codigo usados para replicar
determinada acao ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrao, funcoes Python retornam None (nada).
'''
# def Print(a, b, c):
#     print(a + b)

# Print(15, 8)

'''
Parametro sao a, b, c na funcao à definir, enquanto
argumento sao os valores dados aos parametros, quando
chamada a funcao.
'''
# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 3)

def saudacao(nome= 'sem nome'):
    print(f' Olá, {nome}!')

nome = input('Qual seu nome? ')
saudacao(nome)
saudacao('Luiz')