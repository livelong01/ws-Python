import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = 1'
)
connection.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
)
connection.commit()


for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)


if __name__ == '__main__':
    cursor.close()
    connection.close()
