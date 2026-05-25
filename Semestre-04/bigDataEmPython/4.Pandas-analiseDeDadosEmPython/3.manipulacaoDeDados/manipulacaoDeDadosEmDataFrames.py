import pandas as pd
def printL():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

df = pd.DataFrame([[1,2], [4,5], [7,8], [11,12], [15, 16]], index=('cobra', 'viper', 'sidewinder', 'python', 'coral'), columns=['maxSpeed', 'shield'])
#index coloca cabeçalho, e columns coloca "cabeçalhos na lateral"
print(df)
printL()

print(df.loc['viper']) 
printL()
#o loc tem um efeito semelhante ao selec em SQL, ele captura certo dado da tabela
print(df.loc[['cobra', 'sidewinder']])
printL()

#No caso do iloc, a projeção depende dos indexes numéricos das linhas e colunas de um DataFrame.
print(df.iloc[0]) #mostra uma coluna especifica
printL()
print(df.iloc[[0]])#mostra uma linha especifica
printL()
print(df.iloc[[0,2]]) #mostra linhas especificas
printL()
print(df.iloc[:3]) #mostra de inicio até a terceira linha
printL()
print(df.iloc[2:5]) #mostra de tal linha até tal linha
printL()

# temos o jeito de fazer seleções e projeções por queries.
df2 = pd.DataFrame({'A': range(1,6), #range de 1 a 6
                    'B': range(10, 0, -2),  #range de 10 até 0 pulando de 2 em 2
                    'C': range(10, 5, -1)}) #range de 10 até 5 de 1 em 1
print(df2)
printL()
print(df2.query('A>B')) #mostra a linha quando o item de A for maior que B
printL()
print(df2.query('B == C'))
printL()
print(df2.query('B == 8')) 
printL()
print(df2[df2.A < df2.B]) #mesmo que query
printL()

# podemos deleter tambeme. Para isso utilizamos o drop.
df2 = df2.drop(columns=['C']) #para remover uma coluna toda. Ou df2.drop(columns=['B'], inplace=True)
print(df2)
printL()
df2 = df2.drop([1]) #deletar uma linha especifica ou [1,2], [:3] para deletar quais quisermos
print(df2)
printL()

# para reidexar os index
df2 = df2.reset_index(drop=True) # ou  df.reset_index(drop=True, inplace=True)
print(df2)

#Assim como nos bancos de dados, temos também as operações de junção, feitas pelo concat, merge e join.
#pd.concat([df, df2], axis=1) 
#df.merge(df2, left_on='lkey', right_on='rkey', suffixes=(“_left”,”_right”)))
#df.join(df2, lsuffix='_caller', rsuffix='_df2')