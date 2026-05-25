def printL():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
import pandas as pd
    
df = pd.DataFrame({'Animal': ['Cachorro', 'Cachorro',
                               'Pinguim', 'Pinguim',
                               'gato', 'gato',
                               'falcao'],
                    'Max Speed': [48., 24., 9., 6., 48., 47., 380.]})
print(df)
printL()

agrupar = df.groupby(['Animal']) #eu agrupo todos os dados da coluna animal com o nome igual
print(agrupar.mean().reset_index()) #o mean() serve para mostrar a media com a junção dos dados de mesmo nome. O reset_index() serve para reoganizar a tabela com os ID, pois sem ele o nome dos animais vão passar a se tornar os IDs.
printL()

df2 = pd.DataFrame([[4,9], [16, 25], [36,49]], columns=['Coluna A', 'Coluna B'])
print(df2)
import numpy as np
print(df2.apply(np.sqrt))#com o aplly, eu pego todos os dados do dataframe e aplico o calculo de raiz quadrado da biblioteca numpy
printL()
df2['Coluna A'] = df2['Coluna A'].apply(lambda x: x+10) #eu APLICO em toda a Coluna A uma lambda para acrescer 10 nos dados
print(df2)
printL()
df2['Coluna C'] = df2.apply(lambda x: x['Coluna A']+x['Coluna B'], axis=1) #eu crio uma nova coluna com a soma das duas colunas A e B aplicando o lambda para soma-las
print(df2)