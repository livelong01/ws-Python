-- insert select 
-- insere valores em uma tabela usando outra tabela


insert into profiles (bio, description, user_id) -- concat serve para concatenar valores, texto etc.
select concat('Bio de ' , first_name) , concat( 'Description de ' ,first_name) , id from Users;  -- no lugar da bio, vai ser sempre bio, e igual no description (fixo) e no user_id, sera o id do usuario.



--delete from profiles 
