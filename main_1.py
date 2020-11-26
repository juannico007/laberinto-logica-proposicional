#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functions as fn
import maze as mz
import FNC as F
import json
import guardar_reglas as gr

letrasProposicionales = [chr(x) for x in range(256, 2706)]
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
#Reglas estaticas:
#Regla 2
#formula_2 = fn.regla_2(Nfilas, Ncolumnas, Nturnos)
#letrasProposicionales2 = [chr(x) for x in range(3000, 125000)]
#gr.guardar_polaca(formula_2, "formula_2", letrasProposicionales, letrasProposicionales2)

#Regla 3
#formula_3 = fn.regla_3(Nfilas, Ncolumnas, Nturnos)
#letrasProposicionales3 = [chr(x) for x in range(125000, 130000)]
#gr.guardar_polaca(formula_3, "formula_3", letrasProposicionales, letrasProposicionales3)

#Regla 4
#formula_4 = fn.regla_4(Nfilas, Ncolumnas, Nturnos)
#gr.guardar_fnc(fn.String2Tree(formula_4).inorder(), "Formula_4")



#Reglas que varian
regla = []
#Condiciones iniciales
cond_iniciales = fn.cond_inicial(muros, Nfilas, Ncolumnas)
regla += (F.formaClausal(fn.String2Tree(cond_iniciales).inorder()))

#Regla 1
formula_1 = fn.regla_1(inicio, final, Nfilas, Ncolumnas, Nturnos)
regla += (F.formaClausal(fn.String2Tree(formula_1).inorder()))

#Regla 5
formula_5 = fn.regla_5(final, Nfilas, Ncolumnas, Nturnos)
regla += (F.formaClausal(fn.String2Tree(formula_5).inorder()))

with open(archivo + '.json', 'w') as outfile:
        json.dump(regla, outfile)
