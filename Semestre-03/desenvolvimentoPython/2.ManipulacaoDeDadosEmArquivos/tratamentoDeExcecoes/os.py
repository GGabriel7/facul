# Módulo os:
# Fornece funcionalidades para interagir com o sistema operacional, como manipulação de arquivos e diretórios.

import os

# Como processar um arquivo e utilizando exxeções

def processarArquivo(arquivoOrigem, arquivoDestino):
    try:
        with open(arquivoOrigem, 'r', encoding="utf-8") as origem:
            conteudo = origem.read()
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivoOrigem} não foi encontrado.")
        return
    
    except PermissionError:
        print(f"Erro: Permissão negada para ler o arquivo {arquivoOrigem}.")
        return
    
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo {arquivoOrigem}: {e}")
        return
    
    try:
        with open(arquivoDestino, 'w', encoding="utf-8") as destino:
            destino.write("Cabeçalho: Conteúdo do arquivo\n")
            destino.write(conteudo)
            destino.write(f"Conteúdo escrito em {arquivoDestino}\n")
            
    except PermissionError:
        print(f"Erro: Permissão negada para escrever no arquivo {arquivoDestino}.")
        return
    except Exception as e:
        print(f"Erro inesperado ao escrever no arquivo {arquivoDestino}: {e}")
        return
    

def main():
    diretorioTrabalho = "diretorioTrabalho"
    
    arquivoOrigem = os.path.join(diretorioTrabalho, "arquivoOrigem.txt")
    arquivoDestino = os.path.join(diretorioTrabalho, "arquivoDestino.txt")
    
    processarArquivo(arquivoOrigem, arquivoDestino)
    
if __name__ == "__main__":
    main()