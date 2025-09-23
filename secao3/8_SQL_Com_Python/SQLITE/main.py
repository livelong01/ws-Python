import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


# CUIDADO: fazendo delete sem where deleta todos os registros (n a tabela)
# cursor.execute(f'DELETE FROM {TABLE_NAME}')
# connection.commit()

# apagar tabela de vez!
# cursor.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
# connection.commit()

# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# connection.commit()

# criar tabela
# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'name TEXT,'
#     'weight REAL'
#     ')'
# )
# connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection por comandos maliciosos na variavel vinda do usuario
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name , weight) '
    'VALUES '
    '( ?, ?)'
)
cursor.execute(sql, ["Joao Nogueira", 78.6])
connection.commit()

# cursor.executemany('', '')

cursor.close()
connection.close()
