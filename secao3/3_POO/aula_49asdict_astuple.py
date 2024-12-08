# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    p1 = Pessoa('Luiz', 'Otávio')
    p2 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())  # vai ver como um dicionario o print.
    print(asdict(p1).values())  # vai ver como um dicionario o print.
    print(asdict(p1).items())  # vai ver como um dicionario o print.
    print(astuple(p1)[0])  # vai ver como um dicionario o print.
    print(p1)
    print(p2)
