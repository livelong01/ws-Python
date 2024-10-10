# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} #tem q por set na frente, senao cria dicionario!!!
# s1 = set('Luiz')

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# # print(s1) #{1, 2, 3} ele elimina iteraveis duplicados!!! sem fazer nada.
# s1 = set(l1) #CONVERTE lista em SET , para retirar dupplicados!
# l2 = list(s1) #volta a converter para lista.
# print(l2) #[1, 2, 3]
# s1 = set('Jonathan') # sets nao garantem ordem e apagam duplicados de string 
# print(s1) # {'a', 'o', 'h', 't', 'n', 'J'} //{'t', 'n', 'a', 'h', 'J', 'o'}
s1 = {1 , 2, 3, (1,23,3,)} # tupla é unico q ele aceita, lista, dic, etc q sao mutaveis n pode!
# print(s1[1]) #TypeError: 'set' object is not subscriptable
print(s1)

for i in s1:
    print(i)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos