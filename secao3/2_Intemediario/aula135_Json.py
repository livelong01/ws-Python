#O que é json? video do youtube.
'''
O json é um compactador de dados, ele transforma os dados, parecido com o dicionario
do python e assim ele pode ser enviado para outros locais, mantendo a integridade
e compatibilidade entre sistemas, linguagens, etc.

JSON (JavaScript Object Notation) 
é um formato simples e leve para armazenar e
transmitir dados. Ele é muito usado em aplicações 
web para troca de informações entre o navegador e o servidor.
'''
import json
pessoa = {
    'nome': 'Luiz Otávio ',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)
    # json.dump(pessoa, arquivo, ensure_ascii=False)#ensure_ascii muda a linguagem e corrige os acentos etc. (NAO RECOMENDADO, POR CAUSA DE COMPATIBILIDADE)


with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome']) #eu estou chamando o arquivo json, pelo load. (que ta chamando o json)


    #OBS: ELE CONVERTE TUPLA EM LISTA SEMPRE.