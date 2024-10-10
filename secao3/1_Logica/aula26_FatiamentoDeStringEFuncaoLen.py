"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] i=inicio f= fim p=passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[4:8]) 
print(variavel[4:])
'''
No caso acima, eu pos [4:7] usando inicio e fim
porem ele nao inclui o 7, capturando apenas: "mun" ao inves
de "mund", por isso mudei para "4:8".
Nota: Se voce quiser capturar de onde marcou ate o fim
por ex: mundo. Voce pode por "[4:]" o python entende
que vc quer do digito 4 (incluindo o "m") ate o final do str
'''
print(variavel[0:5]) 
print(variavel[:5]) 
print(variavel[-8:-2])
print(len(variavel[0:5])) # len conta a qtd de caracters selecionados 
# bom para descobrir se vc contou um espaço vazio, por ex. len(variavel[3]), resp: 1
print(variavel[-8:-2])
print(len(variavel)) # checar qts de caract da str
print(variavel[0:len(variavel):1]) 
''' IMPORTANTE!!!
O len pode ser usado para dizer o tamanho da str e 
com isso vc pode por ela para capturar sempre o tamanho
total da str. Metodo muito usado!
O "p" passo, diz a frequencia, por ex: 1
ele vai analisar e capturar de 1 em 1 . 
se fosse 2, seria de 2 em 2. Exemplo abaixo: Reslt: "Oámno"
'''
print(variavel[0:len(variavel):2])

print(variavel[::-1]) #inverter a str toda! Se quiser inverter apenas uma parte.
print(variavel[-1:-5:-1]) #tem q usar em todas as partes o indice "negativo"!


