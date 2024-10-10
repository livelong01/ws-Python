#LINHAS E COLUNAS:

for x in range(1, 11):
    for y in range(1, 6):
        print(x,y) #for aninhado ( x (coluna), y (linha))

#----------------------
linha_e_coluna =[
    (x, y) 
    if y != 2 else (x , y * 1000) # operador ternario
    for x in range(1,11)
    for y in range(1,6)
    if x !=2 #filtro!
]

print(linha_e_coluna)