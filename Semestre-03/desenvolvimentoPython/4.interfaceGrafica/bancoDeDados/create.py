import psycopg2 # Biblioteca para conectar ao PostgreSQL

conn = psycopg2.connect(
    host="localhost", # Endereço do servidor de banco de dados. Pode ser um IP ou 'localhost' para o servidor local
    database="postgresDB",
    user="admin",
    password="admin123"
)  # Conexao com o banco de dados PostgreSQL

cursor = conn.cursor()

# Criacao da tabela AGENDA
cursor.execute('''
    CREATE TABLE IF NOT EXISTS public."AGENDA" 
    (
        id integer PRIMARY KEY,
        nome text COLLATE pg_catalog."default" NOT NULL,
        telefone char(12) COLLATE pg_catalog."default" NOT NULL
    )
    
    TABLESPACE pg_default;
    ALTER TABLE public."AGENDA"
        OWNER to postgres;
''')

# Inserindo dados na tabela AGENDA
cursor.execute('''
    INSERT INTO public."AGENDA" (id, nome, telefone) VALUES
    (1, 'Joao Silva', '12345678901')
''')

cursor.execute('''
    INSERT INTO public."AGENDA" (id, nome, telefone) VALUES
    (2, 'Maria Oliveira', '10987654321')
''')

conn.commit()

# ler os dados da tabela AGENDA
cursor.execute('SELECT * FROM public."AGENDA"')

rows = cursor.fetchall()

for row in rows:
    print(f"id: {row[0]}, nome: {row[1]}, telefone: {row[2]}")  

cursor.close()
conn.close()