import sqlite3 as conector
from modulo import Pessoa

conexao = conector.connect('./bancoDeDados.db', detect_types=conector.PARSE_DECLTYPES) # Permite trabalhar com tipos de dados nativos do Python

cursor = conexao.cursor()

def converterBooleanos(dado):
    return True if dado == 1 else False # Converte 1/0 para True/False

conector.register_converter("BOOLEAN", converterBooleanos) # Registra a função de conversão para o tipo BOOLEAN

cursor.execute("SELECT * FROM Veiculo")
registros = cursor.fetchall()
for registro in registros:
    print(f"Placa: {registro[0]} | Modelo: {registro[1]} | Ano: {registro[2]} | Proprietario CPF: {registro[3]}")
    print("-" * 50)
    
# Consulta para buscar pessoas que usam óculos
cursor.execute("SELECT * FROM Pessoa WHERE usa_oculos=:usa_oculos", {"usa_oculos": True})
registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro) # Desempacota a tupla diretamente no construtor da classe Pessoa
    print("CPF:", type(pessoa.cpf), pessoa.cpf)
    print("Nome:", type(pessoa.nome), pessoa.nome)
    print("Data de Nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("Usa Óculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)
    print("-" * 50)
    
# Utilizando o JOIN para buscar veículos e seus proprietários. JOIN serve para combinar registros de duas ou mais tabelas com base em uma condição relacionada entre elas.
cursor.execute("""
    SELECT Pessoa.nome, Veiculo.placa, Veiculo.cor, Veiculo.ano
    FROM Pessoa
    JOIN Veiculo ON Pessoa.cpf = Veiculo.proprietario
""")
registros = cursor.fetchall()
for registro in registros:
    print(f"Nome: {registro[0]} | Placa: {registro[1]} | Cor: {registro[2]} | Ano: {registro[3]}")
    print("-" * 50)
    
cursor.close()
conexao.close()