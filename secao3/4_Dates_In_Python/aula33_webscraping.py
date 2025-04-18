# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
url2 = 'https://g1.globo.com/'
response = requests.get(url)
raw_html = response.text  # html cru.
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

# if parsed_html is not None:
#     print(parsed_html.title.text)

# vai no site que vc quer, seleciona o que quer pegar e dps em inspecionar e por fim copy selector.

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# print(top_jobs_heading)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    if article is not None:
        # print(article.text)
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text))
