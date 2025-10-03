# Principais conectadores de banco de dados:

import sqlite3  # Conector para SQLite
# Incluíudo nas blbliotecas padrões do Pyton
# Leve e rápido para aplicações pequenas
- Ideal para pequenos desenvolvimentos e testes

import mysql.connector  # Conector para MySQL
# Fácil de instalar e configurar
# Suporte oficial e contínio da Oracle.
- Usar em aplicações que exigem suporte contínuo e escalabilidade

import psycopg2  # Conector para PostgreSQL
# Suporte completo às funcções do PostgreSQL
# Excelente desempenho
# Suporte transações e segurança
- Usar em projetos com grandes volumes de dados e transaões complexas.

Principais Métodos:
    - connect - Estabelece a conexão com o banco: connection = connect(parameters)
    
    - execute - Executa comando SQL no banco de dados: cursor.execute("comandos SQL")
    
    - commit - Salva as transções realizadas: connection.commit()
    
    Exemplo de função: 
        import sqlite3 as conector
        # import mysql.connector as conector
        # import psycopg2 as conector
        
        conexao = conector.connect("URL SQLite")
        
        cursor = conexao.cursor()
        
        cursor.execute("...")
        cursor.fetchall()
        
        conexao.comit()
        
        cursor.close()
        conexao.close()
     
     
Tipos de dados mais comuns: 
    Integer (int): numeros interior
    Text (string): Textos
    Real (float ou double): numeros com ponto flutante (,)
    Blob: binarios: fotos, PDF ou qualquer dado em formato binario
    NULL: Valores nulos
    