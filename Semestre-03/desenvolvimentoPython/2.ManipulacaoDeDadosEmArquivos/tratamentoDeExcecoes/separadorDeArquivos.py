# script para separar arquivos que foram criados no diretorio_de_arquivos. Cada extensão será posta no seu diretorio referente. 

import os
import shutil # Serve para mover arquivos

def criarDiretorio(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio): # Verifica se o diretório já existe
            try:
                os.makedirs(diretorio) # Cria o diretório
                print(f'Diretório {diretorio} criado com sucesso!')
            except PermissionError:
                print(f'Erro: Permissão negada para criar o diretório {diretorio}.')
            except Exception as e:
                print(f'Erro ao criar o diretório {diretorio}: {e}')
                

def moverArquivos(diretorioOrigem):
    for arquivo in os.listdir(diretorioOrigem):
        caminhoArquivo = os.path.join(diretorioOrigem, arquivo)
        
        if os.path.isfile(caminhoArquivo): # Verifica se é um arquivo
            extensao = arquivo.split('.')[-1].lower() # Pega a extensão do arquivo
            if extensao in ['pdf', 'txt', 'jpg', 'png', 'jpeg', 'gif', 'bmp', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']:
                diretorioDestino = os.path.join(diretorioOrigem, extensao) # Define o diretório de destino com base na extensão
                try:
                    if not os.path.exists(diretorioDestino):  # cria só se não existir
                        os.makedirs(diretorioDestino)
                        
                    shutil.move(caminhoArquivo, diretorioDestino) # Move o arquivo para o diretório de destino
                    print(f'Arquivo {arquivo} movido para {diretorioDestino}')
                except PermissionError:
                    print(f'Erro: Permissão negada para mover o arquivo {arquivo}.')
                except Exception as e:
                    print(f'Erro ao mover o arquivo {arquivo}: {e}')
                
            else:
                print(f'Extensão {extensao} não reconhecida. Arquivo {arquivo} não movido.')
                    

def main():
    diretorioDeArquivos = 'diretorio_de_arquivos' # Diretório onde estão os arquivos
    diretorios = [os.path.join(diretorioDeArquivos, ext) for ext in ['pdf', 'txt', 'jpg', 'png', 'jpeg', 'gif', 'bmp', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']]
    
    # Criar diretorios se não existirem
    criarDiretorio(diretorios)
    
    # Mover arquivos para os diretórios correspondentes
    moverArquivos(diretorioDeArquivos)
    

if __name__ == '__main__':
    main()