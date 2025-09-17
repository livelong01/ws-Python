SELECT u.first_name,
MAX(u.salary) as max_salary,
MIN(u.salary) as min_salary,
AVG(u.salary) as avg_salary,
SUM(u.salary) as sum_salary,
COUNT(u.id) as total 
from Users u 
left join profiles as p
on p.user_id = u.id 
-- WHERE u.id IN (118, 117, 116)
GROUP BY first_name 
ORDER BY total DESC 

# o que aconteceu aqui?
# 1. Agrupamos os usuários pelo primeiro nome
# 2. Calculamos o salário máximo, mínimo, médio, soma e a contagem de usuários para cada grupo
# 3. Ordenamos os resultados pela contagem de usuários em ordem decrescente
# 4. Note que usamos LEFT JOIN para garantir que todos os usuários sejam incluídos, mesmo aqueles sem perfil
# 5. Comentamos a cláusula WHERE para incluir todos os usuários no cálculo
-- LIMIT 10