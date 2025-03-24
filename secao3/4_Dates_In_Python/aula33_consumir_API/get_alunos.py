import requests
from pprint import pprint
from get_token import token

_print = print

print = pprint

url = 'http://127.0.0.1:3001/alunos/'

headers = {
    # 'Authorization': token
}

aluno_data = {
    # "nome": "Jorge",
    # "sobrenome": "Alonso",
    # "email": "Jorge@email.com",
    # "idade": "50",
    # "peso": "80.04",
    # "altura": "1.90"
}

response = requests.get(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    response_data = response.json()
    for aluno in response_data:
        print(aluno)
        print('---------------------')
        # print(aluno['nome'])
else:
    # erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
