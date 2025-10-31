import sqlite3

conexao = sqlite3.connect('geraDados/banco_de_dados.db')

print("Conexão bem sucedida!")

meu_cursor = conexao.cursor()