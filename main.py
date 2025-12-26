"""
 Link da documentação > https://docs.python.org/3/library/sqlite3.html#tutorial
"""
import sqlite3
con = sqlite3.connect("teste.db")
# print('Teste realizado')
cursor = con.cursor()


# cursor.execute("CREATE TABLE pais(continente,capital,população)")
cursor.execute("""
    INSERT INTO pais VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

cursor.execute("SELECT * FROM pais")