import requests
from pprint import pprint
from get_token import token

_print = print

print = pprint

url = 'http://127.0.0.1:3001/alunos/3'

headers = {
    'Authorization': token
}

aluno_data = {  # nesse caso, vc pode alterar apenas o dado que vc quer (no caso, nome e sobrenome. PUT-.)
    "nome": "Luna",
    "sobrenome": "Alonso",
    # "email": "Jorge@email.com",
    # "idade": "50",
    # "peso": "80.04",
    # "altura": "1.90"
}

response = requests.put(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    response_data = response.json()
    print(response_data)
    # token = response_data['token']
    # with open('token.txt', 'w') as file:
    #     file.write(token)
else:
    # erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
