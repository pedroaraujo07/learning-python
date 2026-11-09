import sqlite3

conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()

v_cpf = input("CPF: ")
v_nome = input("Nome: ")
v_idade = input("Idade: ")

sql = " INSERT INTO tb_cliente (cpf, nome, idade) values (?, ?, ?) "

cur.execute(sql, (v_cpf, v_nome, v_idade))
conexao.commit()
cur.close()
conexao.close()

print("Fechou a base de dados")