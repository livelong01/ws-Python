# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = set() # ele recebe e itera todos os valores.

s1.add(1)# só 1 de cada vez!
s1.add('Luiz')# só 1 de cada vez!
# s1.add(1,2) # TypeError: set.add() takes exactly one argument (2 given)
s1.update(('Olá mundo', 1, 2, 3, 4)) #no update é igual ao set(), ele itera, entao vc manda ele dentro de uma tupla, q faz com q as letras n se separem.
#{1, 2, 3, 'Luiz', 4, 'Olá mundo'} #PODE MANDAR VARIOS VALORES.
# s1.clear() #set() limpa tudo!
s1.discard('Olá mundo') # vc envia o valor e ele é eliminado do conjunsto #{1, 2, 'Luiz', 3, 4}
s1.discard('Luiz') # vc envia o valor e ele é eliminado do conjunsto #{1, 2, 'Luiz', 3, 4}
print(s1) #{1, 2, 3, 4}

