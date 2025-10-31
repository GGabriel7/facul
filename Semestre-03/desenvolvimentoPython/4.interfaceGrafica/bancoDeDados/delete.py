import psycopg2 # Biblioteca para conectar ao PostgreSQL

conn = psycopg2.connect(
    host="localhost", # Endereço do servidor de banco de dados. Pode ser um IP ou 'localhost' para o servidor local
    database="postgresDB",
    user="admin",
    password="admin123"
)  # Conexao com o banco de dados PostgreSQL

cursor = conn.cursor()

cursor.execute('''
    DELETE FROM public."AGENDA" WHERE id = 1
''')

conn.commit()

# Ler os dados atualizados
cursor.execute('SELECT * FROM public."AGENDA"')
rows = cursor.fetchall()
for row in rows:
    print(f"id: {row[0]}, nome: {row[1]}, telefone: {row[2]}")
    
cursor.close()
conn.close()