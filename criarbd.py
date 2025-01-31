import sqlite3 as lite
from datetime import datetime
con = lite.connect('dados.db')

with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
