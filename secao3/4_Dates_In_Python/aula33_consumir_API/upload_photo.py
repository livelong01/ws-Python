import requests
from pprint import pprint
from get_token import token
from mimetypes import MimeTypes
from requests_toolbelt import MultipartEncoder


_print = print
print = pprint

mimetypes = MimeTypes()

url = 'http://127.0.0.1:3001/fotos'


nome_arquivo = 'aluno.jpg'
mimetypes_arquivo = mimetypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetypes_arquivo)
})

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url,  headers=headers, data=multipart)

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
