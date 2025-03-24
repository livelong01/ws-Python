# pasta 32 site.
# python -m http.server -d .\secao3\4_Dates_In_Python\aula32_site\ 3333
# pip install requests types-requests

import requests
# http:// ->roda na porta 80
# https:// ->roda na porta 443

# precisa informar a porta no fim, pq por padrao ele vai para a port a80 (por conta do http)
url = 'http://localhost:3333/'
url2 = 'https://www.ahnegao.com.br/'
response = requests.get(url2)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
