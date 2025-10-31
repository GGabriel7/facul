import sqlite3 as conector

conexao = conector.connect("./db1.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS veiculo(
    placa  CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    PRIMARY KEY (placa)
    FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf).
    FOREIGN KEY (marca) REFERENCES Marca(id).
        );''')

cursor.execute('''ALTER TABLE Veiculo
                    ADD motor REAL;
               ''') # adiciona algo após a criação

# Ou poderia apagar a tabela inteira para recriar, caso precise de uma rodem certa. Só adicionar vai colocar ela no final

cursor.execute('''DROP TABLE Veiculo;
               ''')

cursor.execute('''CREATE TABLE veiculo(
    placa  CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    motor REAL NOT NULL,
    PRIMARY KEY (placa)
    FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf).
    FOREIGN KEY (marca) REFERENCES Marca(id).
        );''')

conexao.commit()


cursor.cose()
conexao.close()