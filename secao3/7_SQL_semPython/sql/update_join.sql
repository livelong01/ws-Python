
select u.first_name, p.bio from users u
-- update users as u 
join profiles as p
on p.user_id = u.id
-- set p.bio = CONCAT(p.bio, ' Atualizado')
where u.first_name = 'Katelyn'

# o que aconteceu aqui?
# 1 - selecionamos as colunas first_name da tabela users e bio da tabela profiles
# 2 - fizemos um join entre as tabelas users e profiles, usando a coluna user_id da tabela profiles e a coluna id da tabela users
# 3 - atualizamos a coluna bio da tabela profiles, concatenando o valor atual com a string ' Atualizado'
# 4 - filtramos os registros onde o first_name da tabela users é igual a 'Katelyn'
# 5 - o resultado é que a coluna bio da tabela profiles foi atualizada para todos os usuários com first_name 'Katelyn'