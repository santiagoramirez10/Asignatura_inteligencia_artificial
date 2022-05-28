# -*- coding: utf-8 -*-
"""
@author: Santiago Ramírez Pérez

Objetivo del laboratorio: En este ejercicio, su programa recibirá un monto 
entre 1 y 99 centavos de Dolar, Escriba un metodo que retorne en una lista, 
cuantas monedas son necesarias para devolverle a alguien dicho valor, si 
únicamente se cuenta con monedas de 1, 10 y 25 centavos. La lista debe 
entregarse de la siguiente manera:
    
En esta tarea tu función recibirá una cantidad entre 1 y 99 céntimos y deberá 
devolver una lista con tres números [n1, n10, n25], especificando cuántas 
monedas de 1, 10 y 25 céntimos se necesitan para obtener la cantidad dada. 
Sólo disponemos de monedas de 1, 10 y 25 céntimos. No hay otros tipos de
monedas.
"""
def change_money(dinero_ingresado):
    if dinero_ingresado<1 or dinero_ingresado>99:
        print(None)
    monedas_25=dinero_ingresado//25
    dinero_ingresado=dinero_ingresado-(monedas_25*25)
    monedas_10=dinero_ingresado//10
    dinero_ingresado=dinero_ingresado-(monedas_10*10)
    monedas_1=dinero_ingresado//1
    cambio_monedas=[monedas_1,monedas_10,monedas_25]
    return(cambio_monedas)
