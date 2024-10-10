'''
Crie uma função contador() que retorne uma função interna. Essa função interna,
quando chamada, deve aumentar um valor contado toda vez que for chamada e retornar o valor atual.
'''
# def contador ():
#     contagem = 0
#     def aumenta():
#         nonlocal contagem
#         contagem += 1
#         return contagem
#     return aumenta

# contador1 = contador()

# print(contador1())# 1
# print(contador1())# 2
# print(contador1())# 3

'''
Exercício 2: Multiplicador
Crie uma função criar_multiplicador(multiplicador) que retorne uma função interna. 
A função interna deve receber um valor e multiplicá-lo pelo multiplicador passado na função externa.
'''

# def criar_multiplicador(multiplicador):
#     def multiplicando(x):
#         return x * multiplicador
#     return multiplicando

# multi_por_cinco = criar_multiplicador(5)

# print(multi_por_cinco(10))

'''
Exercício 3: Adicionar Prefixo
Crie uma função adicionar_prefixo(prefixo) que retorne uma função interna.
A função interna deve receber uma string e retornar a string com o prefixo adicionado.
'''
# def adicionar_prefixo(prefixo):
#     def texto(string):
#         return f'{prefixo}{string}'
#     return texto

# adicionar_prefixo_Sr = adicionar_prefixo('Sr.')

# print(adicionar_prefixo_Sr('Jonathan'))
# print(adicionar_prefixo_Sr('thiago'))
# print(adicionar_prefixo_Sr('thalles'))

'''
Exercício 4: Filtro de Valores Mínimos
Crie uma função filtro_valores_minimos(minimo) que retorne uma função interna. 
Essa função interna deve ser usada para filtrar valores de uma lista que sejam maiores ou iguais ao valor minimo.
'''
# def filtro_valores_minimos(minimo):
#     def filtro(lista):
#         return list(filter(lambda x: x >= minimo, lista))
#     return filtro

# filtro_valores_minimos_cinco = filtro_valores_minimos(10)

# print(filtro_valores_minimos_cinco([5, 10, 15, 20, 3, 12]))

'''
Exercício 5: Gerador de Saudação Personalizada
Crie uma função gerar_saudacao(saudacao) que retorne uma função interna.
A função interna deve receber um nome e retornar uma saudação personalizada com a saudacao fornecida.
'''
def gerar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}{nome}'
    return saudar

saudacao_bom_dia = gerar_saudacao('BOM DIA!!! Sr.(Sra) ')

print(saudacao_bom_dia('Jonathan Alonso Marques!!!'))