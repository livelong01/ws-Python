#STRING E LIST COMPREHENSION

nomes = ['luiz', 'jonathan', 'tatiane', 'joana', 'rosania', 'thalles']

novos_MAIUSCULAS = [nome.upper() for nome in nomes]
novos_MINUSCULAS = [nome.lower() for nome in nomes]
novos_primeira_maiuscula = [nome.title() for nome in nomes]
novos_ultima_maiuscula = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]

print(novos_primeira_maiuscula) #['Luiz', 'Jonathan', 'Tatiane', 'Joana', 'Rosania', 'Thalles']
print(novos_ultima_maiuscula) #