from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

#Keras é uma biblioteca para desenvolvimento de redes neurais, projetada para permitir experimentação rápida.
from tensorflow.keras.models import Sequential #cria modelos em sequência (camada após camada)
from tensorflow.keras.layers import Dense #camada totalmente conectada (a mais comum)
from tensorflow.keras.optimizers import SGD #otimizador (Stochastic Gradient Descent)
from tensorflow.keras.datasets import mnist #dataset pronto de dígitos (0–9)
from tensorflow.keras import backend as K #funções de baixo nível do Keras

import matplotlib.pyplot as plt
import numpy as np

#Basicamente, nossa rede neural vai aprender a reconhecer o padrão de escrita de números
print('[INFO] acessing MNIST...')
((trainX, trainY), (testX, testY)) = mnist.load_data()

#normalizaremos os dados para que fiquem entre 0 e 1, e faremos isso dividindo o conjunto por 255
trainX = trainX.reshape((trainX.shape[0], 28 * 28 * 1))
testX = testX.reshape((testX.shape[0], 28 * 28 * 1))
trainX = trainX.astype('float32') / 255.0
testX = testX.astype('float32') / 255.0

lb = LabelBinarizer() #faz com o que o resultado da classe se torne binário, ou seja, ao invés de lidarmos com a classe de valor 5, passaremos a lidar com 0000100000.
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

#dividindo arquitetura da rede neural com akuda do Keras
model = Sequential() #Adicionando uma camada atrás da outra em sequência
model.add(Dense(256, input_shape=(784,), activation='sigmoid'))
model.add(Dense(128, activation='sigmoid'))
model.add(Dense(10, activation='softmax'))
# Uma camada de entrada de 784 nós, um para cada pixel da imagem em questão, que se conectará a uma camada oculta densa de 256 nós pela função de ativação da sigmoide.
# Depois, a primeira camada oculta se conectará à segunda, de 128 nós, também por sigmoide.
# Esta se conectará à última camada de predição com 10 nós conectados a partir da Softmax. São 10 nós, porque temos 10 possíveis dígitos.

#a rede tem 100 iterações para convergir e apreender, e vamos apresentar lotes de 128 imagens cada por iteração. 
sgd = SGD(0.01)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=100, batch_size=128)

#vamos utilizar a classification_report, uma função do sklearn que compara os valores preditos com os reais, passados como argumentos.
predictions = model.predict(testX, batch_size=128)
print(classification_report(
    testY.argmax(axis=1), 
    predictions.argmax(axis=1), 
    target_names=[str(x) for x in lb.classes_]
))

#Esse código resultará no gráfico para podemos ver como a rede evoluiu até chegar a essas métricas, ou seja, como a função de custo foi sendo otimizada e a acurácia foi subindo.
plt.style.use('ggplot')
plt.figure()
plt.plot(np.arange(0, 100), H.history['loss'], label='train_loss')
plt.plot(np.arange(0, 100), H.history['val_loss'], label='val_loss')
plt.plot(np.arange(0, 100), H.history['accuracy'], label='train_acc')
plt.plot(np.arange(0, 100), H.history['val_accuracy'], label='val_acc')
plt.title('Training Loss and Accuracy')
plt.xlabel('Epoch #')
plt.ylabel('Loss/Accuracy')
plt.legend() #mostra o resultado no terminal de comando
plt.show() #abre uma pagina para mostrar o resultado
