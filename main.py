import pygame

pygame.init()


# Funciones
def vecinosVivosdDe(matriz, posicion):

    posFila = posicion[0]
    posCol = posicion[1]

    cantVivas = 0

    for unaFila in range(posFila - 1, posFila + 2):
        for unaCol in range(posCol - 1, posCol + 2):
            # print("Analizando la fila: " + str(unaFila) + " Y la columna: " + str(unaCol))
            if (unaFila < 0) | (unaFila >= cantFilas) | (unaCol < 0) | (unaCol >= cantColumnas) | \
                    ((unaFila == posFila) & (unaCol == posCol)):
                continue
            if matriz[unaFila][unaCol] == 1:
                cantVivas += 1

    return cantVivas


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

bloquesGrises = [(2, 2), (2, 4), (15, 15), (25, 29), (0, 0), (0, 1), (0, 2), (1, 1), (1,0)]

matrizVieja = [[0 for a in range(cantFilas)] for b in range(cantColumnas)]
matrizNueva = [[0 for a in range(cantFilas)] for b in range(cantColumnas)]

run = True

while run:
    pygame.time.delay(segundosDelay * 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Generar matriz de cuadrados
    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):

            colores = (100, 100, 100)

            for (unaFila, unaCol) in bloquesGrises:
                if (laFila == unaFila) & (laColumna == unaCol):
                    colores = (255, 255, 255)
                    matrizVieja[laFila][laColumna] = 1
                    break
                else:
                    matrizVieja[laFila][laColumna] = 0

            # random.randrange(256)
            pygame.draw.rect(ventana,
                             colores,  # Color
                             (x + laColumna * (ancho + 3), y + laFila * (alto + 3), ancho,
                              alto))  # posx, posy, ancho, alto

    '''
    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            # La celda está viva
            if (matrizVieja[laFila][laFila] == 1):
                if (vecinosVivosdDe(matrizVieja, (0, 0)):
                    hola
            # La celda está muerta
            else:
    '''

    print(vecinosVivosdDe(matrizVieja, (0, 0)))

    '''
    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            print(Matrix[laFila][laColumna], end="")
        print("")
    '''

    mouse = pygame.mouse.get_pos()
    # print(mouse)

    # Actualizar display
    pygame.display.update()

pygame.quit()




