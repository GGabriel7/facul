import os
import errno # Importando o módulo errno para tratar erros específicos do sistema operacional.

#Criando um diretório com os.mkdir e tratando possíveis exceções.

try:
    os.mkdir("novo_diretorio")
    print("Diretório criado com sucesso!")
except FileExistsError:
    print("O diretório já existe.")
    print("Descrição", error)
except PermissionError:
    print("Você não tem permissão para criar esse diretório.")
    print("Descrição", error)
except Exception as error:
    print("Ocorreu um erro inesperado.")
    print("Descrição", error)
    
# Utilizando rmdir para remover o diretório criado.

try:
    os.rmdir("novo_diretorio")
    print("Diretório removido com sucesso!")
except OSError as error:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio.")
    else:
        print("Erro ao remover o diretório:", error)
    print("Descrição", error)
    
# Utilizando makedirs para criar uma estrutura de diretórios.

try:
    os.makedirs("diretorio_pai/diretorio_filho")
    print("Estrutura de diretórios criada com sucesso!")
except FileExistsError:
    print("A estrutura de diretórios já existe.")
    print("Descrição", error)
except PermissionError:
    print("Você não tem permissão para criar essa estrutura de diretórios.")
    print("Descrição", error)
except Exception as error:
    print("Ocorreu um erro inesperado.")
    print("Descrição", error)
    
# Utilizando scarndir para listar o conteúdo de um diretório.

try:
    entradas = os.scandir(".") # Listando o conteúdo do diretório atual.
    
    for obj in entradas:
        print(obj) # Imprimindo cada entrada encontrada.
        print("Nome:", obj.name) # Nome da entrada.
        print("Caminho:", obj.path) # Caminho completo da entrada.
        print("É um diretório?", obj.is_dir()) # Verificando se é um diretório.
        print("É um arquivo?", obj.is_file()) # Verificando se é um arquivo.
        
        if obj.is_file():
            print("Tamanho do arquivo:", obj.stat().st_size, "bytes") # Tamanho do arquivo em bytes.
        print("-" * 40) # Separador para melhor visualização.
    
except PermissionError:
    print("Você não tem permissão para acessar esse diretório.")
    print("Descrição", error)
except Exception as error:
    print("Ocorreu um erro inesperado.")
    print("Descrição", error)
    
# Utilizando removedirs para remover a estrutura de diretórios criada.

try:
    os.removedirs("diretorio_pai/diretorio_filho")
    print("Estrutura de diretórios removida com sucesso!")
except OSError as error:
    print("Erro ao remover a estrutura de diretórios:", error)
    print("Descrição", error)