# type: ignore
# from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# ROOT_FOLDER = Path(__file__).parent
# CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# chrome_options = webdriver.ChromeOptions()
# chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
# chrome_browser = webdriver.Chrome(
#     service=chrome_service,
#     options=chrome_options,
# )

# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)

# -----------------------*******************--------------------#
# Selenium - Automatizando tarefas no navegador
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# from pathlib import Path
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Caminho para a raiz do projeto
# ROOT_FOLDER = Path(__file__).parent
# # Caminho para a pasta onde o chromedriver está
# # ATENÇÃO: Adicione ".exe" se estiver no Windows
# CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


# def make_chrome_browser(*options: str) -> webdriver.Chrome:
#     chrome_options = webdriver.ChromeOptions()  # type

#     if options:
#         for option in options:
#             chrome_options.add_argument(option)

#     chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))

#     browser = webdriver.Chrome(
#         service=chrome_service,
#         options=chrome_options
#     )

#     return browser


# # AGORA FORA DA FUNÇÃO:
# if __name__ == '__main__':
#     TIME_TO_WAIT = 30
#     # exemplos de options: '--headless', '--disable-gpu'
#     options = ()

#     browser = make_chrome_browser(*options)

#     browser.get('https://www.google.com')

#     # Espere para encontrar o input
#     search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
#         EC.element_to_be_clickable((By.CLASS, 'QS5gu sy4vM')),
#         EC.element_to_be_clickable((By.NAME, 'q'))
#     )
#     '''
#     Esse codigo acima: Apos o navegador abrir aguarde, até (until) aparecer na tela o elemento com nome 'p'.
#     '''
#     search_input.send_keys('Hello World!')
#     search_input.send_keys(Keys.ENTER)

#     # Dorme por 10 segs
#     sleep(TIME_TO_WAIT)

# ----------------------chatgpt------------------#

from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random  # Para gerar atrasos aleatórios

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# Criar navegador com opções para evitar CAPTCHA


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # User-Agent personalizado (faz parecer um navegador comum)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    )

    # Evita que o Google detecte Selenium
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")

    # Usar um perfil de usuário real (permite salvar cookies e histórico)
    chrome_options.add_argument("--user-data-dir=C:\\temp\\selenium-profile")

    # Se estiver no Windows, pode precisar de `chrome_options.add_argument("--profile-directory=Default")`

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 1
    options = ()

    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com')

    browser.maximize_window()

    # 1️⃣ Aceitar os cookies, se existir o botão
    try:
        cookie_button = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.element_to_be_clickable((By.ID, 'L2AGLb'))
        )
        cookie_button.click()
        print("Cookies aceitos!")
    except Exception:
        print("Nenhum botão de cookies encontrado, continuando...")

    # 2️⃣ Esperar até o campo de pesquisa estar presente, visível e interativo
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )

        WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.visibility_of(search_input)
        )

        WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.element_to_be_clickable((By.NAME, 'q'))
        )

        # 3️⃣ Simular comportamento humano antes de digitar
        sleep(random.uniform(2, 5))  # Espera aleatória entre 2 e 5 segundos

        search_input.click()
        search_input.clear()

        for letter in "flamengo":
            search_input.send_keys(letter)
            sleep(random.uniform(0.1, 0.3))  # Simula digitação humana

        search_input.send_keys(Keys.ENTER)
        print("Pesquisa realizada!")

    except Exception as e:
        print(f"Erro ao interagir com a barra de pesquisa: {e}")

# Encontrar a seção de resultados
results = browser.find_element(By.ID, 'search')

# Encontrar os links dentro dos resultados
link = results.find_element(By.CLASS_NAME, 'zReHs')

sleep(5)
if link:
    link.click()
    print('Link clicado!')
else:
    print("Nenhum link encontrado!")

    # Dorme por alguns segundos para visualizar o resultado
sleep(10)
browser.quit()
