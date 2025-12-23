"""
 Link da documentação > https://docs.python.org/3/library/sqlite3.html#tutorial
"""
import sqlite3
con = sqlite3.connect("teste.db")
# print('Teste realizado')
cursor = con.cursor()


# cursor.execute("CREATE TABLE pais(continente,capital,população)")
cursor.execute("SELECT * FROM pais")
print(cursor.fetchall())