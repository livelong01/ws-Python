# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


@dataclass  # (frozen=True)Congela a classe, n deixa criar atrib. e
class Pessoa:  # metodos.
    nome: str  # repr=False, desativa o representante de texto da classe.
    sobrenome: str

    # def __init__(self, nome, sobrenome):  # executado apos o init,
    #     # tytoda vez q se cria um construtor('pessoa')
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('POst Init')  # n sera executado mais..., pq defini 
    # o meu proprio init manualmente. (so qd foi automatico)

    # @property
    # def nome_completo(self):
    # return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    p1 = Pessoa('Luiz', 'Otávio')
    p2 = Pessoa('Luiz', 'Otávio')
    # p1.nome = 'Jonathan'  # Graças ao frozen, n consigo alterar um atributo,
    print(p2)
    # ordenadas = sorted(lista, reverse=True)  # só funciona com o (order=True)
    # print(ordenadas)

    # para usar a ordenacao sem o order=true basta, usar funcao lambda
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)  # volta a funcionar
