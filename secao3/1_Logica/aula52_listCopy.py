"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'luiz'
# noutra_variavel = nome # guarda o nome em outra, n some.
# nome = 'joao'
# print(nome, noutra_variavel) 

lista_a = ['Luiz', 'Maria', 1, 3.1]
lista_b = lista_a # n subst., apenas apontam p/ msm ID.
print(lista_b)
#Mutavel!
lista_a[0] = 'Qualquer coisa'
print(lista_a)# tanto lista a 
print(lista_b)# qt lista b, foram alterados ( msm ID )

'''
para voce copiar a lista de forma a serem IGUAIS
e apontarem para coisas diferentes, voce precisa 
usar o metodo COPY!
'''
lista_b = lista_a.copy() #n vaI SER afetada
lista_a[0] = 'cavaloo' 

print(lista_a)#['cavaloo', 'Maria', 1, 3.1]
print(lista_b)#['Qualquer coisa', 'Maria', 1, 3.1]