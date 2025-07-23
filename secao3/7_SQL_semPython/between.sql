select * from Users 
where
--created_at >= '2020-06-12 17:38:52'
--and created_at <= '2020-09-04 19:06:55';
-- Outra forma de fazer isso mais rapido
--seleciona um range de dados (no caso datas.)
created_at between '2020-06-12 00:00:00' and '2020-09-04 23:59:59'
and 
id between 10 and 44;