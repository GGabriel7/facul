import sqlite3
from faker import Faker
from cria_tabela import conexao, cursor

class AppBD:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect_to_db()
        
    def connect_to_db(self):
        self.conn = conexao
        self.cur = cursor
        print("Conexão com o banco de dados estabelecida.")
        
    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM PRODUTOS")
            registros = self.cur.fetchall() # Recupera todos os registros da consulta
            return registros
        except Exception as e:
            print(f"Erro ao selecionar dados: {e}")
            return [] # Retorna uma lista vazia em caso de erro
    
    def inserir_dados(self, nome, preco):
        try:
            self.cur.execute("INSERT INTO PRODUTOS (nome, preco) VALUES (?, ?)", (nome, preco))
            self.conn.commit()
            print("Dados inseridos com sucesso!")
        
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
            
    def atualizar_dados(self, id, nome, preco):
        try:
            self.cur.execute("UPDATE PRODUTOS SET nome = ?, preco = ? WHERE id = ?", (nome, preco, id))
            self.conn.commit()
            print("Dados atualizados com sucesso!")
        
        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")
            
    def deletar_dados(self, id):
        try:
            self.cur.execute("DELETE FROM PRODUTOS WHERE id = ?", (id,))
            self.conn.commit()
            print("Dados deletados com sucesso!")
        
        except Exception as e:
            print(f"Erro ao deletar dados: {e}")
            

if __name__ == "__main__":
    app_db = AppBD()
    fake = Faker()
    
    for _ in range(10):
        nome = fake.word().capitalize()
        preco = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2)
        app_db.inserir_dados(nome, preco)