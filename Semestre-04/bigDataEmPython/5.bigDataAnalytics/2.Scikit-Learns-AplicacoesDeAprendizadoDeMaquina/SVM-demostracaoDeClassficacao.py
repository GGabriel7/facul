# Vamos implemetar um classificar SVM em Python com o scikit-learn. SVM é um algoritimo capaz de separar observações em um espaço linear ou não linear atraves dos seus vetores.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import load_iris  # dataset considerado classico no ambito do aprendizado de maquina, classifica tipos da especie iris a partir de caracteristicas como comprimento de petala, largura da petala, comprimento da sepala e largura da sepala em cm.
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data.feature_names)
target = data.target

#Para a instanciação simples do classificador
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
svc = SVC(gamma='auto')

#Testando o modelo 'svc' na nossa base 'iris'
cv_result = cross_val_score(svc, iris, target, cv=10, scoring='accuracy')
print('acurácia com cross validation: ', cv_result.mean()*100)

#treinar nosso modelo com o dataset inteiro e tentar predizer um valor inédito.
svc.fit(iris, target)
#Prediz a que classe pertencerá a flor com sépala de comprimento 6.9 cm e de largura 2.8 cm, e com pétala de comprimento 6.1 cm e de largura 2.3 cm
svc.predict([[6.9, 2.8, 6.1, 2.3]])
#visualizar nossos dados e os hiperplanos definidos pelo modelo.
plt.scatter(iris['sepal length (cm)'], iris['petal width (cm)'], c=target)
plt.title('Iris')
plt.show()