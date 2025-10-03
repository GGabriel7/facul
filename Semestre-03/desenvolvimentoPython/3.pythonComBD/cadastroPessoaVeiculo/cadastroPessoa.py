import sqlite3 as conector 

try:
    conexao = conector.connect("./db1.db")
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE Pessoa(
        cpf INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf)
            );''')
    
    conexao.commit()
    
except conector.DatabaseError as err:
    print("Erro de banco de dados", err)
    
finally:
    if conexao:
        cursor.cose()
        conexao.close() 