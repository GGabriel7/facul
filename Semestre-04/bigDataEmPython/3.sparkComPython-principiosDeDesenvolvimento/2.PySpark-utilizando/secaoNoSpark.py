from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() #criamos uma seção do Spark
print(spark) #saida: <pyspark.sql.session.SparkSession object at 0x00000222B882BD40>

dataset = spark.read.csv('2.PySpark-utilizando\california_housing_test.csv', inferSchema=True, header =True) # ler os dados do arquivo california...csv

dataset.head() #exibirá o cabeçalho das colunas e o conteúdo da primeira linha

dataset.count() # mostra a quantidade de linhas

dataset.createOrReplaceTempView('tabela_temporaria') #cria uma tabela temporaria
print(spark.catalog.listTables())

#consulta SQL 
query = 'FROM tabela_temporaria SELECT longitude, latitude LIMIT 3'  
saida = spark.sql(query)  
saida.show() 

spark.stop()