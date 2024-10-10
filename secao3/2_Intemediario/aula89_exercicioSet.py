"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def primeiro_duplicado(listas):
    lista_resultado = []  #cria uma lista com o resultado de cada lista.
    conjunto = set() #cria um conjunto para medir o tamanho do set.
    for lista in listas: # faz um for em cada lista de uma vez
        if len(lista) != len(set(lista)): # verifica se a lista tem repetidos
            conjunto.clear() 
            for numero in lista: # for na lista individual.
                tam_Antes = len(conjunto) #verifica o tamanho do conjunto antes de adc o prox numero
                conjunto.add(numero) # adc o numero
                tam_Depois = len(conjunto) #caso o numero seja repetido, o tamanho n muda.
                if tam_Antes == tam_Depois: # se o tamanho n muda, adc o numero repetido.
                    lista_resultado.append(numero) 
                    break # break e vai pra prox lista.
        else:
            lista_resultado.append(-1) # caso o conjunto n tenha repetido, adc -1 a lista resultado.
    return lista_resultado # mostra o resultado para CADA lista.
    

print(primeiro_duplicado(lista_de_listas_de_inteiros))

###############RESPOSTA DO PROFESSOR#####################################


def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )
    '''
    O professor criou um conjunto que adc numeros, porem o if verifica se o numero
    ja esta na lista anterior, se tiver ele printa o numero, se n tiver nenhum repetido,
    no fim ele retorna a costante "primeiro_duplicado" que tem valor de -1
    
    '''