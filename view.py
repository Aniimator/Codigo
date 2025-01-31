import sqlite3 as lite
from datetime import datetime

#inserir conexão
con = lite.connect('dados.db')

# Inserir no inventario
def inserir_form(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO inventario (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)

def deletar_form(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM inventario WHERE id = ?"
        cursor.execute(query, i)

def atualizar_form(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE inventario SET nome = ?, local = ?, descricao = ?, marca = ?, data_da_compra = ?, valor_da_compra = ?, serie = ?, imagem = ? WHERE id = ?"
        cursor.execute(query, i)

def ver_form():
    lista_itens = []
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM inventario")
        rows = cursor.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens

def ver_iten(id):
    lista_itens = []
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id = ?", (id))
        rows = cursor.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens
