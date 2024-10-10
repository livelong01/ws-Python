# VARIAVEIS livres + nonlocal (local, globals)
# print(globals())
# def fora(x):
#     a = x #variaVEL livre, qd ela n esta DEFINIDA no escopo mais interno
#     def dentro():
#         print(locals())
#         # print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar=''):
        nonlocal valor_final #nonlocal permite vc alterar a variavel que antes era livre.
        valor_final += valor_a_concatenar #variavel valor final n é desse escopo, só pode LER. NÃO pode alterar ela.
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)