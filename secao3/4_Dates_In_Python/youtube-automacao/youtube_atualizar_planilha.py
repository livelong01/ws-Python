# https://www.youtube.com/watch?v=4kPRm8D8Vx0
# 4 Automações com Python que Vão SALVAR Seu Tempo no Trabalho

# 3 - atualizar planilha:
import openpyxl
import os


def atualizar_planilha():
    caminho_arquivo = r"C:\temp\ws-Python\secao3\4_Dates_In_Python\youtube-automacao\dados.xlsx"
    print("Tentando abrir:", caminho_arquivo)

    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado 😤")
        return

    workbook = openpyxl.load_workbook(caminho_arquivo)
    aba = workbook.active
    aba.append(["Thiago", 40, "Pedreiro"])
    workbook.save(caminho_arquivo)

    print("Planilha atualizada!")


atualizar_planilha()
