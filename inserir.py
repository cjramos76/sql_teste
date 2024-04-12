import sqlite3
from DB_Sqlite3_Constants import DB_FILE, TABLE_NAME

def inserir():
    print('inserir')
    connection : sqlite3.Connection = sqlite3.connect(DB_FILE)
    cursor : sqlite3.Cursor = connection.cursor()

    # sql:str = '''insert into customers (name, weight) values (?, ?)'''
    # cursor.executemany(sql, (("Juan", 65), ("Jorge", 90), ("Rafa", 93), ("Santi", 77)))
    my_customer:list[dict] = [{
        "nome": "Felipe",
        "peso": 105
    },{
        "nome": "Anderson",
        "peso": 123
    },{
        "nome": "Andre",
        "peso": 144
    }]

    sqlDict:str = '''insert into customers (name, weight) values (:nome, :peso)'''
    cursor.executemany(sqlDict, my_customer)

    connection.commit()
    cursor.close()
    connection.close()