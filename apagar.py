import sqlite3
from DB_Sqlite3_Constants import DB_FILE, TABLE_NAME

def apagar():
    print('apagar')
    print('=================================')
    print('Delete')
    print('=================================')
    connection : sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor : sqlite3.Cursor = connection.cursor()

    delete : str = f'DELETE FROM {TABLE_NAME} WHERE WEIGHT>=100'
    cursor.execute(delete)
    connection.commit()
    cursor.close()
    connection.close()