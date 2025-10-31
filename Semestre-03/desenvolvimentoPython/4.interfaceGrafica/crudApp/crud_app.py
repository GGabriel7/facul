import psycopg2
from psycopg2 import Error

def connectDB():
    try:
        connection = psycopg2.connect(
            user="your_username",
            password="your_password",
            host="localhost",
            database="portgrasDB"
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL", e)
        return None
    
def create_contact(nome, telefone):
    conn = connectDB()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO public."AGENDA" (nome, telefone)
                VALUES (%s, %s) RETURNING id;
            """, (nome, telefone))
            
            contact_id = cursor.fetchone()[0] # Pega o ID do contato inserido
            conn.commit()
            print(f"Contato criado com ID: {contact_id}")
            
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
                SELECT id, nome, telefone FROM public."AGENDA";)
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
                UPDATE public."AGENDA"
                SET nome = %s, telefone = %s
                WHERE id = %s;
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
                DELETE FROM public."AGENDA"
                WHERE id = %s;
            """, (contact_id,))
            
            conn.commit()
            print(f"Contato com ID {contact_id} deletado.")
        
        except Error as e:
            print("Erro ao deletar contato:", e)
            
        finally:
            cursor.close()
            conn.close()
            
def main():
    while True:
        print("\nMenu de CRUD de Contatos")
        print("1. Criar Contato")
        print("2. Ler Contatos")
        print("3. Atualizar Contato")
        print("4. Deletar Contato")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        match choice:
            case '1':
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                create_contact(nome, telefone)
            case '2':
                read_contacts()
            case '3':
                contact_id = int(input("Digite o ID do contato a ser atualizado: "))
                novo_nome = input("Digite o novo nome: ")
                novo_telefone = input("Digite o novo telefone: ")
                update_contact(contact_id, novo_nome, novo_telefone)
            case '4':
                contact_id = int(input("Digite o ID do contato a ser deletado: "))
                delete_contact(contact_id)
            case '5':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()