

insert ignore into users_roles (user_id , role_id)
select id,
(SELECT id from roles order by rand() limit 1) as qualquer FROM users
ORDER BY rand() limit 5;

-- Insere registros na tabela users_roles, associando usuários a papéis aleatórios.
-- A subconsulta (SELECT id from roles order by rand() limit 1) seleciona um papel aleatório para cada usuário.
-- A cláusula ORDER BY rand() na consulta principal garante que a seleção de usuários também seja aleatória.
-- O limite de 5 registros é aplicado para inserir apenas 5 associações aleatórias. 
-- """A cláusula INSERT IGNORE evita erros caso a associação já exista, ignorando duplicatas.""""