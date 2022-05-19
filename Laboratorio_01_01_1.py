# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez

Objetivo del laboratorio: Completa la función suma_matrices para que, dadas 
dos arrays numpy cualquiera devuelva la suma elemento a elemento.
"""
def suma_matrices(matriz_a,matriz_b):
  matriz_suma=[]
  for i in range(len(matriz_a)):
    filas_matriz=[]
    for j in range(len(matriz_a[i])):
      filas_matriz.append(matriz_a[i][j]+matriz_b[i][j])
    matriz_suma.append(filas_matriz)
  return(matriz_suma)