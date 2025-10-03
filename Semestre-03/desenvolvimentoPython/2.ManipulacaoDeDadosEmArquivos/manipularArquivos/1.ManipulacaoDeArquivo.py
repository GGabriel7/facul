import os

#Operações Básicas Para Manipular Arquivos em Python

arquivo1 = open("arquivo1.txt", "w", encoding="utf-8")  #Abre o arquivo para escrita (cria se não existir)

arquivo1.write("Linha 1\n") #Escreve uma linha no arquivo
arquivo1.write("Linha 2\n")
arquivo1.write("Linha 3\n")

print(os.path.abspath(arquivo1.name))  #Mostra o caminho absoluto do arquivo
print(os.path.relpath(arquivo1.name))  #Mostra o caminho relativo do arquivo
print(arquivo1) #Mostra o objeto arquivo
print(arquivo1.name) #Mostra o nome do arquivo
print(arquivo1.mode) #Mostra o modo de abertura do arquivo
print(arquivo1.closed) #Mostra se o arquivo está fechado (False)

arquivo1.close()  #Fecha o arquivo

# Caractere	Significado
# 'r'	Abre o arquivo para leitura (default).
# 'w'	Abre o arquivo para escrita, truncando o arquivo primeiro.
# 'x'	Cria um arquivo para escrita e falha, caso ele exista.
# 'a'	Abre o arquivo para escrita, acrescentando conteúdo ao final do arquivo (mantendo o conteudo anterior), caso ele exista.
# 'b'	Modo binário.
# 't'	Modo texto (default).
# '+'	Abre o arquivo para atualização (leitura ou escrita).