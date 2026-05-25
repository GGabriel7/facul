#objetivo: pegar uma arrey e introduzir um calculo em cada elemento (mapeando cada elemento) e depois somar tudo (reduzindo assim o arrey)

from pyspark import SparkContext
sparkContext = SparkContext()

#criando dados para ser analisado com o spark
import numpy as np
vetor = np.array([10, 20, 30, 40, 50])
print(vetor) #[10, 20, 30, 40, 50]

paralelo = sparkContext.parallelize(vetor) #coloacor a variavel vetor para ser analisada com o spark e deixamos ela disponível atráves da var paralelo
print(paralelo)# saida: ParallelCollectionRDD[3] at readRDDFromFile at PythonRDD.scala:274

# mapeando os dados | mapear cada elemento do vetor para ser introduzido neles a formula x**2+x
mapa = paralelo.map(lambda x : x**2+x)
mapa.collect()
print(mapa) # saida: [110, 420, 930, 1640, 2550]

#reduzindo | pagararei os dados que foram mapeados anteriormente sendo aplicado a formula x**2+x em cada elemento do vetor farei o somatorio
from operator import add

somatorio = mapa.reduce(add)
print(somatorio) #print: 5650