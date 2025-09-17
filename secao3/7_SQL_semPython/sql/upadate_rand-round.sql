-- Cria um salario aleatorio para os usuarios  rand funcao "random" e ", 2", serve para duas casas decimais.
update Users set salary = ROUND(rand() * 10000, 2)

select salary from Users where salary between 1000 and 1500
order by salary asc;

-- Atualiza o salario dos usuarios com um valor aleatorio entre 0 e 10000, arredondado para duas casas decimais.
-- A função rand() gera um número aleatório entre 0 e 1, que é multiplicado por 10000 para obter um valor entre 0 e 10000.
-- A função ROUND é usada para arredondar o valor para duas casas decimais. 
-- A consulta final seleciona os salários atualizados que estão entre 1000 e 1500, ordenados em ordem crescente.