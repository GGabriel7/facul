from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("TesteInstalacaoSpark").getOrCreate()