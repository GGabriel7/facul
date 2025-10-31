import sqlite3

conexao = sqlite3.connect('APP/banco_de_dados.db')

print("Conexão bem sucedida!")

cursor = conexao.cursor()

if __name__ == "__main__":
    # Criação da tabela "usuarios"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTOS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco NUMERIC(10, 2) NOT NULL
        );
    ''')
    
    conexao.commit()
    print("Tabela 'PRODUTOS' criada com sucesso!")
    cursor.close()
    conexao.close()