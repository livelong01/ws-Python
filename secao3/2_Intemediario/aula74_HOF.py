"""
Higher Order Functions
Funções de primeira classe
"""
def saudacao (msg, nome):
    return f' {msg}, {nome}!'

def executa (funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao ## sao a msm funcao na memeroria com nomes diferentes.

v = executa(saudacao, 'Bom dia', 'Jonathan')
print(v)
