from conectar import meu_cursor, conexao

meu_cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco NUMERIC(10, 2) NOT NULL
    );
''')

conexao.commit()
print("Tabela criada com sucesso!")
conexao.close()