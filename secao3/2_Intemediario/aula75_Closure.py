'''
Closure e funcoes que retornam outras funcoes.
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom Noite')
print(falar_bom_dia('Jonathan'))
print(falar_boa_noite('Jonathan'))

nomes = ['tatiane', 'thiago', 'jonathan']

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

'''RESUMO:
Ele criou um closure para deixar dinamico apenas
o NOME, enquanto a saudacao que é sempre igual ficou
FIXA! 
Ou seja, a funcao esta sempre preparada para dar bom dia ou boa noite.
porem o nome da pessoa que vai receber vai sempre mudar.
o que ajuda a economizar memoria
CRLT + SHIFT + P, DIGITE: REMOVE ALL BREAKPOINTS  e ele remove todos o break.
'''