#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

##################################Variables globales#######################################################
letrasProposicionales=[chr(x) for x in range(256, 2706)]        #Va de 256 hasta la letra 2450: la ultima
Conectivos = ['O','Y','>','=']                                  #Lista de conectivos para inorder
negacion = ["-"]                                                #Negacion para inorder
###########################################################################################################

#Arbol para guardar las formulas
class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
    
    #Conversion del arbol a forma inorderr
    def inorder(self):
        if self.label in letrasProposicionales:
            return self.label
        elif self.label in negacion:
            return  self.label + self.right.inorder()
        elif self.label in Conectivos:
            return "(" + self.left.inorder() + self.label + self.right.inorder() + ")"
        else:
            print("Rotulo incorrecto")
            sys.exit(1)
        
        
#Funcion que convierte un string en polaca inversa a arbol. Recibe:
#Formula en polaca inversa a convertir: A
def String2Tree(A):
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo {0} no se reconoce".format(c))
    return Pila[-1]

#Convierte un arbol a notación inorder. Recibe:
#Arbol de formula: f
#Numero de filas: Nf, numero de columnas: Nc y numero de turnos: Nt, como enteros
def Inorderp(f, Nf, Nc, Nt):
    if f.right == None:
        if ord(f.label) - 256 >= 49:
            return str(Pinv(ord(f.label) - 256 - 49, Nf, Nc, Nt))
        else:
            return str(decodifica(ord(f.label) - 256, Nf, Nc))
    elif f.label == '-':
        return f.label + Inorderp(f.right, Nf, Nc, Nt)
    else:
        return "(" + Inorderp(f.left, Nf, Nc, Nt) + f.label + Inorderp(f.right, Nf, Nc, Nt) + ")"
    
#Pide posicion inicial y final al usuario. Recibe:
#Numero de filas: Nf y Numero de columnas: Nc como enteros
def inicio_final(Nf, Nc):
    #pide inicio
    print("\nPosicion inicial:")
    f = int(input("Inserte la fila: "))
    assert(f >= 0 and f <= Nf - 1), ("Fila invalida, debe ser un numero entre 0 y " + str(Nf - 1)
                                            + "\nse recibio " + str(f))
    c = int(input("Inserte la columna: "))
    assert(c >= 0 and f <= Nc - 1), ("Columna invalida, debe ser un numero entre 0 y " + str(Nc - 1)
                                            + "\nse recibio " + str(c))
    inicio = (f, c)

    #Pide final
    print("\nPosicion final:")
    f = int(input("Inserte la fila: "))
    assert(f >= 0 and f <= Nf - 1), ("Fila invalida, debe ser un numero entre 0 y " + str(Nf)
                                            + "\nse recibio " + str(f))
    c = int(input("Inserte la columna: "))
    assert(c >= 0 and f <= Nc - 1), ("Columna invalida, debe ser un numero entre 0 y " + str(Nc)
                                            + "\nse recibio " + str(c))
    final = (f, c)
    return inicio, final

#Codifica dos valores en un numero. Recibe:
#valor 1: f, valor 2: c, maximos del primer valor: Nc y del segundo valor: Nf como enteros
def codifica(f, c, Nf, Nc):
    #Nos aseguramos que los valores esten en el rango
    assert((f >= 0) and (f <= Nf - 1)), ("Primer argumento incorrecto! Debe ser un numero entre 0 y " 
                                          + str(Nf - 1) + "\n se recibio" + str(f))
    assert((c >= 0) and (c <= Nc - 1)), ("Segundo argumento incorrecto! Debe ser un numero entre 0 y " 
                                          + str(Nc - 1) + "\n se recibio" + str(c))
    #codificamos
    val = Nc * f + c
    return val

#Decodifica un codigo en 2 valores. Recibe
#Codigo a decodificar: n, valores maximos para el primer numero: Nf y para el segundo numero: Nc como enteros
def decodifica(n, Nf, Nc):
    #Nos aseguramos que el valor este en el rango
    assert((n >= 0) and (n <= Nf * Nc - 1)), ("Primer argumento incorrecto! Debe ser un numro entre 0 y " 
                                              + str(Nf * Nc -1) + "\n se recibio" + str(n))
    #decodificamos
    f = n // Nc
    c = n % Nc
    return f, c

#Codifica 3 elementos, recibe:
#valor 1: f, valor 2: c, , valor 3: t, maximos del primer valor: Nc, del segundo valor: Nf y del tercer valor: Nt como enteros
def P(f, c, t, Nf, Nc, Nt):
    #nos aseguramos de que el valor este en el rango
    assert((f >= 0) and (f <= Nf - 1)), ("Primer argumento incorrecto! Debe ser un numero entre 0 y " 
                                          + str(Nf - 1) + "\n se recibio" + str(f))
    assert((c >= 0) and (c <= Nc - 1)), ("Segundo argumento incorrecto! Debe ser un numero entre 0 y " 
                                          + str(Nc - 1) + "\n se recibio" + str(c))
    assert((t >= 0) and (t <= Nt - 1)), ("Tercer argumento incorrecto! Debe ser un numero entre 0 y " 
                                          + str(Nt - 1) + "\n se recibio" + str(t))
    #codificamos
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(t, v1, Nt, Nf*Nc) + Nf*Nc
    codigo = chr(v2 + 256)
    return codigo

#Decodifica un codigo en 3 valores, recibe:
#Codigo a decodificar: n, valores maximos para el primer numero: Nf, para el segundo numero: Nc y para el tercer numero: Nt como enteros
def Pinv(n, Nf, Nc, Nt):
    #Nos aseguramos de que los valores esten en la cuadricula
    assert((n >= 0 and n <= Nf * Nc * Nt - 1)), ("Primer argumento incorrecto! Debe ser un numero entre 0 y "
                                                  + str(Nf * Nc * Nt - 1) + "\n se recibio " + str(n))
    t, v1 = decodifica(n, Nf * Nc, Nt)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, t


#Condiciones iniciales, tomadas de una lista de muros, recibe
#Lista de casillas en las que hay muros: M
#Numero de filas: Nf, Numero de columnas: Nc
def cond_inicial(M, Nf, Nc):
    inicial = True
    r = ""
    for f in range(Nf):
        for c in range(Nc):
            if(f, c) in M:
                if inicial:
                    code = chr(codifica(f, c, Nf, Nc) + 256)
                    r += code
                    inicial = False
                else:
                    code = chr(codifica(f, c, Nf, Nc) + 256)
                    r += code + "Y"
            else:
                if inicial:
                    code = chr(codifica(f, c, Nf, Nc) + 256)
                    r += code + "-"
                    inicial = False
                else:
                    code = chr(codifica(f, c, Nf, Nc) + 256)
                    r += code + "-" + "Y"
    return r


#Primera regla: debe iniciar en una casilla dada y terminar en una casilla dada, recibe:
#Inicio: i y final: f como tuplas de forma (fila, columna)
#Numero de turnos: Nt numero de filas: Nf y numero de columnas: Nc como enteros
def regla_1(i, f, Nf, Nc, Nt):
    r1 = ""
    r1 += P(i[0], i[1], 0, Nf, Nc, Nt)
    r1 += P(f[0], f[1], Nt - 1, Nf, Nc, Nt) + "Y"
    return r1


#Segunda regla: El agente no puede estar en 2 puntos a la vez, recibe:
#Numero de filas: Nf, Numero de columnas: Nc y Numero de turnos: Nt como enteros
def regla_2(Nf, Nc, Nt):
    r2 = ""
    inicial_3 = True
    for t in range(Nt):
        inicial_2 = True
        for i in range(Nf):
            for j in range(Nc):
                inicial = True
                for f in range(Nf):
                    for c in range(Nc):
                        if f == i and c == j:
                            end = "-" + P(f, c, t, Nf, Nc, Nt) + ">"
                        elif inicial:
                            r2 += P(f, c, t, Nf, Nc, Nt)
                            inicial = False
                        else:
                            r2 += P(f, c, t, Nf, Nc, Nt) + "O"
                r2 += end
                if inicial_2:
                    inicial_2 = False
                else:
                    r2 += "Y"
        if inicial_3:
            inicial_3 = False
        else:
            r2 += "Y"
    return r2

#Tercera regla: El jugador no puede estar parado en una pared. Recibe
#Numero de filas: Nf, Numero de columnas: Nc y Numero de turnos: Nt como enteros
def regla_3(Nf, Nc, Nt):
    r3 = ""
    inicial_2 = True
    for f in range(Nf):
        for c in range(Nc):
            inicial = True
            for t in range(Nt):
                if inicial:
                    r3 += P(f, c, t, Nf, Nc, Nt)
                    inicial = False
                else:
                    r3 += P(f, c, t, Nf, Nc, Nt) + "O"
            if inicial_2:
                r3 += "-" + chr(codifica(f, c, Nf, Nc) + 256) + ">"
                inicial_2 = False
            else:
                r3 += "-" + chr(codifica(f, c, Nf, Nc) + 256) + ">" + "Y"
    return r3

#Cuarta regla: El jugador solo se puede mover una casilla por turno, hacia arriba, abajo, izquierda o derecha. Recibe
#Numero de filas: Nf, Numero de columnas: Nc y Numero de turnos: Nt como enteros
def regla_4(Nf, Nc, Nt):
    r4 = ""
    inicial_3 = True
    for t in range(Nt - 1):    
        inicial_2 = True
        for i in range(Nf):
            for j in range(Nc):       
                inicial = True
                #Lista de adyacencia para el movimiento
                #Si la casilla es una columna
                if i == 0 and j == 0:
                    adj = [(i + 1, j), (i, j + 1)]
                elif i == 0 and j == Nc - 1:
                    adj = [(i + 1, j), (i, j - 1)]
                elif i == Nf - 1 and j == 0:
                    adj = [(i - 1, j), (i, j + 1)]
                elif i == Nf - 1 and j == Nc - 1:
                    adj = [(i - 1, j), (i, j - 1)]
                    #Si la casilla esta en un borde
                elif i == 0:
                    adj = [(i + 1, j), (i, j - 1), (i, j + 1)]
                elif i == Nf - 1:
                    adj = [(i - 1, j), (i, j - 1), (i, j + 1)]
                elif j == 0:
                    adj = [(i - 1, j), (i + 1, j), (i, j + 1)]
                elif j == Nc - 1:
                    adj = [(i - 1, j), (i + 1, j), (i, j - 1)]
                #Si se puede mover en todo sentido
                else:
                    adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for (f, c) in adj:
                    if inicial:
                        r4 += P(f, c, t + 1, Nf, Nc, Nt) 
                        inicial = False
                    else:
                        r4 += P(f, c, t + 1, Nf, Nc, Nt) + "O"
                if inicial_2:
                    r4 += P(i, j, t, Nf, Nc, Nt) + ">"
                    inicial_2 = False
                else:
                    r4 += P(i, j, t, Nf, Nc, Nt) + ">" + "Y"
        if inicial_3:
            inicial_3 = False
        else:
            r4 += "Y"
    return r4
        
#Quinta regla: Una vez el agente llegue a la ultima casilla, no se movera de ella. Recibe:
#casilla final: f como tupla de forma (fila, columna)
#Numero de filas: Nf, Numero de columnas: Nc y Numero de turnos: Nt como enteros
def regla_5(f, Nf, Nc, Nt):
    r5 = ""
    inicial_2 = True
    for i in range(Nt - 1):
        inicial = True
        for t in range(i + 1, Nt):
            if inicial:
                r5 += P(f[0], f[1], t, Nf, Nc, Nt) 
                inicial = False
            else:
                r5 += P(f[0], f[1], t, Nf, Nc, Nt) + "Y"
        if inicial_2:
            r5 += P(f[0], f[1], i, Nf, Nc, Nt) + ">"
            inicial_2 = False
        else:
            r5 += P(f[0], f[1], i, Nf, Nc, Nt) + ">" + "Y"
        
    return r5
