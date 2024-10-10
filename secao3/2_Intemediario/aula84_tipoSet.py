# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} #tem q por set na frente, senao cria dicionario!!!
# s1 = set('Luiz')
s1 = set()
s1 = set('Luiz')  # vazio ##{'z', 'i', 'u', 'L'} <class 'set'> 77 MELHOR passar listas e tuplas ou coisas iteraveis.
# s1 = {'Luiz', 1, 2, 3}  # com dados
s1 = {'Luiz', 1,2,3} #se passar com chaves, ele fica corretamente, sem separar por letras.
print(s1, type(s1))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos