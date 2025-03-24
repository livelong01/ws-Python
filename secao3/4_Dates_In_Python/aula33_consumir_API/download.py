import requests

url = 'http://localhost:3001/images/1742839173871_12125.jpg'
nome_arquivo = url.split('/')[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    # sucesso
    print(response.status_code)
    print(response.reason)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)
else:
    # erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
