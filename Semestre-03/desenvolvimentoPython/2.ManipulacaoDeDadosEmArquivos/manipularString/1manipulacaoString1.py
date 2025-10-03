arquivo = open('textos.txt', 'r', encoding='utf-8')

conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
print('Tipo de conteudo:', type(conteudo)) # Mostra o tipo do conteúdo lido
print('Conteudo retornado pelo read():')
print(repr(conteudo)) # Mostra o conteúdo lido, incluindo caracteres especiais

proximo_conteudo = arquivo.readline() # Tenta ler a próxima linha (não haverá mais conteúdo)
print('\nTipo de conteudo:', type(proximo_conteudo)) # Mostra o tipo do conteúdo lido
print('Próximo conteudo retornado pelo read():')
print(repr(proximo_conteudo)) # Mostra que não há mais conteúdo a ser lido

conteudoRestante = arquivo.readlines() # Tenta ler todas as linhas restantes (não haverá mais conteúdo)
print('\nTipo de conteudo:', type(conteudoRestante)) # Mostra o tipo do conteúdo lido
print('Próximo conteudo retornado pelo read():')
print(repr(conteudoRestante))

arquivo.close() # Fecha o arquivo