import sqlite3 as conector

conexao = conector.connect("./db1.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE veiculo(
    placa  CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    PRIMARY KEY (placa)
    FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf).
    FOREIGN KEY (marca) REFERENCES Marca(id).
        );''')

conexao.commit()
cursor.cose()
conexao.close()