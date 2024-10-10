# numeros = [1,2,3,4,5]
# novos_numeros = numeros #referencia, aponta
# novos_numeros[0] = 20
# print(numeros) #[20, 2, 3, 4, 5]

# numeros = [1,2,3,4,5]
# novos_numeros = numeros.copy() #todos os valores copiados
# novos_numeros[0] = 20
# print(numeros) #[1, 2, 3, 4, 5]
# print(novos_numeros) #[20, 2, 3, 4, 5]

#USANDO LIST COMPREHENSION
# numeros = [1,2,3,4,5]
# novos_numeros = [numero for numero in numeros]
# mesma coisa que: 

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

#------------------------------
# def divisaoFn(x, y):
#     return x/y



# numeros = [1,2,3,4,5]
# divisao = [divisaoFn(numero, 2) #o q vai aparecer, usando funcao!
#            for numero in numeros]
# multiplicacao = [numero * 2
#            for numero in numeros]
# quadrado = [numero ** 2
#            for numero in numeros]

# print(numeros) #[1, 2, 3, 4, 5]
# print(divisao)  #[0.5, 1.0, 1.5, 2.0, 2.5] !!MAP!!
# print(multiplicacao)  #[2, 4, 6, 8, 10] !!MAP!!
# print(quadrado)  #[1, 4, 9, 16, 25] !!MAP!!


