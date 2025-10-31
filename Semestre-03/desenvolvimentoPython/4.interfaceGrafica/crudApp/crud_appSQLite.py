import sqlite3
from sqlite3 import Error

def connectDB():
    try:
        connection = sqlite3.connect('agenda.db')
        return connection
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def create_table():
    conn = connectDB()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS AGENDA (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL
                );
            """)
            conn.commit()
            print("Tabela AGENDA criada ou já existe.")
        except Error as e:
            print("Erro ao criar tabela:", e)
        finally:
            cursor.close()
            conn.close()

def create_contact(nome, telefone):
    conn = connectDB()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO AGENDA (nome, telefone)
                VALUES (?, ?);
            """, (nome, telefone))
            
            conn.commit()
            print(f"Contato {nome} adicionado com sucesso.")
        
        except Error as e:
            print("Erro ao criar contato:", e)
        
        finally:
            cursor.close()
            conn.close()

def read_contacts():
    conn = connectDB()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT id, nome, telefone FROM AGENDA;
            """)
            
            contacts = cursor.fetchall()
            
            for contact in contacts:
                print(f"ID: {contact[0]}, Nome: {contact[1]}, Telefone: {contact[2]}")
        
        except Error as e:
            print("Erro ao ler contatos:", e)
        
        finally:
            cursor.close()
            conn.close()
            
def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connectDB()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE AGENDA
                SET nome = ?, telefone = ?
                WHERE id = ?;
            """, (novo_nome, novo_telefone, contact_id))
            
            conn.commit()
            print(f"Contato com ID {contact_id} atualizado.")
        
        except Error as e:
            print("Erro ao atualizar contato:", e)
        
        finally:
            cursor.close()
            conn.close()
            
def delete_contact(contact_id):
    conn = connectDB()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                DELETE FROM AGENDA
                WHERE id = ?;
            """, (contact_id,))
            
            conn.commit()
            print(f"Contato com ID {contact_id} deletado.")
        
        except Error as e:
            print("Erro ao deletar contato:", e)
        
        finally:
            cursor.close()
            conn.close()

def main():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Criar contato")
        print("2. Ler contatos")
        print("3. Atualizar contato")
        print("4. Deletar contato")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            create_contact(nome, telefone)
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            contact_id = int(input("Digite o ID do contato a ser atualizado: "))
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            update_contact(contact_id, novo_nome, novo_telefone)
        elif choice == '4':
            contact_id = int(input("Digite o ID do contato a ser deletado: "))
            delete_contact(contact_id)
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()