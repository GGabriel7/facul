# Esse programa pode pegar algum arquivo de texto adicionado na compilação e transferir o resultado para um outro arquivo. na hora de compilar você faz: python nomeArquivo.py nomeDoTXT.txt > nomeDoArquivoResultado. Fica: python exMapReduce.py exMapReduce.txt > qtd

# Ele recebe um txt com diversas palavras e conta quantas vezes cada uma apareceu e transfere para um outro arquivo.

from mrjob.job import MRJob
import re

palavraRegex = re.compile(r"[\w]+")

class QuantidadePalavras (MRJob):
    def mapper(self, _, linha):
        for p in palavraRegex.findall(linha):
            yield (p.lower(), 1)
            
    def reducer(self, p, qtd):
        yield(p, sum(qtd))
        
if __name__ == '__main__':
    QuantidadePalavras.run()