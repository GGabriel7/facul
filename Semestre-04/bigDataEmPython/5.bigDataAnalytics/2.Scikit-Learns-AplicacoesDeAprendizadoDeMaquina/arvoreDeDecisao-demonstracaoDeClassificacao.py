#programa para criarmos e vizualizarmos uma arvore de decisão. Arvore de Decisão é um algoritimo que serve para dividir informações com NÓS de decisão.

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree

#processo de experimentação por meio do treinamento feito com validação cruzada
clf = DecisionTreeClassifier(max_depth=3, random_state=0)
iris = load_iris()
cross_val_score(clf, iris.data, iris.target, cv=10)

#treinamento propriamente dito e à visualização do resultado.
clf.fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.show()