#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functions as fn
import FNC as ts
import maze as mz
import visualizacion as vs
import DPLL as dp
import guardar_reglas as gr

letrasProposicionales = [chr(x) for x in range(256, 2706)]
interp_verdaderas = {}
Nfilas = 7
Ncolumnas = 7
Nturnos = 49
letras_muros = []
letras_turnos = []

#Establece el inicio y el final dado por el usuario
inicio, final = fn.inicio_final(Nfilas, Ncolumnas)
archivo = str(inicio) + "-" + str(final)

#Crea el laberinto conectado
muros = mz.create_maze(inicio, final, Nfilas, Ncolumnas)

print("Generando letras")

#Letras correspondientes a los muros
for i in range(Nfilas):
    for j in range(Ncolumnas):
        n = fn.codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(n + 256)
        letras_muros.append(cod)


#Letras correspondientes a la presencia del agente en una casilla en un turno
for i in range(Nturnos):
    for j in range(Nfilas):
        for k in range(Ncolumnas):
            n = fn.P(j, k, i, Nfilas, Ncolumnas, Nturnos)
            letras_turnos.append(n)


print("Generando reglas y formula")
formula = ""

#Condiciones iniciales
cond_iniciales = fn.cond_inicial(muros, Nfilas, Ncolumnas)
formula += cond_iniciales

#Regla 1
formula_1 = fn.regla_1(inicio, final, Nfilas, Ncolumnas, Nturnos)
formula += formula_1 + "Y"

#Regla 2
formula_2 = fn.regla_2(Nfilas, Ncolumnas, Nturnos)
formula += formula_2 + "Y"

#Regla 3
formula_3 = fn.regla_3(Nfilas, Ncolumnas, Nturnos)
formula += formula_3 + "Y"

#Regla 4
formula_4 = fn.regla_4(Nfilas, Ncolumnas, Nturnos)
formula += formula_4 + "Y"

#Regla 5
formula_5 = fn.regla_5(final, Nfilas, Ncolumnas, Nturnos)
formula += formula_5 + "Y"

gr.guardar_polaca(formula, archivo, letrasProposicionales)
'''
print("Buscando interpretación que satisfaga el problema")
I = dp.DPLL(x, interp_verdaderas)
interp_verdaderas = {}
print("Interpretación hallada")
print("Eliminando letras adicionales")
for i in I:
    if i in letras_muros:
        m = ord(i) - 256
        interp_verdaderas[m] = I[i]
    elif i in letras_turnos:
        m = ord(i) - 256
        interp_verdaderas[m] = I[i]
print("Letras adicionales eliminadas")
for i in range(Nfilas * Ncolumnas * (Nturnos + 1)):
    if i not in interp_verdaderas:
        interp_verdaderas[i] = 0

vs.dibujar_tablero(interp_verdaderas, Nfilas, Ncolumnas, Nturnos, 122)'''