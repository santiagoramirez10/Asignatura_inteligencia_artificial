# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: Determinar si un número entero n es un palíndromo,
esto es, si es el mismo número cuando se lee de izquierda a derecha y cuando 
se lee a la derecha a la izquierda. Devuelva True si es así, de lo contrario 
devuelva False.

Reto: usar una sola línea de código.
"""
def palindromo(numero):
  resultado_palindromo=(str(numero))[::-1]==(str(numero))
  return(resultado_palindromo)

