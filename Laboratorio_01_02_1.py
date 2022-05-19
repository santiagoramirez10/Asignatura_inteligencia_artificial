# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez

Objetivo del laboratorio: Calcule el porcentaje de precisión de las predicciones 
correctas (consulte aquí) para la siguiente salida del modelo (predicha) y la 
realidad del terreno (real).

Ejecute la siguiente celda para generar los datos a partir de los cuales debe 
calcular la métrica. Puede calcular la métrica implementando el código python, 
o manualmente, o copiar/pegar los datos reales y previstos en Excel, etc.

RETO: usar Python con sklearn.metrics.accuracy_score

Observe que cada vez que ejecuta la siguiente celda, se genera un conjunto 
diferente de valores. Tendrá que calcular la métrica para los valores que ve. 
Si vuelve a ejecutar la celda, tendrá que volver a calcular el valor de la 
métrica.
"""
import numpy as np
from sklearn.metrics import accuracy_score
t1_actual=np.random.randint(2, size=20)
t1_predicted=np.abs(t1_actual*(np.random.random(size=20)>(np.random.random()*.9+.05)).astype(int))
accuracy=accuracy_score(t1_actual,t1_predicted)