# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

CAMINHO_ARQUIVO = 'aula8.json'
p1 = Pessoa('Jonathan', 35)
p2 = Pessoa('Tatiane', 29)
p3 = Pessoa('Luna', 0)

pessoas = [vars(p1), p2.__dict__, vars(p3)]

def salvar(): #pus dentro da funcao, para adiar sua execucao (pq senao ela sempre executa e isso gasta mt memoria.)
    print('FAZENDO DUMP')
    with open(CAMINHO_ARQUIVO, 'w',  encoding='utf8') as arquivo:
        json.dump(pessoas, arquivo, ensure_ascii= False, indent= 2)

# salvar()

if __name__ == '__main__':
    print('Ele é o __main__')
    salvar()

    '''
    isso nao sera executado qd for importado por outro modulo
    porque esse moduloA n sera o __main__. Mas ainda posso executar essa funcao 
    lá no moduloB, ja que ele vai ser o main. Salvar() sera executado la sem problemas, 
    porque ele será o main.
    '''