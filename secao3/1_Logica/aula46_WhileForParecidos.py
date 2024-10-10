for i in range(10): # 0 - 9 
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3): # 1 - 2 (o ultimo n n é incluido)
        print(i, j)
else:
    print('For completo com sucesso!')