from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone (Eletronico, LogFileMixin): #HERANLÇA MULTIPLCA, N RECOMENDADO
    def ligar(self):
        super().ligar()

        if self._ligado: #PREFIRA COMPOSICAO AO INVES DE HERANÇA!!!
            msg = f'{self._nome} esta ligado.'
            self.log_sucess(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado: #PREFIRA COMPOSICAO AO INVES DE HERANÇA!!!
            msg = f'{self._nome} esta desligado.'
            self.log_error(msg)


    
