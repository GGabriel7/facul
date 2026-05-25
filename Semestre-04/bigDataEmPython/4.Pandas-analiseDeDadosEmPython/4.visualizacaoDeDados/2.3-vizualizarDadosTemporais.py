import plotly.express as px
df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.show()

#GERAR GRÁFICO EM LINHA mostrando a expectativa de vida ao longo dos anos para Austrália e Nova Zelândia