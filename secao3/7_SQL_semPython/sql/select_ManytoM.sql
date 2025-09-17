-- 
SELECT u.id as uid, u.first_name, p.bio , r.name AS role_name
FROM Users u
LEFT JOIN profiles as p ON u.id = p.user_id
INNER JOIN users_roles ur  ON u.id = ur.user_id 
INNER JOIN roles as r ON ur.role_id = r.id 
where u.id = 119
ORDER BY uid ASC
limit 0, 1
;

-- O LEFT JOIN indica que você quer manter todos os registros da tabela da esquerda (neste caso, Users), mesmo que não exista um correspondente na tabela profiles. 
-- A junção está sendo feita com base no u.id = p.user_id, ou seja, o campo user_id da tabela profiles deve bater com o id da tabela Users.
-- Resultado:
-- Vai retornar todos os usuários existentes na tabela Users, mesmo se não houver um perfil correspondente na tabela profiles.
-- Quando não houver correspondência, os campos pid e bio virão como NULL.  
-- No fim, o resultado será ordenado pelo uid (id do usuário) em ordem ascendente e limitado a 1 registro.
-- retirando a restricao do where e o limit, o resultado será todos os usuários com seus respectivos perfis e roles.