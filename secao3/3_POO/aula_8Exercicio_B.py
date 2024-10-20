# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
from aula_8Exercicio_A import CAMINHO_ARQUIVO, Pessoa , salvar

import json
# salvar() #executar o dump do outro modulo
# salvar()
with open(CAMINHO_ARQUIVO, 'r+',  encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

# for pessoa in pessoas:
#     print(vars(Pessoa(**pessoa)))

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(vars(p1))
print(vars(p2))
print(vars(p3))



#VERSAO DO PROFESSOR: 

