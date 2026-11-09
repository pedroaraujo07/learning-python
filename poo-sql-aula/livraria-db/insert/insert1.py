import sqlite3

conexao = sqlite3.connect('livraria.db')

cur = conexao.cursor()

sql = ''' INSERT INTO tb_cliente
          (cpf, nome,  idade)
          VALUES('123', 'Alice', 21) '''

cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")