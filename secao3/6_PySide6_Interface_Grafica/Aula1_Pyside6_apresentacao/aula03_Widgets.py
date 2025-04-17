# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)  # Cria a aplicação

botao = QPushButton("Botao 1")  # Cria um botão com o texto "Clique aqui!"
# Define o estilo do botão
botao.setStyleSheet("font-size: 50px; background-color: red; color: white;")

botao2 = QPushButton("Botao 2")  # Cria um botão com o texto "Clique aqui!"
# Define o estilo do botão
botao2.setStyleSheet("font-size: 50px; background-color: blue; color: white;")

botao3 = QPushButton("Botao 3")  # Cria um botão com o texto "Clique aqui!"
# Define o estilo do botão
botao3.setStyleSheet("font-size: 50px; background-color: green; color: white;")

central_widget = QWidget()  # Cria um widget central

# layout = QVBoxLayout()  # Cria um layout vertical
# layout = QHBoxLayout()  # Cria um layout Horizontal
layout = QGridLayout()  # Cria um layout Horizontal

central_widget.setLayout(layout)  # Define o layout do widget central

layout.addWidget(botao, 1, 1, 1, 1)  # Adiciona o botão ao layout
layout.addWidget(botao2, 2, 2, 1, 1)  # Adiciona o botão ao layout
# Adiciona o botão ao layout com span de 2 colunas
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()  # Mostra o widget central na tela

app.exec()  # Executa a aplicação
