#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functions as fn
import tableaux as tb
import maze as mz
import visualizacion as vs


interp_verdaderas = {x:0 for x in range(2450)}  
Nfilas = 7
Ncolumnas = 7
Nturnos = 49
letras_muros = []
letras_turnos = []
muros = []

print("Se jugara en un tablero de", Nfilas, "x", Ncolumnas)
print("Para iniciar, se requieren la posicion inicial y final del jugador")

inicio, final = fn.inicio_final(Nfilas, Ncolumnas)

walls = mz.create_maze(inicio, final, Nfilas, Ncolumnas)

print("\nletras representando muros")
print("\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        n = fn.codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(n + 256)
        print(cod, end=" ")
        letras_muros.append(cod)
    print()
    
for(i, j) in walls:
    muros.append(fn.codifica(i, j, Nfilas, Ncolumnas))
    
for i in muros:
        interp_verdaderas[i] = 1
    
print("\nletras por turnos")
for i in range(Nturnos):
    print("\nturno", i, ": ")
    for j in range(Nfilas):
        for k in range(Ncolumnas):
            n = fn.P(j, k, i, Nfilas, Ncolumnas, Nturnos)
            print(n, end=" ")
            letras_turnos.append(n)
        print()
        
formula = ""

print("\nGenerando regla 1:")
formula_1 = fn.regla_1(inicio, final, Nfilas, Ncolumnas, Nturnos)
formula += formula_1

print("\nGenerando regla 2:")
formula_2 = fn.regla_2(Nfilas, Ncolumnas, Nturnos)
formula += formula_2 + "Y"


print("\nGenerando regla 3:")
formula_3 = fn.regla_3(Nfilas, Ncolumnas, Nturnos)
formula += formula_3 + "Y"

print("\nGenerando regla 4:")
formula_4 = fn.regla_4(Nfilas, Ncolumnas, Nturnos)
formula += formula_4 + "Y"

print("\nGenerando regla 5:")
formula_5 = fn.regla_5(final, Nfilas, Ncolumnas, Nturnos)
formula += formula_5 + "Y"


turnos = [80, 128, 170, 212, 254, 296, 346, 396, 452, 508, 558, 608, 664, 720, 776, 2449]
for i in range(832, 2449, 49):
    turnos.append(i)
for i in turnos:
    interp_verdaderas[i] = 1
        
vs.dibujar_tablero(interp_verdaderas, 7, 7, 49, 121)
#print(tb.Tableaux(formula))
#tb.imprime_listaHojas(tb.listaHojas)