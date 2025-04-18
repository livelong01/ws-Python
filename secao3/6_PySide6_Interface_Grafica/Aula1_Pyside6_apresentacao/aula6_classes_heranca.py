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



class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        #Botao1
        self.botao1 = self.make_button('botao 1', "background-color: red; color: white; font-size: 20px;")
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = self.make_button("Botão 2", "background-color: green; color: white; font-size: 20px;")

        self.botao3 = self.make_button("Botão 3", "background-color: blue; color: white; font-size: 20px;")

        # StatusBar!
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Mostrar mensagem")

        # MenuBar:
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira acao!')
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_statusbar)

        # MenuBar2 :
        self.segunda_acao = self.primeiro_menu.addAction('Segunda acao!')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)  
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout) 

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)  
        self.grid_layout.addWidget(self.botao2, 2, 2, 1, 1)  
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

    @Slot()
    def muda_mensagem_da_statusbar(self):
        self.status_bar.showMessage('O slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado? ', self.segunda_acao.isChecked())
    
    def make_button(self, text, style):
        btn = QPushButton(text)  # oi
        btn.setStyleSheet(style) 
        return btn

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()  # Mostra o widget central na tela
    app.exec()
