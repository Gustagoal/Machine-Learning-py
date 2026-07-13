import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gucastro1",
    database="banco"   # nome do banco
)

print("Conectado com sucesso!")

cursor = conexao.cursor()

cursor.execute("Select * from locais")

resultado = cursor.fetchall()

for locais in resultado:
    print(locais[1])