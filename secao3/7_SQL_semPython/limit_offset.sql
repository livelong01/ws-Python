-- limit limita a quatd de valores
-- offset mostra quando de onde vamos começar, por exemplo limit 5 mostra os 5 primeiros valores
-- offset 10 mostra a partir do 10 valor encontrado, os proximos 5 (por causa do limit.)

select id, first_name, email as uemail
from Users
where id BETWEEN 50 AND 100
order by id asc
limit 5 offset 10;
-- pode ser escrito como: limit 10, 5 ( é a msm coisa que o de cima.)