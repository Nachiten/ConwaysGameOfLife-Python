import pygame

pygame.init()


# Funciones
def vecinosVivosdDe(matriz, posicion):
    posFila = posicion[0]
    posCol = posicion[1]

    cantVivas = 0

    # print("posFila: " + str(posFila) + " posCol: " + str(posCol))

    for filaFuncion in range(posFila - 1, posFila + 2):
        for colFuncion in range(posCol - 1, posCol + 2):
            # print("Fila: " + str(filaFuncion) + " Columna: " + str(colFuncion))
            if (filaFuncion < 0) | (filaFuncion >= cantFilas) | \
                    (colFuncion < 0) | (colFuncion >= cantColumnas) | \
                    ((filaFuncion == posFila) & (colFuncion == posCol)):
                continue
            if matriz[filaFuncion][colFuncion] == 1:
                cantVivas += 1

    return cantVivas


def printearMatrices():
    print("Matriz vieja: ")

    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):
            print(matrizVieja[filaFuncion][columnaFuncion], end="")
        print("")

    print("Matriz nueva: ")

    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):
            print(matrizNueva[filaFuncion][columnaFuncion], end="")
        print("")


def generarMatrizVieja():
    # Generar matriz de cuadrados
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):

            colores = (100, 100, 100)

            if matrizVieja[filaFuncion][columnaFuncion] == 1:
                colores = (255, 255, 255)

            # random.randrange(256)
            pygame.draw.rect(ventana,
                             colores,  # Color
                             (x + columnaFuncion * (ancho + 3), y + filaFuncion * (alto + 3), ancho,
                              alto))  # posx, posy, ancho, alto


def generarMatrizPrimeraVez():
    # Generar matriz de cuadrados
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):

            colores = (100, 100, 100)

            for (unaFila, unaCol) in bloquesGrises:
                if (filaFuncion == unaFila) & (columnaFuncion == unaCol):
                    colores = (255, 255, 255)
                    matrizVieja[filaFuncion][columnaFuncion] = 1
                    break
                else:
                    matrizVieja[filaFuncion][columnaFuncion] = 0

            pygame.draw.rect(ventana,
                             colores,  # Color
                             (x + columnaFuncion * (ancho + 3), y + filaFuncion * (alto + 3), ancho,
                              alto))  # posx, posy, ancho, alto


def generarMatrizNueva():
    # Generar matrizNueva (basandose en datos de matrizVieja)
    for laFila in range(0, cantFilas):
        for laColumna in range(0, cantColumnas):
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


def pasarMatrizNuevaAVieja():
    # Pasar todos los datos de matrizNueva a matrizVieja para repetir ciclo
    for laFila in range(0, cantFilas):
        for laColumna in range(0, cantColumnas):
            matrizVieja[laFila][laColumna] = matrizNueva[laFila][laColumna]


def manejarPausa(estaPausado, estaCorriendo):
    # if not estaPausado:
    # print("NO esta en pausa")

    radioCirculo = 20
    anchoCirculo = 10

    while True:
        pygame.time.delay(200)
        for unEvento in pygame.event.get():
            if unEvento.type == pygame.KEYDOWN:
                estaPausado = not estaPausado

        if not estaPausado:
            pygame.draw.circle(ventana, (0, 255, 0), (850, 50), radioCirculo, anchoCirculo)
            return estaPausado
        # print("SI esta en pausa")

        pygame.draw.circle(ventana, (255, 0, 0), (850, 50), radioCirculo, anchoCirculo)

        # Actualizar display
        pygame.display.update()


# Variables Importantes [Globales]
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
anchoVentana = 900
altoVentana = 900
segundosDelay = 1
run = True
estaEnPausa = True

pygame.display.set_caption("El juego de la vida de Conway")

bloquesGrises = [(2, 2), (2, 4), (25, 29), (25, 28), (25, 27), (25, 26), (25, 25), (0, 0), (0, 1), (0, 2), (1, 1),
                 (1, 0), (15, 16), (15, 17), (15, 18), (15, 19), (16, 16), (16, 17), (16, 18), (16, 19), (17, 16),
                 (17, 17), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (17, 26)]

matrizVieja = [[0 for vx in range(cantFilas)] for vy in range(cantColumnas)]
matrizNueva = [[0 for nx in range(cantFilas)] for ny in range(cantColumnas)]

# Setup Inicial
ventana = pygame.display.set_mode((anchoVentana, altoVentana))

generarMatrizPrimeraVez()
pygame.display.update()


# Bucle infinito
while run:

    estaEnPausa = manejarPausa(estaEnPausa, run)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    generarMatrizVieja()

    generarMatrizNueva()

    pasarMatrizNuevaAVieja()

    # Actualizar display
    pygame.display.update()

    pygame.time.delay(segundosDelay * 200)

pygame.quit()

'''
# mouse = pygame.mouse.get_pos()
# print(mouse)

for unEvento in pygame.event.get():
    if unEvento.type == pygame.QUIT:
        estaCorriendo = False
'''
