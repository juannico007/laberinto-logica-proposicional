print("Importando paquetes...")
import FNC as F
import functions as fn
import json
print("Listo!")

def guardar_polaca(regla_polaca, archivo, letrasProposicionalesA):
    print("Creando arbol...")
    regla_arbol = fn.String2Tree(regla_polaca)
    print("Creando cadena inorder...")
    regla_inorder = regla_arbol.inorder()
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

def guardar_inorder(regla_inorder, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Transformacion de Tseitin...")
    regla_fnc = F.Tseitin(regla_inorder, letrasProposicionalesA, letrasProposicionalesB)
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

def guardar_fnc(regla_fnc, archivo, letrasProposicionalesA, letrasProposicionalesB):
    print("Forma clausal...")
    regla_clausal = F.formaClausal(regla_fnc)
    print(f"Guardando a archivo {archivo}...")
    with open(archivo + '.json', 'w') as outfile:
        json.dump(regla_clausal, outfile)
    print("Terminado!")

#############################
# Las reglas se leen con:
# with open('regla0.json', 'r') as file:
#     reglas = json.load(file)
