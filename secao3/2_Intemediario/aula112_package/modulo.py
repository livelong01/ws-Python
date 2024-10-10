__all__ = [
    'variavel', 'soma',
]

variavel = 'Alguma coisa'
'''
Usando o __all__ vc escolhe o q a variavel
vai distrubir, qd alguem importar o all, ou seja,
quando a pessoa fizer import xxx* com asteristico
vc pode escolher o q for importar, mt util!
'''


def soma ( x, y ):
    return x + y

# from modulo_b import fala_oi

# fala_oi()

#para funcionar o import acima no MAIN, deve-se
# fazer o seguinte:

# from aula112_package.modulo_b import fala_oi

# fala_oi()