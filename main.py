import random

import pygame

pygame.init()

# Variables Importantes
x = 50
y = 50
ancho = 10
alto = 10
cantFilas = 30
cantColumnas = 30
anchoVentana = 600
altoVentana = 600
segundosDelay = 1

ventana = pygame.display.set_mode((anchoVentana, altoVentana))

pygame.display.set_caption("Primer Juego")

run = True
while run:
    pygame.time.delay(segundosDelay * 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos()
    print(mouse)

    numeroCuadrado = 0

    # Generar matriz de cuadrados
    for i in range(0, cantColumnas):
        for j in range(0, cantFilas):

            print(numeroCuadrado)

            # random.randrange(256)
            pygame.draw.rect(ventana,
                             (255, 255, 255),  # Color
                             (x + i * (ancho + 3), y + j * (alto + 3), ancho, alto))  # posx, posy, ancho, alto
            numeroCuadrado += 1

    # Actualizar display
    pygame.display.update()

pygame.quit()
