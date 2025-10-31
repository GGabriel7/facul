import sqlite3 as conector 

conexao = conector.connect("./db.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
    id INTEGER NOT NULL,
    cpf TEXT NOT NULL,
    nome TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    oculos BOOLEAN NOT NULL,
    PRIMARY KEY (id)
        );''')

cursor.execute('''INSERT INTO Pessoa (id, cpf, nome, data_nascimento, oculos)
VALUES (1, '12345678901', 'João da Silva', '1990-01-01', 1);''')

conexao.commit()

cursor.close()
conexao.close()