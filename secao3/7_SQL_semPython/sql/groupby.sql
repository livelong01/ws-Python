
-- saber quantos usuarios tem mesmo nome (valores repetidos)
SELECT first_name, COUNT(id) as total FROM Users u 
GROUP BY first_name
ORDER BY total DESC


SELECT u.first_name, COUNT(u.id) as total from Users u 
left join profiles as p
on p.user_id = u.id 
WHERE u.id IN (118, 117, 116)
GROUP BY first_name 
ORDER BY total DESC 
LIMIT 5;

## o que aconteceu aqui?
# 1 - selecionamos a coluna first_name da tabela users e contamos a quantidade de ids
# 2 - fizemos um join entre as tabelas users e profiles, usando a coluna user_id da tabela profiles e a coluna id da tabela users
# 3 - filtramos os registros onde o id da tabela users está na lista (118, 117, 116)
# 4 - agrupamos os resultados pelo first_name
# 5 - ordenamos os resultados pela contagem total em ordem decrescente
# 6 - limitamos o resultado a 5 registros
# 7 - o resultado é a contagem de usuários para cada nome, considerando apenas os usuários com id 118, 117 e 116
-- saber quantos usuarios tem mesmo nome (valores repetidos) e sobrenome
