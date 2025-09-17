select u.id as uid, p.id as pid,
p.bio, u.first_name
FROM Users as u, profiles as p
where u.id = p.user_id;

-- delete from profiles where id between 260 and 262

-- seleciona os users que tem profile, que estao relacionados atraves da condicao "ON" u.id = p.user_id
select u.id as uid, p.id as pid,
p.bio, u.first_name
FROM Users as u 
INNER JOIN profiles p 
ON u.id = p.user_id
WHERE U.first_name  LIKE '%a'
ORDER BY u.first_name DESC
LIMIT 5;

-- agora no fim, ele selciona users que tem profile, que estao relacionados atraves da condicao "ON" u.id = p.user_id
-- e que o nome do usuario termina com a letra 'a'
-- e ordena pelo nome do usuario em ordem decrescente, limitando a 5 resultados
-- e seleciona os campos u.id, p.id, p.bio e u.first_name