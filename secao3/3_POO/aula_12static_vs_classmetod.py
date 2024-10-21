# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection: 
    
    def __init__(self, host = 'localhost'): #metodo de instnacia
        self.host = host
        self.user = None
        self.password = None
    #PRECISO DE SELF DENTRO DA INSTNACIA? ENTAO VAI SER METODO DE INSTANCIA
    def set_user(self, user): #metodo de instancia, se chama o SELF
        #setter
        self.user = user

    def set_password(self, password): #chamou self, metodo de instnacia.
        self.password = password #usa self embaixo!
    
    @classmethod
    def create_with_auth(cls, user, password): #CLASS METHOD
        connection = cls() # é como se ele fizesse: connection = connection()
        connection.user = user #AGORA ELE pode chamar e modificar o user, e senha
        connection.password = password #uma factiorie que cria usuarios.
        return connection 

    @staticmethod #funcao organizacional, mudar nome, mandar msg, deixar legivel algo.
    def log(msg):
        print('LOG: ', msg)


c1 = Connection.create_with_auth('luiz', '1234')
# print(Connection.soma(2,3))
print(Connection.log('Essa é a msg de log.'))
# c1.set_user('Jonathan')
# c1.set_password('123')
print(c1.user)
print(c1.password)
    