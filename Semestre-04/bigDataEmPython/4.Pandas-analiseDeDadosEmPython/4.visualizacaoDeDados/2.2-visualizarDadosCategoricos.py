import plotly.express as px #API para criação de gráficos no Python que contém diversos datasets de testes

#Exemplo de quadro hipotético de medalhas da China, Coreia do Sul e Canadá em um gráfico de barras
long_df = px.data.medals_long()
fig = px.bar(long_df, x='nation', y='count', color='medal', title='Long-Form Input') 
fig.show()

#Gráfico de pizza mostrando a proporção dos valores distintos de dias da semana no conjunto de comandas
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
fig.show()