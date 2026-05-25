from pyspark import SparkContext
sparkContext = SparkContext()

lista = [1,2,3,4,5,3]

listaRDD = sparkContext.parallelize(lista) #com isso, eu pego o vetor e transformo os dados dele em um objeto de dados do spark, para eu poder fazer operações nele pelo próprio spark

print(listaRDD.count()) #saida: 6