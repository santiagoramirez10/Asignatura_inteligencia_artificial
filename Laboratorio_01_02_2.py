# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: Calcule la métrica de sensibilidad [también conocida 
como Tasa de verdadero positivo o Recuperación, consulte Sensibilidad en 
Wikipedia] para el siguiente resultado del modelo (previsto) y la realidad del 
terreno (real)

Ejecute la siguiente celda para generar los datos a partir de los cuales debe 
calcular la métrica. Puede calcular la métrica implementando el código python, 
o manualmente, o copiar/pegar los datos reales y previstos en Excel, etc.

import numpy as np
t2_predicted = np.random.randint(2, size=20)
t2_actual = np.random.randint(2, size=20)
t2_predicted[np.argwhere(t2_actual==1)[0][0]]=0
print ("actual   ", ", ".join([str(i) for i in t2_actual]))
print ("predicted", ", ".join([str(i) for i in t2_predicted]))

Desafío: usa Python sklearn.metrics.recall_score

Observe que cada vez que ejecuta la siguiente celda, se genera un conjunto 
diferente de valores. Tendrá que calcular la métrica para los valores que ve. 
Si vuelve a ejecutar la celda, tendrá que volver a calcular el valor de la 
métrica.
"""
import numpy as np
from sklearn.metrics import recall_score
t2_actual=np.random.randint(2,size=20)
t2_predicted=np.random.randint(2, size=20)
t2_predicted[np.argwhere(t2_actual==1)[0][0]]=0
tpr=recall_score(t2_actual,t2_predicted)