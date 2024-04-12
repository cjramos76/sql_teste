import sqlite3

from typing import Dict
from inserir import inserir
from consultar import consultar
from apagar import apagar





def main():

    print('=================================')
    print('Main SQLite3')
    print('=================================')

    consultar()
    inserir()
    consultar()
    apagar()
    consultar()


if (__name__ == '__main__'):
    main()