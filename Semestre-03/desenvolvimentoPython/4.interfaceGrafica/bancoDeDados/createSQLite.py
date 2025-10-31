import sqlite3 # Biblioteca para conectar ao SQLite

# Cria (ou abre) o banco no mesmo diretório
conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

# Cria a tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS AGENDA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone CHAR(12) NOT NULL
)
''')

# Inserindo os dados na tabela AGENDA
cursor.execute('INSERT INTO AGENDA (nome, telefone) VALUES ("Joao Silva", "12345678901")')
cursor.execute('INSERT INTO AGENDA (nome, telefone) VALUES ("Maria Oliveira", "10987654321")')

conn.commit()

# Lê e mostra os dados
cursor.execute('SELECT * FROM AGENDA')

rows = cursor.fetchall()

for row in rows:
    print(f"id: {row[0]}, nome: {row[1]}, telefone: {row[2]}")

# Fecha a conexão
cursor.close()
conn.close()