import sqlite3

conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()

sql = "SELECT * FROM tb_cliente "

cur.execute(sql)

l_registros = cur.fetchall()

for registro in l_registros:
    print(registro)

cur.close()
conexao.close()
print("Fechou a base de dados")