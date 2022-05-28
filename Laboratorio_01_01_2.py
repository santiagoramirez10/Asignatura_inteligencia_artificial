# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: En este ejercicio, al ejecutar la celda de más abajo, 
se generará una lista de número aleatorios.

Tendrás que calcular el valor promedio de la lista y asignarlo a la variable 
avg más abajo.

Puedes usar el método que quieras para realizar el cálculo (a mano, excel, 
python, etc.) lo que importa es el valor que obtengas.
"""
import numpy as np
def promedio_lista(lista):
    promedio=0
    for i in range(len(lista)):
        promedio+=lista[i]/len(lista)
    return(promedio)
rlist = np.random.randint(100,size=10)
avg=promedio_lista(rlist)