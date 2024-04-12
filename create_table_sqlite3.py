import sqlite3
from DB_Sqlite3_Constants import DB_FILE, TABLE_NAME

def create_table():
    connection : sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor : sqlite3.Cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
        ')'
    )


    cursor.close()
    connection.close()