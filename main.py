#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functions as fn

Nfilas = 7
Ncolumnas = 7
Nturnos = 49
letras_muros = []
letras_turnos = []

print("Se jugara en un tablero de", Nfilas, "x", Ncolumnas)
print("Para iniciar, se requieren la posicion inicial y final del jugador")

inicio, final = fn.inicio_final(Nfilas, Ncolumnas)

print("\nletras representando muros")
print("\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        n = fn.codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(n + 256)
        print(cod, end=" ")
        letras_muros.append(cod)
    print()
    
print("\nletras por turnos")
for i in range(Nturnos):
    print("\nturno", i, ": ")
    for j in range(Nfilas):
        for k in range(Ncolumnas):
            n = fn.P(j, k, i, Nfilas, Ncolumnas, Nturnos)
            print(n, end=" ")
            letras_turnos.append(n)
        print()
    
print("\nRegla 1:")
formula_1 = fn.regla_1(inicio, final, Nfilas, Ncolumnas, Nturnos)
print(fn.Inorderp(fn.String2Tree(formula_1), Nfilas, Ncolumnas, Nturnos))

print("\nRegla 2:")
formula_2 = fn.regla_2(Nfilas, Ncolumnas, Nturnos)
print(fn.Inorderp(fn.String2Tree(formula_2), Nfilas, Ncolumnas, Nturnos))

print("\nRegla 3:")
formula_3 = fn.regla_3(Nfilas, Ncolumnas, Nturnos)
print(fn.Inorderp(fn.String2Tree(formula_3), Nfilas, Ncolumnas, Nturnos))

print("\nRegla 4:")
formula_4 = fn.regla_4(Nfilas, Ncolumnas, Nturnos)
print(fn.Inorderp(fn.String2Tree(formula_4), Nfilas, Ncolumnas, Nturnos))

print("\nRegla 5:")
formula_5 = fn.regla_5(final, Nfilas, Ncolumnas, Nturnos)
print(fn.Inorderp(fn.String2Tree(formula_5), Nfilas, Ncolumnas, Nturnos))
    