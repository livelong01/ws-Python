select u.id as uid, p.id as pid,
p.bio, u.first_name
FROM Users as u 
LEFT JOIN profiles p 
ON u.id = p.user_id;

-- LEFT JOIN retorna todos os registros da tabela da esquerda (Users) e os registros correspondentes da tabela da direita (profiles).
-- Se não houver correspondência, os campos da tabela da direita serão preenchidos com NULL. (no exemplo apareceu null no campo apagado)