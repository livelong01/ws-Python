# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores sao "Syntax Sugar" (Açucar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('I will docorate you')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Your result was {resultado}')
        print('ok now you have been decorated')
        return resultado
    return interna
#A FUNCAO ACIMA, É A FUNCAO DECORADORA!

'''
O símbolo @criar_funcao é um açúcar sintático do Python, 
usado para decorar a função inverte_string sem precisar fazer isso manualmente.
O que acontece por trás dos panos é que 
""inverte_string = criar_funcao(inverte_string)"" é chamado automaticamente. 
Ou seja, a função interna se torna a nova versão de inverte_string.
Isso significa que, quando inverte_string é chamada, na verdade, 
é a função interna (definida dentro de criar_funcao) que está sendo executada.
'''

@criar_funcao  # o PYTHON deixa vc usar a "interna" do criar funcao sem precisar renomear nada. Ele usa já faz tudo pra vc.
def inverte_string(string):
    print(f'{inverte_string.__name__}') # eu pergunto o nome da funcao invert string e ele diz que é "interna". Se referindo a funcao interna de criar_funcao.
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param must be a string")




invertida = inverte_string('123')
print(invertida)

'''
The Decorated function take a existent function and add, remove , restrict and alter it.
Decorar uma função é como adicionar "camadas extras" de funcionalidades, sem mexer na receita principal.

Exemplo de uso:

Reaproveitamento de Código:
Suponha que você precise adicionar um recurso, como autenticação, 
a várias funções. Em vez de escrever esse processo em cada uma das 
funções manualmente, você cria um decorador que faz a autenticação 
e simplesmente "decora" todas as funções que precisam desse comportamento.
Isso reduz a repetição e torna o código mais organizado.

Facilidade de Manutenção:
Se você precisar mudar alguma coisa que está na parte decorada 
— por exemplo, mudar a maneira como os dados são registrados —, 
você faz isso apenas no decorador, e todas as funções que o usam 
são atualizadas automaticamente.

'''