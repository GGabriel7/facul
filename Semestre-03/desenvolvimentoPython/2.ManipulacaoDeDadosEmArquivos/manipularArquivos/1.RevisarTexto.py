def main():
    print("Digite suas Frases. Digite 'sair' para finalizar.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == 'sair':
            break
        frases.append(entrada)
        
    with open("meuArquivo.txt", "w", encoding="utf-8") as arquivo: #Abre o arquivo para escrita (cria se não existir)
        for frase in frases:
            arquivo.write(frase + "\n")
            
    print("Arquivo original criado. Agora vamos manipulá-lo.")
    
    dadosModificados = []
    
    with open("meuArquivo.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dadosModificados.append(linha.strip().upper()) #Exemplo de manipulação: converter para maiúsculas
            
    with open("meuArquivo.txt", "w", encoding="utf-8") as arquivo:
        for linha in dadosModificados:
            arquivo.write(linha + "\n")
    
    print("Arquivo modificado.")
    

if __name__ == "__main__":
    main()