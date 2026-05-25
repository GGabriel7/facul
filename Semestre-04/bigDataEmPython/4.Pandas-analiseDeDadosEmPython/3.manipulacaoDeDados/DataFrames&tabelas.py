# Obs.: Uma característica interessante na estrutura de dados de DataFrame ou dados em painel é o fato de poderem ser criados a partir de praticamente qualquer outra estrutura. Podemos criar Pandas DataFrames a partir de arquivos CSV, Excel, listas de dicionários, matrizes, junções de listas etc.


import pandas as pd
json_array=[ {'a':1,'b':2}, {'a':3,'b':4}, {'a':5,'b':6} ] 
df = pd.DataFrame(json_array)
print(df.info()) #info() resulta na descrição de cada coluna e seu tipo, com a contagem de valores não nulos.
print("-=-=-=-=-=-=-=-=-=-=-=-")
print(df.describe()) #describe() resulta na descrição de estatísticas bem básicas, como, a contagem de cada coluna(count), quantos valores unicos de cada variavel(unique), quantas categorias, o primeiro registro(top), drequencia(freq)...