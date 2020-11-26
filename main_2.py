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
archivo = "(0, 0)-(0, 6)"                  #prueba correcta
#archivo = "(2, 4)-(1, 6)"                  
#archivo = "(3, 3)-(0, 0)"                  #crasheo, no asigno valores de verdad a todas las letras ._.
#archivo = "(3, 5)-(0, 4)"
#archivo = "(6, 6)-(4, 5)"

interp_verdaderas = {}

print("Importando reglas...")
formula = []

with open("formula_2" + '.json', 'r') as file:
     regla_2 = json.load(file)
     

with open("formula_3" + '.json', 'r') as file:
     regla_3 = json.load(file)
     
with open("formula_4" + '.json', 'r') as file:
     regla_4 = json.load(file)
     
with open(archivo + '.json', 'r') as file:
     reglas = json.load(file)
     
formula += regla_2
formula += regla_3
formula += regla_4
formula += reglas
print("Reglas importadas")


print("Ejecutando DPLL...")
interp_verdaderas = dp.DPLL(formula, interp_verdaderas)[1]
print("Modelo hallado")

print(f"Guardando a archivo {archivo}...")
with open(archivo + '_sol.json', 'w') as outfile:
    json.dump(interp_verdaderas, outfile)
print("Terminado!")

with open(archivo + '_sol.json', 'r') as file:
     interp_verdaderas = json.load(file)

print("Eliminando letras adicionales")
interp_verdaderas = {ord(i)-256:interp_verdaderas[i] for i in interp_verdaderas if i in letrasProposicionales}
print("Letras adicionales eliminadas")

print(len(interp_verdaderas))

vs.dibujar_tablero(interp_verdaderas, Nfilas, Ncolumnas, Nturnos, archivo)


print(f"Guardando a archivo {archivo}...")
with open(archivo + '_sol.json', 'w') as outfile:
    json.dump(interp_verdaderas, outfile)
print("Terminado!")