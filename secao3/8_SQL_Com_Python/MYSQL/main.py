# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
import pymysql
import dotenv

TABLE_NAME = 'customers'
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
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
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)

        data5 = cursor.fetchall()  # A melhor pratica é por numa variavel
        for row in data5:
            print(row)
        for row in data5:
            print(row)

        # for row in cursor.fetchall():  # Ele esgota os dados e na proxima tentativa 
        #     print(row)
        # for row in cursor.fetchall():  # isso nao faz nada.
        #     print(row)

        


