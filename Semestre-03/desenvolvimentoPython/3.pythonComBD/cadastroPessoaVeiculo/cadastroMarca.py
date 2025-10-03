import sqlite3 as conector

conexao = conector.connect("./db1.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE Marca(
    id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    sigla CHARACTER(2) NOT NULL,
    PRIMARY KEY (id)
        );''')

conexao.commit()


cursor.cose()
conexao.close() 