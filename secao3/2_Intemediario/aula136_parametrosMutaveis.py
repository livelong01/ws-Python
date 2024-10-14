#Problema dos parametros mutaveis em funcoes python.

def adc_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
#como corrigir o problema. :
#1) criar antes o parametro.
# lista1 = []
#2) O ideal é n usar os parametros padrao... exemplo: 
# se for mutavel, use o None. fazer o if acima! 


cliente1 = adc_clientes('luiz')
adc_clientes('joana', cliente1)
adc_clientes('joao', cliente1)
print(cliente1)

cliente2 = adc_clientes('Helena')
adc_clientes('Maria', cliente2)
print(cliente2)

cliente3 = adc_clientes('rafael')
adc_clientes('charles', cliente3)
print(cliente3)