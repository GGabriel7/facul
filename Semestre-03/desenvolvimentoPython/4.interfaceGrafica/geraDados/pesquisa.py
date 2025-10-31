from conectar import meu_cursor, conexao

meu_cursor.execute('''
    SELECT * FROM usuarios;
''')

registros = meu_cursor.fetchall()

for registro in registros:
    print(f"ID: {registro[0]}, Nome: {registro[1]}, Preço: {registro[2]}")

meu_cursor.close()
conexao.close()