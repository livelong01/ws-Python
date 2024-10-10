#condicionais: 
numeros = [1,2,3,4,5,6,7,8,9,10]
novos_numeros = [numero for numero in numeros if numero > 5] #fazer o if pela direita
impares =[numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
#outro tipo de if
outro_if = [numero   #o q vai formar a nova lista 
            if numero != 6 else 600 # if que precisa de else vem antes do for.
            for numero in numeros  #for que itera a lista pre-existe
            if numero % 2 == 0] # if que filtra apenas os pares.

# outra forma de fazer é substituindo o pela list compreension ja existente pares.
outro_if_novo = [numero 
                 if numero !=6 else 600 #operador ternario, precisa do ELSE
                 for numero in pares]


print(numeros) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(novos_numeros) #[6, 7, 8, 9, 10]
print(impares)  #[1, 3, 5, 7, 9]
print(pares)  #[2, 4, 6, 8, 10]
print(outro_if) #[2, 4, 600, 8, 10] IGUAL   
print(outro_if_novo) #[2, 4, 600, 8, 10] IGUAL  
