import sqlite3

conexao = sqlite3.connect('livraria.db')

cur = conexao.cursor()

sql = ''' INSERT INTO tb_cliente
          (cpf)
          VALUES('126') '''

cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")