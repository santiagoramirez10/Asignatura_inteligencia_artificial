# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: Comprender los datos y la métrica de evaluación 
(pérdida logarítmica multiclase, logloss) de la siguiente competencia de Kaggle:

https://www.kaggle.com/c/shelter-animal-outcomes/

Observe que esta competencia es una tarea de clasificación con 5 clases y, para 
cada elemento, el modelo produce una probabilidad para cada clase. Las clases 
están numeradas del 0 al 4.

Ejecute la siguiente celda para generar los datos a partir de los cuales debe 
calcular la métrica. Puede calcular la métrica implementando el código python, o 
manualmente, o copiar/pegar los datos reales y previstos en Excel, etc.

import numpy as np
t4_predicted = np.random.random(size=(7,5)).T+0.5
t4_predicted = np.round((t4_predicted/np.sum(t4_predicted,axis=0)),2).T
t4_actual = np.eye(5)[np.random.randint(5,size=len(t4_predicted))].astype(int)
print ("actual")
print (t4_actual)
print ("\npredicted")
print (t4_predicted)

Asigne el valor de su cálculo a la variable logloss con tres decimales
"""
import numpy as np
from sklearn.metrics import log_loss
t4_predicted=np.random.random(size=(7,5)).T+0.5
t4_predicted=np.round((t4_predicted/np.sum(t4_predicted,axis=0)),2).T
t4_actual=np.eye(5)[np.random.randint(5,size=len(t4_predicted))].astype(int)
logloss=log_loss(t4_actual, t4_predicted)
logloss=round(logloss,3)