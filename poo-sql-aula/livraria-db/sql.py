import sqlite3
database = 'livraria.db'
conexao = sqlite3.connect(database)
cur = conexao.cursor()

sql = '''CREATE TABLE tb_cliente(
         cpf TEXT PRIMARY KEY,
         nome TEXT NOT NULL,
         idade INTEGER NULL)'''

cur.execute(sql)
cur.close()
conexao.close()
print("Fechou a base de dados")