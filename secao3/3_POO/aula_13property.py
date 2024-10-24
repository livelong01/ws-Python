# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

'''
RESUMO: 
Nas outras linguagens, como no java, existia protected, privated, public. 
E voce escolhia o q podia ser mexido e o que ficava protegido. Dando acesso
limitado para as pessoas atraves do get. Que deixava a pessoa chamar, mas n editar.
Fora que quando vc fizesse uma modificacao no codigo principal, n precisaria mexer no
codigo do cliente, pois n quebrava o codigo. 

No python, se usa o property, que transforma o atributo do objeto em getter.
assim basta chamar o atributo q ele sera usado normalmente.
A vantagem é que se eu editar algo no atributo, só precisarei corrigir no @property
e ele vai funcionar no codigo cliente. Age de forma semelhante as protecoes do java.
mudou no init, basta mudar no @property e o programa funciona perfeitamente 👍 

'''
class Caneta:
    def __init__(self, cor):
        #privated, protected public
        self.cor_tinta = cor
    @property
    def cor(self):
        print('Property')
        return self.cor_tinta  
    @property
    def cor_tampa(self):
        return 12345  
#######################################

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
print(caneta.cor)

#######################################
# class Caneta:
#     def __init__(self, cor):
#         #privated, protected public
#         self.cor = cor
#     def get_cor(self):
#         print('get cor')
#         return self.cor
# #######################################

# caneta = Caneta('Azul')
# print(caneta.getcor())