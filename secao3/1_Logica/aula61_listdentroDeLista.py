''''
Lista de listas e seus indices
'''

salas = [
    #0         1
['Maria', 'Helena', ], # 0
#   0
['Elaine'], # 1
#  0         1        2
['Luiz' , 'João', 'Eduarda', ] #2 #(0, 10 , 20, 30 , 40)
] 

# print(salas[1][0]) #assim ele acessa o #1 (segunda lista) e [0] o primeiro valor da lista, no caso, elaine!
# print(salas[0][1]) #Helena
# print(salas[2][2]) #Eduarda
# print(salas[2][3][2]) #20

for sala in salas:
    print(sala) # esse vai olhar para lista inteira
    for aluno in sala:
        print(aluno) # esse for olha para "cada" aluno

print(*salas, sep='\n') 
'''RESULTADO: 
['Maria', 'Helena']
['Elaine']
['Luiz', 'João', 'Eduarda']
'''