import pandas as pd
df = pd.read_csv('2.preparacaoDeDados/dados_exemplo.csv') #vai analisar todo o arquivo com o pandas. O leitor do arquivo pandas já considera a primeira linha como a o cabeçalho e o adequada, e as virgulas como separação. pode ser usados outros reads como read_excel ou read_json.
print(df)

print("-=-=-=-=-=-=-=-=")

# COM JSON
df2 = pd.read_json('2.preparacaoDeDados/dados_exemplo.json')
print(df2)

print("-=-=-=-=-=-=-=-=")

# transformando lista em dataframe dentro do proprio codigo
array = [{'a':1,'b':2}, {'a':3,'b':4}, {'a':5,'b':6}]
df3 = pd.DataFrame(array)
print(df3)
df3.to_json('2.preparacaoDeDados/dados_copiados.json', orient='records') #criando ou transformando um arquivo json com os dados