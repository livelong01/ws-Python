# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None: # O None e o
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ... #bool (bolean) nesse caso, sao dicas de prog para prog, para ajudar a entender o que resultado as funcoes. (N FAZEM NADA)

# n = Notificacao('Testando notificacao') #n funciona! pQ É ABSTRATA  

class NotificacaoEmail(Notificacao):
    def enviar(self)-> bool:  #Princípio da substituição de liskov
        print('E-mail: Enviando: - ', self.mensagem)
        return True #Princípio da substituição de liskov

class NotificacaoSMS(Notificacao):
    def enviar(self)-> bool:  #Princípio da substituição de liskov
        print('SMS: Enviando: - ', self.mensagem)
        return False #Princípio da substituição de liskov

# ne = NotificacaoEmail('testando notificacao.')
# ne.enviar()

# ns = NotificacaoSMS('testando notificacao.')
# ns.enviar()

# def notificar(notificacao:str):  #agora o python só vai aceitar STR. E abaixo se vc por um ponto em notificacao, ele chama todas as funcoes str.... 
#     notificacao

def notificar(notificacao:Notificacao): #POLIMORFISMO NO OBJETO notificacao:Notificacao, pois ele aceita TODAS as classes FILHAS E ELA PROPRIA.
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada: # for verdadeira
        print('Notificacao enviada.')
    else:
        print('Notificacao não enviada.')

notificacao_email = NotificacaoEmail('testando email.')
notificar(notificacao_email) #Aqui esta o polimorfismo! PRESTE ATENCAO AQUI.

notificacao_sms = NotificacaoSMS('testando SMS.')
notificar(notificacao_sms) #Aqui esta o polimorfismo! PRESTE ATENCAO AQUI.
