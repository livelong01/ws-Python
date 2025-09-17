insert into users_roles (user_id, role_id)
VALUES
(119, 4)

SELECT user_id, role_id from users_roles WHERE 
user_id = 119 and role_id = 4;

-- SELECT
-- id,
-- (SELECT id from roles order by rand() limit 1) as qualquer FROM users;

insert into users_roles (user_id , role_id)
select id,
(SELECT id from roles order by rand() limit 1) as qualquer FROM users;

-- Insere um novo registro na tabela users_roles associando o usuário com id 119 ao papel com id 4.
-- A consulta final seleciona o user_id e role_id da tabela users_roles para verificar a inserção.
-- A segunda parte do código insere um novo registro na tabela users_roles para cada usuário,   
-- associando-o a um papel aleatório selecionado da tabela roles.