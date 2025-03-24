import requests
from pprint import pprint
_print = print
# print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "Jonathan",
    "password": "indio1993",
    "email": "jonathaki@mail.com"
}

response = requests.post(url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    print(response.json())
else:
    # erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
