select id, first_name, email as uemail
from Users
where id BETWEEN 50 AND 100
order by id asc;

-- primeiro vc seleciona as colunas que quer ver. (select)
-- de onde vc ta pegando essas colunas (from Users)
-- (where) para vc selecionar quais dados vc quer por ex id 1 ate 50
-- por fim, ordena em asc (crescente) por id, 1,2,3,4... e assim por diante. IPC: desc(decrescente) outra ordenacao.