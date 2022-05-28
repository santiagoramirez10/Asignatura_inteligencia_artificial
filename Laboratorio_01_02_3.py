# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: Comprender los datos y la métrica de evaluación 
(Root Mean Squared Logarithmic Error, RMSLE) de la siguiente competencia de 
Kaggle:

https://www.kaggle.com/c/nyc-taxi-trip-duration/

Observe que esta competencia es una tarea de regresión ya que estamos midiendo 
la diferencia en la predicción con respecto a la real.

Ejecute la siguiente celda para generar los datos a partir de los cuales 
debe calcular la métrica. Puede calcular la métrica implementando el código 
python, o manualmente, o copiar/pegar los datos reales y previstos en Excel, 
etc.

import numpy as np
t3_actual    = np.random.randint(80,size=15)+20
t3_predicted = np.random.randint(80,size=15)+20
print ("actual   ", t3_actual)
print ("predicted", t3_predicted)

Desafío: para python, use la función numpy np.log o np.log1p.

Observe que cada vez que ejecuta la siguiente celda, se genera un conjunto 
diferente de valores. Tendrá que calcular la métrica para los valores que ve. 
Si vuelve a ejecutar la celda, tendrá que volver a calcular el valor de la 
métrica.
"""
import numpy as np
from sklearn.metrics import mean_squared_log_error
t3_actual=np.random.randint(80,size=15)+20
t3_predicted=np.random.randint(80,size=15)+20
rmsle=mean_squared_log_error(t3_actual,t3_predicted, squared=False)