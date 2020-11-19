#!/usr/bin/env python3
# -*- coding: utf-8 -*-

letrasProposicionales = [chr(x) for x in range(256, 1000000)]
#letrasProposicionales = ['p', 'q', 'r', 's', 't']

#Encuentra el complemento de un literal
#Recibe el literal l
def complemento(l):
    if l in letrasProposicionales:
        return '-' + l
    elif l[0] == '-':
        return l[1]
    else:
        #print(f"error, literal invalido {l}")
        raise Exception(f"error, literal invalido {l}")

def hay_unidad(S):
    for i in S:
        if len(i) == 1:
            return i[0]
    return None
    

#Subrutina de unit propagation
#Recibe S: un conjunto de clausulas e I: una interpretación
def unit_propagate(S, I):
    unidad= hay_unidad(S)
    while ([] not in S) and (unidad != None):
        #print(len(S))
        if len(unidad) == 1:
            I[unidad] = 1
        else:
            I[complemento(unidad)] = 0
        S = [c for c in S if unidad not in c]

        comp = complemento(unidad)
        for i in S:
            if comp in i:
                i.remove(comp)
        
        if [] in S:
            return 'Insatisfacible', {}
        
        unidad = hay_unidad(S)
        
    return S, I

def R_DPLL(S, I):
    S, I = unit_propagate(S, I)
    if S == 'Insatisfacible' or [] in S:
        return None
    if S == []:
        return I
    count = {}
    max = [None, 0]
    for i in S:
        for j in i:
            count[j] = count.get(j, 0) + 1
            if count[j] > max[1]:
                max[0] = j
                max[1] = count[j]
                
    Ip = dict.copy(I)             
    unidad = max[0]
    comp = complemento(unidad)
    
    if len(unidad) == 1:
        Ip[unidad] = 1
    else:
        Ip[comp] = 0
    
    Sp = [c[:] for c in S if unidad not in c]

    for i in Sp:
        if comp in i:
            i.remove(comp)
            
    ret = R_DPLL(Sp, Ip)
    if ret != None:
        return ret
    
    Ipp = dict.copy(I)
    if len(unidad) == 1:
        Ipp[unidad] = 0
    else:
        Ipp[comp] = 1
        
    comp = complemento(unidad)
    Spp = [c[:] for c in S if comp not in c]
    
    for i in Spp:
        if unidad in i:
            i.remove(unidad)
            
    return R_DPLL(Spp, Ipp)
            

def DPLL(S, I):
    for unidad in I:
        comp = complemento(unidad)
        if I[unidad] == 1:
            S = [c for c in S if unidad not in c]
            for i in S:
                if comp in i:
                    i.remove(comp)
        else:
            S = [c for c in S if comp not in c]
            for i in S:
                if unidad in i:
                    i.remove(unidad)
        if S == 'Insatisfacible' or [] in S:
            return None
    print("first step done")
    return R_DPLL(S, I)
    
if __name__ == "__main__":
    s = [['p', 'q' , 'r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
    I = {}

    I = DPLL (s, I)
    if I != None:
        print(I)
    else:
        print('Insatisfacible')