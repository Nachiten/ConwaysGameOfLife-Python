import pygame

pygame.init()


# Funciones
def vecinosVivosdDe(matriz, posicion):
    posFila = posicion[0]
    posCol = posicion[1]

    cantVivas = 0

    # print("posFila: " + str(posFila) + " posCol: " + str(posCol))

    for unaFilaFuncion in range(posFila - 1, posFila + 2):
        for unaColFuncion in range(posCol - 1, posCol + 2):
            # print("Fila: " + str(unaFilaFuncion) + " Columna: " + str(unaColFuncion))
            if (unaFilaFuncion < 0) | (unaFilaFuncion >= cantFilas) | \
               (unaColFuncion < 0) | (unaColFuncion >= cantColumnas) | \
               ((unaFilaFuncion == posFila) & (unaColFuncion == posCol)):
                continue
            if matriz[unaFilaFuncion][unaColFuncion] == 1:
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
cantFilas = 60
cantColumnas = 60
# Configuracion
anchoVentana = 800
altoVentana = 800
segundosDelay = 1

ventana = pygame.display.set_mode((anchoVentana, altoVentana))

pygame.display.set_caption("Primer Juego")

bloquesGrises = [(2, 2), (2, 4), (25, 29), (0, 0), (0, 1), (0, 2), (1, 1),
                 (1, 0), (15, 16), (15, 17), (15, 18), (15, 19), (16, 16), (16, 17), (16, 18), (16, 19), (17, 16), (17, 17), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (17, 26)]

matrizVieja = [[0 for a in range(cantFilas)] for b in range(cantColumnas)]
matrizNueva = [[0 for a in range(cantFilas)] for b in range(cantColumnas)]

run = True

primeraVuelta = True

while run:
    pygame.time.delay(segundosDelay * 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Generar matriz de cuadrados
    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):

            colores = (100, 100, 100)

            if primeraVuelta:
                for (unaFila, unaCol) in bloquesGrises:
                    if (laFila == unaFila) & (laColumna == unaCol):
                        colores = (255, 255, 255)
                        matrizVieja[laFila][laColumna] = 1
                        break
                    else:
                        matrizVieja[laFila][laColumna] = 0
            else:
                if matrizVieja[laFila][laColumna] == 1:
                    colores = (255, 255, 255)

            # random.randrange(256)
            pygame.draw.rect(ventana,
                             colores,  # Color
                             (x + laColumna * (ancho + 3), y + laFila * (alto + 3), ancho,
                              alto))  # posx, posy, ancho, alto

    primeraVuelta = False

    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            # La celda está viva
            if matrizVieja[laFila][laColumna] == 1:
                if (vecinosVivosdDe(matrizVieja, (laFila, laColumna)) == 2) | \
                   (vecinosVivosdDe(matrizVieja, (laFila, laColumna)) == 3):
                    matrizNueva[laFila][laColumna] = 1
                else:
                    matrizNueva[laFila][laColumna] = 0
            # La celda está muerta
            else:
                if vecinosVivosdDe(matrizVieja, (laFila, laColumna)) == 3:
                    matrizNueva[laFila][laColumna] = 1
                else:
                    matrizNueva[laFila][laColumna] = 0

    # print("Vecinos vivos de 15,16: " + str(vecinosVivosdDe(matrizVieja, (16, 17))))

    '''
    print("Matriz vieja: ")

    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            print(matrizVieja[laFila][laColumna], end="")
        print("")

    print("Matriz nueva: ")

    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            print(matrizNueva[laFila][laColumna], end="")
        print("")
    '''

    # Pasar todos los datos de la matriz nueva a la vieja para repetir ciclo
    for laFila in range(0, cantColumnas):
        for laColumna in range(0, cantFilas):
            matrizVieja[laFila][laColumna] = matrizNueva[laFila][laColumna]

    # mouse = pygame.mouse.get_pos()
    # print(mouse)

    # Actualizar display
    pygame.display.update()

pygame.quit()
