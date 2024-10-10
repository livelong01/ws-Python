# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #UNIAO
s4 = s1 & s2 #INTERSECAO (O Q TEM NOS DOIS)
s5 = s1 - s2 #DIFERENÇA EM RELACAO A S1!
s6 = s2 - s1 #DIFERENÇA EM RELACAO A S2!
s7 = s1 ^ s2 #DIFERENÇA SIMETRICA ( O Q SÓ TEM EM CADA 1)

print(s3) #{1, 2, 3, 4}
print(s4) #{2, 3}
print(s5) # {1}
print(s6) # {4}
print(s7) # {1, 4}
