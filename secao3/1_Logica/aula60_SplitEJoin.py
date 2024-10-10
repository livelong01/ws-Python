"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '    Olha só que,     coisa interessante        '

lista_frases_cruas = frase.split(', ') #quebra na virgula(virgula n aparece).
print((lista_frases_cruas))

'''
Acima dividimos a string em duas partes em uma lista
com dois conteudos. Assim, jogando no for, ele printa os
dois conteudos da frase.
'''
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #.strip: tira os espaços do começo e fim do trecho cortado.
#tmb pode usar o rstrip (tira espaços da direita(right) e lstrip (left) esquerda.)
print(lista_frases)

#JOIN: 

frases_unidas = ', '.join(lista_frases) #n aceita numeros
print(frases_unidas)
'''
O JOIN une iteraveis, seja string, listas e tuplas. 
nesse caso, usei o ', ' (virgula e espaço) para unir as duas
frases separadas na string.
O processo foi: 
Antes tinha uma frase cheia de espaços desnecessarios, 
depois criou uma nova variavel e separou a string em duas partes
usando o espaço e virgula.
depois a corrigiu usando strip e o for, onde retirou os espaços
Por fim, reuniu as frases usando o join, com o ', '.
Agora a frase esta bem diagramada.
'''

