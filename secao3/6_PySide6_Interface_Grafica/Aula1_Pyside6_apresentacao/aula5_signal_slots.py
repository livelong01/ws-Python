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
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')
layout = QGridLayout()

botao1 = QPushButton("Botão 1") #oi
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
@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O slot foi executado')
    return inner

#exemplo 2 de acao
@Slot()
def outro_slot(checked):
    print('Está marcado? ', checked)


#exemplo 2 de acao
@Slot()
def terceiro_slot(segunda_acao):
    def inner():
        outro_slot(segunda_acao.isChecked())
    return inner

#MenuBar:
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira acao!')
primeira_acao.triggered.connect(
    slot_example(status_bar)
)

#MenuBar2 : 
segunda_acao = primeiro_menu.addAction('Segunda acao!')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot) # termina em "ed" para nos conectar
segunda_acao.hovered.connect(terceiro_slot(segunda_acao)) # termina em "ed" para nos conectar

botao1.clicked.connect(terceiro_slot(segunda_acao))

window.show()  # Mostra o widget central na tela

app.exec()