#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functions as fn
import FNC as ts
import maze as mz
import visualizacion as vs
import DPLL as dp

letrasProposicionales = [chr(x) for x in range(256, 2706)]
interp_verdaderas = {}
Nfilas = 7
Ncolumnas = 7
Nturnos = 49
letras_muros = []
letras_turnos = []
muros = []

#Establece el inicio y el final dado por el usuario
inicio, final = fn.inicio_final(Nfilas, Ncolumnas)

#Crea el laberinto conectado
walls = mz.create_maze(inicio, final, Nfilas, Ncolumnas)

print("Generando letras")

#Letras correspondientes a los muros
for i in range(Nfilas):
    for j in range(Ncolumnas):
        n = fn.codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(n + 256)
        letras_muros.append(cod)

#Asigna valores de verdad a los muros con el laberinto hecho
for(i, j) in walls:
    n = fn.codifica(i, j, Nfilas, Ncolumnas)
    cod = chr(n + 256)
    muros.append(cod)
for i in muros:
        interp_verdaderas[i] = 1
for i in range(Nfilas):
    for j in range(Ncolumnas):
        if (i, j) not in walls:
            n = fn.codifica(i, j, Nfilas, Ncolumnas)
            cod = chr(n + 256)
            interp_verdaderas[cod] = 0

#Letras correspondientes a la presencia del agente en una casilla en un turno
for i in range(Nturnos):
    for j in range(Nfilas):
        for k in range(Ncolumnas):
            n = fn.P(j, k, i, Nfilas, Ncolumnas, Nturnos)
            letras_turnos.append(n)


print("Generando reglas y formula")
formula = ""

#Regla 1
formula_1 = fn.regla_1(inicio, final, Nfilas, Ncolumnas, Nturnos)
formula += formula_1

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

#Regla 6
formula_6 = fn.regla_6(final, Nfilas, Ncolumnas, Nturnos)
formula += formula_6 + "Y"

print("Formula hecha")
print("Ejecutando transformacion de Tseitin")
x = ts.Tseitin(fn.String2Tree(formula).inorder(), letrasProposicionales)
x = ts.formaClausal(x)
print("Transformacion de Tseitin hecha")
print("Forma normal conjuntiva hallada")

print("Buscando interpretación que satisfaga el problema")
I = dp.DPLL(x, interp_verdaderas)
interp_verdaderas = {}
print("Interpretación hallada")
print("Eliminando letras adicionales")
for i in I:
    if i in letras_muros:
        m = ord(i) - 256 - (Nfilas * Ncolumnas)
        interp_verdaderas[m] = I[i]
    elif i in letras_turnos:
        m = ord(i) - 256
        interp_verdaderas[m] = I[i]
print("Letras adicionales eliminadas")
for i in range(Nfilas * Ncolumnas * (Nturnos + 1)):
    if i not in interp_verdaderas:
        interp_verdaderas[i] = 0
vs.dibujar_tablero(interp_verdaderas, Nfilas, Ncolumnas, Nturnos, 122)