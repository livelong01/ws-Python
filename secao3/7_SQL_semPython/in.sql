-- seleciona uma lista de elementos entre os valores que voce quiser.
select * from Users 
where id in (100, 105, 108) 
and first_name in ('Len', 'Hilda');