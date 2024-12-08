# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(
        default='Missing', repr=False  # some do repr
    )
    sobrenome: str = 'Not sent'
    idade: int = 100  # so pode por valor padrao com valores imutaveis.
    enderecos: list[str] = field(default_factory=list)  # lista n funciona, 
    # pq o valor é mutavel!
    # A lista só funciona com valor padrao, se usar o FIELD do dataclass.


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))  # mostra todas as config dos campos (até as padroes)
    print(p1)
