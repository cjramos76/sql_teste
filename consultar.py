import sqlite3
from DB_Sqlite3_Constants import DB_FILE, TABLE_NAME

def consultar():
     connection : sqlite3.Connection = sqlite3.connect(DB_FILE)
     cursor : sqlite3.Cursor = connection.cursor()
     print('select')

     # Query buscando todos os customers
     select : str = f'select * from {TABLE_NAME}'
     cursor.execute(select)

     print('=================================')
     print('Busca um customer fetchone')
     print('=================================')
     customer = cursor.fetchone()
     ident, name, weight = customer
     print(ident, name, weight)

     print('=================================')
     print('Busca um customer fetchall')
     print('=================================')
     for row in cursor.fetchall():
          _id, nome, peso = row
          print(_id, nome, peso)

     print('=================================')
     print('Busca um customer fechone fetch by id')
     print('=================================')
     cursor.execute(f'select id, name, weight from {TABLE_NAME} where id=7')
     customer7 = cursor.fetchone()
     print(f'customer7: {customer7}')

     print('=================================')
     print('Busca um customer fetchall fetch with where')
     print('=================================')
     cursor.execute(f'select * from {TABLE_NAME} where weight>=100')
     customers = cursor.fetchall()
     for customer in customers:
          print(customer)


     cursor.close()
     connection.close()