#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy

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
        print("up", len(S))
        if len(unidad) == 1:
            I[unidad] = 1
        else:
            I[complemento(unidad)] = 0
        S = [c for c in S if unidad not in c]

        comp = complemento(unidad)
        for i in S:
            if comp in i:
                i.remove(comp)
        
        unidad = hay_unidad(S)
        
    return S, I

def DPLL(S, I):
    print(len(S))
    S, I = unit_propagate(S, I)
    if [] in S:
        print("c muere")
        return "Insatisfacible", {}
    if S == []:
        return "Satisfacible", I
    
    unidad = S[0][0]
                
    Ip = copy.deepcopy(I)     
    comp = complemento(unidad)
    
    if len(unidad) == 1:
        Ip[unidad] = 1
    else:
        Ip[comp] = 0
    
    Sp = [c[:] for c in S if unidad not in c]

    for i in Sp:
        if comp in i:
            i.remove(comp)
            
    ret = DPLL(Sp, Ip)
    if ret[0] == "Satisfacible":
        return "Satisfacible", ret[1]
    
    else:
        Ipp = copy.deepcopy(I)
        if len(unidad) == 1:
            Ipp[unidad] = 0
        else:
            Ipp[comp] = 1
        
        comp = complemento(unidad)
        Spp = [c[:] for c in S if comp not in c]
        
        for i in Spp:
            if unidad in i:
                i.remove(unidad)
            
        return DPLL(Spp, Ipp)
            

if __name__ == "__main__":
    s = [['p', 'q' , 'r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
    I = {}

    I = DPLL(s, I)[1]
    if I != None:
        print(I)
    else:
        print('Insatisfacible')