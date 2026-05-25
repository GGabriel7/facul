import plotly.express as px #API para criação de gráficos no Python que contém diversos datasets de testes

#gera um histograma
df = px.data.tips()
fig = px.histogram(df, x='total_bill') 
fig.show()

# gera um gráfico de dispersão, scatterplot
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', symbol='species')
fig.show()