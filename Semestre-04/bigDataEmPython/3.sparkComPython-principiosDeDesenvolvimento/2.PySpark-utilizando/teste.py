from pyspark import SparkContext
sparkContext = SparkContext() # instanciamos o objeto SparkContext para usarmos na variavel sparkContext
print(sparkContext) #saida: <SparkContext master=local[*] appName=pyspark-shell>
print(sparkContext.version) #saída: 4.1.1