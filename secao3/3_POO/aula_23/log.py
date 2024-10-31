#abstracao
#log
'''
A classe log é abstrata, pois ela foi criada para nao ser usada´, por isso o error
para afastar as pessoas dela. Ela indica que vc tem que criar/usar a subclasse dela
no caso: LogFileMixin. 
O sufixo "mixin" deixa claro para outros desenvolvedores que essa classe pode ser
modificada e usada.
'''
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
#ele pega o caminho do arquivo de acordo com o modulo atual.


class Log: #CLASSE MAE
    def _log(self, msg): #assinatura do metodo, protegido, para ser usado so nessa classe e nas filhas.
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        self._log(f'Sucess: {msg}')

class LogFileMixin(Log): #classe filha
    def _log(self, msg): #assinatura do metodo # para sobrepor um metodo, deixe tudo igual.
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log): #CLASSE FILHA     #polimorfismo, qd o msm metodo é chamado, mas ele se comporta diferente dependendo do ambiente.
    def _log(self, msg): #assinatura do metodo # para sobrepor um metodo, deixe tudo igual.
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('Que legal')