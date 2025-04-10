# https://www.youtube.com/watch?v=4kPRm8D8Vx0
# 4 Automações com Python que Vão SALVAR Seu Tempo no Trabalho

# 4 - Web scrapping

from bs4 import BeautifulSoup
import requests


def extrair_informacoes_site():
    url = 'https://www.nationalgeographic.com/pages/topic/latest-stories'
    headers = {"User-Agent": "Mozilla/5.0"}
    requisicao = requests.get(url, headers=headers)

    if requisicao.status_code == 200:
        pagina = BeautifulSoup(requisicao.text, "html.parser")
        titulos = pagina.find_all(class_="sr-only")
        links = pagina.select(".PromoTile__Link")
        for titulo, link in zip(titulos, links):
            print(f'Titulo: {titulo.text}, link: {link['href']}')
            print()


extrair_informacoes_site()
