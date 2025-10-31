import sqlite3 as conector
from modulo import Pessoa

conexao = conector.connect("bancoDeDados.db")
cursor = conexao.cursor()

# Tabela para armazenar dados de pessoas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pessoa (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    usa_oculos BOOLEAN NOT NULL
        );""")

pessoa1 = Pessoa("12345678900", "Gabriel", "2004-05-15", True)
pessoa2 = Pessoa("98765432100", "Ana", "1990-10-20", False)
pessoa3 = Pessoa("45678912300", "Carlos", "1985-03-30", True)
pessoa4 = Pessoa("78912345600", "Mariana", "2000-07-25", False)

#Inserindo dados na tabela Pessoa
cursor.execute("""
    INSERT INTO Pessoa (cpf, nome, data_nascimento, usa_oculos) VALUES (?, ?, ?, ?)
""", (pessoa1.cpf, pessoa1.nome, pessoa1.data_nascimento, pessoa1.usa_oculos))
cursor.execute("""
    INSERT INTO Pessoa (cpf, nome, data_nascimento, usa_oculos) VALUES (?, ?, ?, ?)
""", (pessoa2.cpf, pessoa2.nome, pessoa2.data_nascimento, pessoa2.usa_oculos))

# Utilizando nome como paraâmetro
cursor.execute("""
    INSERT INTO Pessoa (cpf, nome, data_nascimento, usa_oculos) VALUES (:cpf, :nome, :data_nascimento, :usa_oculos)
""", {"cpf": pessoa3.cpf, "nome": pessoa3.nome, "data_nascimento": pessoa3.data_nascimento, "usa_oculos": pessoa3.usa_oculos})
cursor.execute("""
    INSERT INTO Pessoa (cpf, nome, data_nascimento, usa_oculos) VALUES (:cpf, :nome, :data_nascimento, :usa_oculos)
""", {"cpf": pessoa4.cpf, "nome": pessoa4.nome, "data_nascimento": pessoa4.data_nascimento, "usa_oculos": pessoa4.usa_oculos})

# Tabela para armazenar dados de marcas de veículos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculo(
    placa  CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario TEXT NOT NULL,
    PRIMARY KEY (placa),
    FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf)
        );""")

# Inserindo dados na tabela Veículo utilizando executemany
listaVeiculos = [
    ("ABC1234", 2020, "Prata", "12345678900"),
    ("XYZ5678", 2018, "Vermelho", "98765432100"),
    ("JKL9999", 2022, "Preto", "78912345600")
]
cursor.executemany("""
    INSERT INTO veiculo (placa, ano, cor, proprietario) VALUES (?, ?, ?, ?)
""", listaVeiculos)

conexao.commit()

cursor.close()
conexao.close()