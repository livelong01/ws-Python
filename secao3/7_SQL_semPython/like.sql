select * from Users -- Usar like (valor parecido com o q vc quer).
--where first_name like '%a' -- qualquer coisa (%) que termina com a.
--where first_name like 'a%' --qualquer coisa (%) que começa com a.
--where first_name like 'Ha%' -- pode ser mais de uma letra.
-- where first_name like 'H%h' -- começa com h e termina com h.
--where first_name like '%mo%' -- no meio da palavra tenha "mo"
--where first_name like '%a%b%' -- procura essas letras na palavra
--where first_name like 'j_cob' --procura uma palavra q possua j_cob, no caso era jacob, ou jocob, jicob etc.
where first_name like '_____' -- como usei 5 _ ele vai encontrar apenas nomes com 5 letras.