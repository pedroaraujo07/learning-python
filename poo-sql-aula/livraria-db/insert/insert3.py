import sqlite3

conexao = sqlite3.connect('livraria.db')

cur = conexao.cursor()

sql = ''' INSERT INTO tb_cliente
          (cpf, nome)
          VALUES('125', 'João') '''

cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")