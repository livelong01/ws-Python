-- comentario.
-- outro comentário
/* outro tipo de comentario*/
use base_de_dados;
-- ver os dados em tabela
show tables;

--descricao das colunas. 
describe Users;

-- inserir registros na base de dados
--insert into Users (first_name, last_name, email, password_hash) values 
--("Jorge", "Minda", "Jorge@gmail.com", "s_hash"),
--("Luiz", "Carvalho", "Carvalho@gmail.com", "3_hash"),
--("Thalles", "Marques", "thalles@gmail.com", "6_hash");

-- seleciona colunas: u = apelido da tabela.
--select * from Users u;
--select u.email as uemail, u.id uid, u.first_name ufirst_name from Users as u;

-- where filtra registros 
--operadores: = < <= > >= <> !=
--operadores logicos: and e or
select * from users
--where id=6;
--where first_name="Luiz"
--where id>=6;
--where id <> 5 --diferente
-- where id != 5
where created_at <= "2025-06-11 08:31:58" 
--and first_name = "tatiane" and password_hash = 5545; --PODE USAR or também