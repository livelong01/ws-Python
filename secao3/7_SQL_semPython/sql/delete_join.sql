
-- Apaga registros com join.
select u.first_name, p.bio from users u
-- delete p, u from users u
left join profiles as p
on p.user_id = u.id
where u.first_name = 'Tanner'

# o que aconteceu aqui?
# 1 - selecionamos as colunas first_name da tabela users e bio da tabela profiles   
# 2 - fizemos um join entre as tabelas users e profiles, usando a coluna user_id da tabela profiles e a coluna id da tabela users
# 3 - apagamos os registros das tabelas users e profiles
# 4 - filtramos os registros onde o first_name da tabela users é igual a 'Tanner'
# 5 - o resultado é que os registros das tabelas users e profiles foram apagados