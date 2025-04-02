import requests
from bs4 import BeautifulSoup

# URL do G1
url = 'https://g1.globo.com/'

# Fazer a requisição HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    raw_html = response.text  # HTML cru
    parsed_html = BeautifulSoup(raw_html, 'html.parser')  # Parse do HTML

    # Teste: imprimir o título da página para ver se foi carregado corretamente
    print("Título da página:", parsed_html.title.text)

    # Tentar encontrar todas as manchetes principais
    # Nova classe para manchetes
    headlines = parsed_html.select('.feed-post-link')

    # Se encontrou manchetes, exibir os títulos
    if headlines:
        # Pega as 5 primeiras manchetes
        for idx, headline in enumerate(headlines[:8]):
            print(f"{idx+1}. {headline.text.strip()} - {headline['href']}")
    else:
        print("Nenhuma manchete encontrada. O layout pode ter mudado.")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
