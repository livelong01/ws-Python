# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')
layout = QGridLayout()

botao1 = QPushButton("Botão 1")
botao1.setStyleSheet("background-color: red; color: white; font-size: 80px;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("background-color: green; color: white; font-size: 20px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("background-color: blue; color: white; font-size: 20px;")

central_widget.setLayout(layout)  # Define o layout do widget central

layout.addWidget(botao1, 1, 1, 1, 1)  # Adiciona o botão ao layout
layout.addWidget(botao2, 2, 2, 1, 1)  # Adiciona o botão ao layout
# Adiciona o botão ao layout com span de 2 colunas
layout.addWidget(botao3, 3, 1, 1, 2)

#StatusBar!
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem")

#exemplo de acao
def slot_example(status_bar):
    status_bar.showMessage('O slot foi executado')

#MeuBar:
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira acao!')
primeira_acao.triggered.connect(
    lambda: slot_example(status_bar)
)




window.show()  # Mostra o widget central na tela

app.exec()