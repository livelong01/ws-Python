#Classes decoradoras (Decorator Classes)

from typing import Any


class Multiplicar:
    def __init__(self, func) :
        self.func = func
        self._multiplicador = 10
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        resultado = self.func(*args, **kwargs)

        return resultado * self._multiplicador


@Multiplicar #decorador com letra maiuscula, uma classe q esta decorando.
def soma (x,y):
    return x + y


dois_mais_dois = soma(2, 4)
print(dois_mais_dois)


class Multiplicar:
    def __init__(self, multiplicador) :
        self._multiplicador = multiplicador
    
    def __call__(self, func) -> Any:
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador

        return interna # sem ativar


@Multiplicar(5) #agora vc vai ter q repassar direatamente o Multiplicador da funcao adiada.
def soma (x,y):
    return x + y


dois_mais_dois = soma(2, 4)
print(dois_mais_dois)