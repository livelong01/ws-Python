# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)  # Cria a aplicação

botao = QPushButton("Clique aqui!")  # Cria um botão com o texto "Clique aqui!"
# Define o estilo do botão
botao.setStyleSheet("font-size: 50px; background-color: red; color: white;")
botao.show()  # Mostra o botão na tela

# botao2 = QPushButton("texto do botao")
# botao2.show()

app.exec()  # Executa a aplicação




