# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# C:\\temp\\ws-Python\\treino
# caminho = r'C:\\temp\\ws-Python\\treino'
import os
caminho = os.path.join('\\temp', 'ws-Python', 'treino')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(caminho_completo_pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(imagem)
