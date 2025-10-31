import sqlite3 # Biblioteca para conectar ao sqlite

conn = sqlite3.connect('banco_de_dados.db')  # Conexao com o banco de dados SQLite

cursor = conn.cursor()

cursor.execute('''
    UPDATE AGENDA SET nome = 'Joao Pereira' WHERE id = 1
''')
conn.commit()

# Ler os dados atualizados
cursor.execute('SELECT * FROM AGENDA')
rows = cursor.fetchall()
for row in rows:
    print(f"id: {row[0]}, nome: {row[1]}, telefone: {row[2]}")

cursor.close()
conn.close()