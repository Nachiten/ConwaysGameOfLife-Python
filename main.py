import random

import pygame

pygame.init()

# Variables Importantes

# Posicion Bloques
x = 20
y = 20
# Tamaño bloques
ancho = 10
alto = 10
# Matriz
cantFilas = 30
cantColumnas = 30
# Configuracion
anchoVentana = 600
altoVentana = 600
segundosDelay = 1

ventana = pygame.display.set_mode((anchoVentana, altoVentana))

pygame.display.set_caption("Primer Juego")

bloquesGrises = [(2, 2), (2, 4), (0, 0), (15, 15), (25, 29)]

Matrix = [[0 for a in range(cantFilas)] for b in range(cantColumnas)]

# Generar matriz de cuadrados
for laFila in range(0, cantColumnas):
    for laColumna in range(0, cantFilas):

        colores = (100, 100, 100)

        for (unaFila, unaCol) in bloquesGrises:
            if (laFila == unaFila) & (laColumna == unaCol):
                colores = (255, 255, 255)
                Matrix[laFila][laColumna] = 1
                break
            else:
                Matrix[laFila][laColumna] = 0

        # random.randrange(256)
        pygame.draw.rect(ventana,
                         colores,  # Color
                         (x + laColumna * (ancho + 3), y + laFila * (alto + 3), ancho, alto))  # posx, posy, ancho, alto

for laFila in range(0, cantColumnas):
    for laColumna in range(0, cantFilas):
        print(Matrix[laFila][laColumna], end="")
    print("")

run = True
while run:
    pygame.time.delay(segundosDelay * 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos()
    # print(mouse)

    # Actualizar display
    pygame.display.update()

pygame.quit()
