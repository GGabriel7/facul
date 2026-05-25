import pandas as pd
import numpy as np

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() #criamos uma seção do Spark

dataset = spark.read.csv('2.PySpark-utilizando\california_housing_test.csv', inferSchema=True, header =True) # ler os dados do arquivo california...csv

dataset.createOrReplaceTempView('tabela_temporaria') #cria uma tabela temporaria

#consulta SQL 
query1 = 'SELECT MAX(total_rooms) as maximo_quartos FROM tabela_temporaria'
q_maximo_quartos = spark.sql(query1)
pd_maximo_quartos = q_maximo_quartos.toPandas()
print('A quantidade máxima de quartos é: {}'.format(pd_maximo_quartos['maximo_quartos']))
qtd_maximo_quartos = int(pd_maximo_quartos.loc[0,'maximo_quartos'])

query2 = 'SELECT longitude, latitude FROM tabela_temporaria WHERE total_rooms = '+str(qtd_maximo_quartos)
localizacao_maximo_quartos = spark.sql(query2)
pd_localizacao_maximo_quartos = localizacao_maximo_quartos.toPandas()
print(pd_localizacao_maximo_quartos.head())
