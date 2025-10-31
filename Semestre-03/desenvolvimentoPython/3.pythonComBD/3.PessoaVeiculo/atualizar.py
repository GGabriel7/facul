import sqlite3 as conector

conexao = conector.connect('./bancoDeDados.db')
conexao.execute("PRAGMA foreign_keys = on") # Ativa o suporte a chaves estrangeiras.
cursor = conexao.cursor()

# cursor.execute("""UPDATE Pessoa SET oculos = 1""") - Fazer isso faz com que todos os registros sejam atualizados, evite isso.

cursor.execute("""UPDATE Pessoa SET usa_oculos=? WHERE cpf=?""", (1, "12345678900"))

# utilizando nome como parâmetro
cursor.execute("""UPDATE Pessoa SET usa_oculos=:usa_oculos WHERE cpf=:cpf""", {"usa_oculos": 1, "cpf": "98765432100"})

# Deletar registros. Usar WHERE para evitar deletar todos os registros
cursor.execute("""DELETE FROM Pessoa WHERE cpf=?""", ("45678912300",))

conexao.commit()

cursor.close()
conexao.close()