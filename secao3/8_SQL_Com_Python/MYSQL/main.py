# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = 'customers'
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        #  SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        #  CUIDADO ISSO LIMPA A TABELA E REINICIA OS DADOS.
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # COMEÇO A MANIPULAR DADOS A PARTIR DAQUI
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Jonathan', 34)
        result = cursor.execute(sql, data)

        # print('Numero de linhas afetadas: ', result)
    connection.commit()

# usando dicionario :
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data2 = {
            "nome": "Jorge",
            "idade": 29
        }
        result = cursor.execute(sql, data2)

        # print('Numero de linhas afetadas: ', result)
    connection.commit()
    
# Usando dicionario com multiplas entradas 

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data3 = (
            {"nome": "Carmem","idade": 45},
            {"nome": "Julia","idade": 85},
            {"nome": "Corvo","idade": 15},
            {"nome": "Julho","idade": 25},
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        print('Numero de linhas afetadas: ', result)
    connection.commit() 

# Usando tuplas com multiplas entradas 

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 35),
            ("Cortana", 58),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        print('Numero de linhas afetadas: ', result)
    connection.commit()

# LENDO VALORES COM SELECT

    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id para consulta: '))
        maior_id = int(input('Digite o maior id para consulta: '))
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (menor_id, maior_id))

        data5 = cursor.fetchall()  # A melhor pratica é por numa variavel
        # for row in data5:
        #     print(row)


        # for row in data5:
        #     print(row)

        # for row in cursor.fetchall():  # Ele esgota os dados e na proxima tentativa 
        #     print(row)
        # for row in cursor.fetchall():  # isso nao faz nada.
        #     print(row)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            f'WHERE ID = %s '  
        )

        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT  * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

    # Editando com Delete, where e placeholders no PYmYSQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            f'SET nome = %s, idade = %s '
            f'WHERE ID=%s '
        )

        cursor.execute(sql, ('Jaqueline', 15, 4))

        cursor.execute(f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1')
        lastIdFromSelect = cursor.fetchone()

        resultFromSelect = cursor.execute(f'SELECT  * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()
        for row in data6:
            print(row)
        

        
        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)  # rowcount funciona apos qualquer comando execute (sempre pega o ultimo)
        print('lastrowid', cursor.lastrowid)  # lastrowid funciona apenas apos inserts
        print('lastIdFromSelect na mão', lastIdFromSelect['id'])  # type: ignore
        cursor.scroll(-2)
        print('rownumber', cursor.rownumber)  # rownumber mostra a linha atual do cursor em selects

        connection.commit()

        


