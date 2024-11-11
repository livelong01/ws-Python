#Funcoes decoradoras e decoradores com classes.

# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__ #Para capturar o nome da classe.
#         class_dict = self.__dict__ #para criar um dicionario.
#         class_repr = f'{class_name}({class_dict})' #montou o dicionario.
#         return class_repr     

# class SuperTime:
#     ...

# class Time(SuperTime, MyReprMixin): #As duas tem o repr herdado e podem usar apenas com 1 codigo.
#     def __init__(self, nome):
#         self.nome = nome 
    
#     # def __repr__(self): #TIREI DAQUI E PUS NA CLASSE PROPRIA PARA "REPR"
#     #     class_name = self.__class__.__name__ #Para capturar o nome da classe.
#     #     class_dict = self.__dict__ #para criar um dicionario.
#     #     class_repr = f'{class_name}({class_dict})' #montou o dicionario.
#     #     return class_repr #o que sera mostrado ao tentar visualizar a funcao.

# class Planeta(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
    # def __repr__(self):
    #     class_name = self.__class__.__name__ #Para capturar o nome da classe.
    #     class_dict = self.__dict__ #para criar um dicionario.
    #     class_repr = f'{class_name}({class_dict})' #montou o dicionario.
    #     return class_repr 

# brasil = Time('Brasil')
# portugal =Time('Portugal')


# terra = Planeta('Terra')
# marte = Planeta('Marte')

# print(brasil)
# print(portugal)
# print(terra)
# print(marte)

##################### USANDO COMPOSICAO (NAO HERANÇA) ################

def adicionar_repr(cls):  #CLS é usado para representar que a funcao recebe uma CLASSE.
        def meu_repr(self):
            class_name = self.__class__.__name__ 
            class_dict = self.__dict__ 
            class_repr = f'{class_name}({class_dict})' 
            return class_repr 
        cls.__repr__ = meu_repr 
        return cls

''' COMO ISSO FUNCIONA_: 
1) a funcao recebe uma classe, por ex: "Terra"
2) a funcao implmenta tudo como se tivesse dentro da classe... por isso tem self, setc.
3) no fim ele chama cls.__repr__, que é exatamente como se ele tivesse definindo
o repr da classe, que no caso seria: Terra.__repr__ = a funcao que faz toda a representacao
do repr.
4) no final ele retorna a classe com o repr adicionado. (que aconteceu em cls.__repr = meu_repr)
'''
@adicionar_repr #decorador da funcao, que adc "repr" a ela! mais
class Time: 
    def __init__(self, nome):
        self.nome = nome 
    
@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    

# Time = adicionar_repr(Time) #Essa linha adc o repr na classe, tem q posicionar isso sempre no inicio, ANTES de criar o OBJETO.
brasil = Time('Brasil')
portugal =Time('Portugal')

# Planeta = adicionar_repr(Planeta) #isso nao fica muito bonito, sobrescrever a classe, por isso se usa o DECORADOR acima DA CLASSE.
terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugal)
print(terra)
print(marte)