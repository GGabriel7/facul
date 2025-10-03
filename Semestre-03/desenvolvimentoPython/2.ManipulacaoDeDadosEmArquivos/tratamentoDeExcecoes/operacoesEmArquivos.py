import os

# Utilizando a função remove() para deletar um arquivo

arquivoRemover = 'arquivoRemover.txt'

try:
    os.remove(arquivoRemover)
    print(f'Arquivo {arquivoRemover} removido com sucesso!')
except FileNotFoundError:
    print(f'Arquivo {arquivoRemover} não encontrado. Nada foi removido.')
except Exception as e:
    print(f'Ocorreu um erro ao tentar remover o arquivo: {e}')
    
# Utilizando a função rename() para renomear um arquivo
nomeAntigo = 'arquivoAntigo.txt'
nomeNovo = 'arquivoNovo.txt'

try:
    os.rename(nomeAntigo, nomeNovo)
    print(f'Arquivo renomeado de {nomeAntigo} para {nomeNovo} com sucesso!')
except FileNotFoundError:
    print(f'Arquivo {nomeAntigo} não encontrado. Não foi possível renomear.')
except Exception as e:
    print(f'Ocorreu um erro ao tentar renomear o arquivo: {e}')
    