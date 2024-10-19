#Mantendo estados dentro da classe.
class Camera: 
    def __init__(self, nome, filmando= False ):
        self.nome = nome
        self.filmando =  filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        self.filmando = True
        print(f'{self.nome} está filmando...')
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto esta filmando')
            return        
        print(f'{self.nome} esta fotografando')

c2 = Camera('Canon')
c2 = Camera('Nikon')
c2.filmar()
c2.filmar()
print(c2.filmando)
print(c2.filmando)
c2.fotografar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()


'''
Isso significa que a classe guarda informacoes, alteracoes
que vc faz ao longo da execucao do codigo. Ou seja, no caso acima,
ela salvou a informacao de que a camera 1 estava filmando e por isso
qd se usa c1.filmando no final, recebemos TRUE como resposta.
'''