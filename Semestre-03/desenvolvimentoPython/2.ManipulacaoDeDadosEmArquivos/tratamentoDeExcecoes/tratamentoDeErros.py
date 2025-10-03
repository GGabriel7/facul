# Tratamento de errps em Python é feito com o bloco try e except
# O bloco try tenta executar um código que pode gerar um erro e o bloco except captura esse erro e permite que você lide com ele de forma adequada

try:
    #Tentativa de criar um arquivo em um diretporio protegido por permissões
    with open('/root/arquivo_protegido.txt', 'w') as arquivo:
        arquivo.write('Conteúdo do arquivo')

except PermissionError:
    print("Erro: Permissão negada ao tentar criar o arquivo.")
    

try:
    # Tentativa de criar um arquivo que já existe
    with open('arquivo_existente.txt', 'x') as arquivo:
        arquivo.write('Conteúdo do arquivo')
exept FileExistsError:
    print("Erro: O arquivo já existe.")
    

try:
    # Tentativa de abrir um arquivo que não existe
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")


try:
    # Tentativa de escrever em um arquivo aberto em modo de leitura
    with open('arquivo.txt', 'r') as arquivo:
        arquivo.write('Novo conteúdo')
        
except IOError:
    print("Erro: Operação de E/S falhou.")
    
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Erro inesperado: {e}")

try:
    # Tentativa de dividir por zero
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")