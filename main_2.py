#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import visualizacion as vs
import DPLL as dp
import json

letrasProposicionales = [chr(x) for x in range(256, 2706)]
Nfilas = 7
Ncolumnas = 7
Nturnos = 49

#Archivos creados para distintas pruebas
archivo = "(0, 0)-(0, 6)"
#archivo = "(2, 4)-(1, 6)"
#archivo = "(3, 3)-(0, 0)"
#archivo = "(3, 5)-(0, 4)"
#archivo = "(6, 6)-(4, 5)"

interp_verdaderas = {}

with open(archivo + '.json', 'r') as file:
     reglas = json.load(file)

#print("Ejecutando DPLL...")
#I = dp.DPLL(reglas, interp_verdaderas)
#print("Modelo hallado")

with open(archivo + '_sol.json', 'r') as file:
     interp_verdaderas = json.load(file)

print("Eliminando letras adicionales")
interp_verdaderas = {ord(i)-256:interp_verdaderas[i] for i in interp_verdaderas if i in letrasProposicionales}
print("Letras adicionales eliminadas")

vs.dibujar_tablero(interp_verdaderas, Nfilas, Ncolumnas, Nturnos, archivo)


print(f"Guardando a archivo {archivo}...")
with open(archivo + '_sol.json', 'w') as outfile:
    json.dump(interp_verdaderas, outfile)
print("Terminado!")