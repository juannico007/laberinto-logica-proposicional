#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
    

#Crea un laberinto de dimensiones n * m conectado, con 2 casillas que nunca tendran un muro en ella. Recibe:
#Dimensiones del tablero, f = filas, c = columnas como enteros, tamaño por defecto 7x7
#Caisllas de inicio y final como tuplas
def create_maze(start, end, c = 7, f = 7):
    sets = []
    board = np.zeros((f,c))
    keep = []
    for y in range(f):
        muros = []
        n_muros = random.randint(c//3, c//2)
        
        #Coloco los muros en la fila respectiva
        j = 0
        it = 0
        while j < n_muros and it < 30:
            x = random.randint(0, c - 1)
            if (y, x) != start and (y, x) != end and board[y, x] != -1 and (y,x) not in keep:
                muros.append(x)
                board[y, x] = -1
                j += 1
            it += 1
        muros.sort()

        #Junto las casillas adyacentes de la fila sin muro en un set
        set_c = []
        for i in range(len(muros)):
            if i == 0:
                set_c.append({(y, x) for x in range(muros[i])})
            if i == len(muros) - 1:
                set_c.append({(y, x) for x in range(muros[i] + 1, c)})
            else:
                set_c.append({(y, x) for x in range(muros[i] + 1, muros[i + 1])})
                
        set_c = [x for x in set_c if x]
        
        #Establezco las casillas que se extienden hacia abajo
        if y < f - 1:
            keep = []
            for s in set_c:
                nxt = set()
                stuck = True
                while stuck:
                    for cas in s:
                        down = random.randint(1, len(s))
                        if down == 1:
                            keep.append((y + 1, cas[1]))
                            nxt.add((y + 1, cas[1]))
                            stuck = False
                        if(len(nxt) >= len(s) / 2):
                            break
                    s.update(nxt)
        
        #print(set_c)
        #Coloco los primeros conjuntos en el arreglo
        if y == 0:
            sets.append(set_c)
            
        #Junto las casillas adyacentes en un solo conjunto
        #Verticalmente
        if y > 0:
            #Junto lo que no este aun en el conjunto
            while len(set_c) > 0:
                s = set_c.pop(0)
                found = False
                for i in sets[0]:
                    for (a,b) in s:
                        if (a,b) in i or (a - 1, b) in i:
                            found = True
                            temp = s.union(i)
                            sets[0].remove(i)
                            sets[0].append(temp)
                            break
                if not found:
                    sets[0].append(s)
            #Reviso en el conjunto
            temp = sets[0][:]
            sets[0] = []
            stack = []
            notdisj = False
            while len(temp) > 0:
                if not notdisj:
                    stack.append(temp.pop(0))
                notdisj = False
                for i in temp:
                    if not stack[0].isdisjoint(i):
                        notdisj = True
                        stack.append(i)
                for i in stack:
                    if i in temp:
                        temp.remove(i)
                if notdisj:
                    temp2 = set()
                    for i in stack:
                        temp2 = temp2.union(i)
                    stack = [temp2]
                    if len(temp) == 0:   
                        notdisj = False
                        sets[0].append(stack.pop())
                else:
                    sets[0].append(stack.pop())
        
        if y == f - 1:
            ll = []
            for s in sets[0]:
                for ca in s:
                    if ca[0] == y:
                        ll.append(ca[1])
            ll.sort()
            mini = ll[0]
            maxi = ll[-1]
            set_c = set()
            for x in range(mini, maxi + 1):
                board[y, x] = 0
                set_c.add((y, x))
            
            sets[0].append(set_c)
            #Reviso en el conjunto
            temp = sets[0][:]
            sets[0] = []
            stack = []
            notdisj = False
            while len(temp) > 0:
                if not notdisj:
                    stack.append(temp.pop(0))
                notdisj = False
                for i in temp:
                    if not stack[0].isdisjoint(i):
                        notdisj = True
                        stack.append(i)
                for i in stack:
                    if i in temp:
                        temp.remove(i)
                if notdisj:
                    temp2 = set()
                    for i in stack:
                        temp2 = temp2.union(i)
                    stack = [temp2]
                    if len(temp) == 0:   
                        notdisj = False
                        sets[0].append(stack.pop())
                else:
                    sets[0].append(stack.pop())
            
            walls = []
            for i in range(f):
                for j in range(c):
                    if (i,j) not in sets[0][0]:
                        walls.append((i, j))
                        
    return walls