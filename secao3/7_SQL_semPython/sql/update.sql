-- Update Atualiza registros


update Users u set first_name = 'Joninho', last_name = ' Marques'
where id BETWEEN 25 AND 28

-- select * from Users u where id = 100
select * from Users where id BETWEEN 25 AND 28;