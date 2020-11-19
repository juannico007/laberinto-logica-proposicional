#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de laberintos nxm a partir de
# una lista de literales. los primeros nxm literales representan muros en casillas;
# el literal es positivo sii hay un muro en esa casilla.
# los demas literales representan la presencia del agente en esa posicion
# el literal es positivo sii el agente esta en esa casilla en ese turno

# Formato de la entrada: - las letras proposionales seran: 1, ..., 2450;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Require conocer el tamaño de la cuadricula
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(f, n, m, t, a):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, m, ancho y largo de la cuadricula respectivamente
    #   - a, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step_x = 1/m
    step_y = 1/n
    tangulos = []
    
    # Creo los muros del laberinto
    for i in range(n*m):
       if f[i]==1:
           tangulos.append(patches.Rectangle(*[((i % n) * step_x, 1 - (i // n + 1) * step_y), step_x, step_y], facecolor='black'))
       

    #Ubico el inicio
    for i in range(n * m, n * m * 2):
        if f[i] == 1:
            cprev = i % (n * m)
            tangulos.append(patches.Rectangle(*[((cprev % n) * step_x, 1 - (cprev // n + 1) * step_y), step_x, step_y], facecolor='blue'))
    
    #Ubico el final
    for i in range(n * m * t, n * m * (t + 1)):
        if f[i] == 1:
            cf = i % (n * m)
            tangulos.append(patches.Rectangle(*[((cf % n) * step_x, 1 - (cf // n + 1) * step_y), step_x, step_y], facecolor='blue'))
    print(cf)
    # Creo las líneas horizontales del tablero
    for i in range(n):
        locacion = i * step_y
        tangulos.append(patches.Rectangle(*[(0, step_y + locacion), 1, 0.005], facecolor='black'))
        
    # Creo las lineas verticales del tablero
    for i in range(m):
        locacion = i * step_x
        tangulos.append(patches.Rectangle(*[(step_x + locacion, 0), 0.005, 1], facecolor='black'))            
            
    #Coloco las lineas de los pasos
    direc = " "
    for i in range(n * m * 2, n * m * (t + 1)):
        if f[i] == 1:
            c = i % (n * m)
            if c == cprev - 1:
                tangulos.append(patches.Rectangle(*[((cprev % n) * step_x + step_x / 2 + 0.005, 1 - (cprev // n + 1) * step_y + step_y / 2), -step_x, 0.01], facecolor='red'))
                direc = "left"
            if c == cprev - 7:
                tangulos.append(patches.Rectangle(*[((cprev % n) * step_x + step_x / 2, 1 - (cprev // n + 1) * step_y + step_y / 2), 0.01, step_y + 0.005], facecolor='red'))
                direc = "up"
            if c == cprev + 1:
                tangulos.append(patches.Rectangle(*[((cprev % n) * step_x + step_x / 2, 1 - (cprev // n + 1) * step_y + step_y / 2- 0.005), step_x + 0.01, 0.01], facecolor='red'))
                direc = "right"
            if c == cprev + 7:
                tangulos.append(patches.Rectangle(*[((cprev % n) * step_x + step_x / 2, 1 - (cprev // n + 1) * step_y + step_y / 2 + 0.005), 0.01, -step_y - 0.005], facecolor='red'))
                direc = "down"
            if c == cf:
                print("a")
                vertices = []
                if direc == "right":
                    vertices.append(((c % n) * step_x + step_x / 2, 1 - (c // n + 1) * step_y + step_y / 2 + 0.005))
                    vertices.append(((c % n) * step_x + step_x / 4, 1 - (c // n + 1) * step_y + step_y / 3 + 0.005))
                    vertices.append(((c % n) * step_x + step_x / 4, 1 - (c // n + 1) * step_y + 2 * step_y / 3 + 0.005))
                elif direc == "up":
                    vertices.append(((c % n) * step_x + step_x / 2 + 0.005, 1 - (c // n + 1) * step_y + step_y / 2) + 0.01)
                    vertices.append(((c % n) * step_x + step_x / 3 + 0.005, 1 - (c // n + 1) * step_y + step_y / 4) + 0.01)
                    vertices.append(((c % n) * step_x + 2 * step_x / 3 + 0.005, 1 - (c // n + 1) * step_y + step_y / 4) + 0.01)
                elif direc == "left":
                    vertices.append(((c % n) * step_x + step_x / 2, 1 - (c // n + 1) * step_y + step_y / 2+ 0.005))
                    vertices.append(((c % n) * step_x + 3 * step_x / 4, 1 - (c // n + 1) * step_y + step_y / 3 + 0.005))
                    vertices.append(((c % n) * step_x + 3 * step_x / 4, 1 - (c // n + 1) * step_y + 2 * step_y / 3 + 0.005))
                elif direc == "down":
                    vertices.append(((c % n) * step_x + step_x / 2 + 0.005, 1 - (c // n + 1) * step_y + step_y / 2 - 0.01))
                    vertices.append(((c % n) * step_x + step_x / 3 + 0.005, 1 - (c // n + 1) * step_y + 3 * step_y / 4 - 0.01))
                    vertices.append(((c % n) * step_x + 2 * step_x / 3 + 0.005, 1 - (c // n + 1) * step_y + 3 * step_y / 4 - 0.01))
                tangulos.append(patches.Polygon(vertices, color = "red"))
            cprev = c
            
    for t in tangulos:
        axes.add_patch(t)

    
    #plt.show()
    fig.savefig("tablero_" + str(a) + ".png")
 

if __name__ == "__main__":
    f={x:0 for x in range(2450)}    
    muros = [0, 1, 8, 10, 12, 13, 17, 22, 24, 25, 26, 28, 29, 33, 36, 37, 38, 40, 47]
    for i in muros:
        f[i] = 1
    turnos = [80, 128, 170, 212, 254, 296, 346, 396, 452, 508, 558, 608, 664, 720, 776, 2449]
    for i in range(832, 2449, 49):
        turnos.append(i)
    for i in turnos:
        f[i] = 1
    #print(f)

    dibujar_tablero(f, 7, 7, 49, 121)
