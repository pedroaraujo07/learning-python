import sqlite3

conexao = sqlite3.connect('livraria.db')

cur = conexao.cursor()

sql = ''' UPDATE tb_cliente
          SET NOME = "Carla"
          WHERE CPF = 123 '''

cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")