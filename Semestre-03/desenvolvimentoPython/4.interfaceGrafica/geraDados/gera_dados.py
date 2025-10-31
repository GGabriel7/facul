from faker import Faker # biblioteca para gerar dados falsos
from conectar import meu_cursor, conexao

fake = Faker('pt_BR')

for _ in range(10):  # Gera 10 registros
    #gerar nome e preços de produtos falsos
    nome = fake.word().capitalize()
    preco = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2)
    print(f"Nome: {nome}, Preço: {preco}")
    
    meu_cursor.execute('''
        INSERT INTO usuarios (nome, preco) VALUES (?, ?)
    ''', (nome, preco))
    
conexao.commit()
print("Dados inseridos com sucesso!")
meu_cursor.close()
conexao.close()