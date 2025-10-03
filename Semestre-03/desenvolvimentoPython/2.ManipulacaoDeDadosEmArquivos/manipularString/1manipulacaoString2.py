with open('textos.txt') as arquivo:
    contador_linhas = 0
    print('Retornando o conteúdo do arquivo:')
    for linha in arquivo:
        print(repr(linha)) #repr mostra os caracteres especiais
        if linha:
            contador_linhas += 1
        
    print(f'\nO arquivo possui {contador_linhas} linhas.\n')
    
with open('textos.txt') as arquivo:
    contador = 0
    print('Representação do arquivo após o uso do método strip():')
    for linha in arquivo:
        linhaLimpa = linha.strip() #strip remove os espaços em branco do início e do fim da string
        print(repr(linhaLimpa))
        if linhaLimpa:
            contador += 1
    
    print(f'\nO arquivo possui {contador} linhas com conteúdo.')
    
# A diferença é que o método strip() remove os espaços em branco do início e do fim da string, removendo as linhas em branco e mantendo apenas as linhas com conteúdo.

with open('textos.txt') as arquivo:
    texto = arquivo.read() #lê todo o conteúdo do arquivo de uma vez
    contador = texto.count('O') # conta o número de ocorrências da letra 'O' maiúscula no texto
    print(f'\nO arquivo possui {contador} letras "O" maiúsculas.')
    
    contador2 = texto.count(',') # conta o número de vírgulas no texto
    print(f'O arquivo possui {contador2} vírgulas.\n')