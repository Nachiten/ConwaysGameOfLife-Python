import pygame
from datetime import datetime


# Funciones
def hacerUnLog(unString):
    # Dia y hora actuales
    fecha = datetime.now()
    print(str(fecha.timetuple()[3]) + ":"
          + str(fecha.timetuple()[4]) + ":"
          + str(fecha.timetuple()[5]) + " " + unString)


def printearMatrizNueva():
    hacerUnLog("Matriz nueva: ")
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):
            print(matrizNueva[filaFuncion][columnaFuncion], end="")
        hacerUnLog("")


def printearMatrizVieja():
    hacerUnLog("Matriz vieja: ")
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):
            print(matrizVieja[filaFuncion][columnaFuncion], end="")
        hacerUnLog("")


def vecinosVivosdDe(matriz, posicion):
    posFila = posicion[0]
    posCol = posicion[1]

    cantVivas = 0

    for filaFuncion in range(posFila - 1, posFila + 2):
        for colFuncion in range(posCol - 1, posCol + 2):
            if (filaFuncion < 0) | (filaFuncion >= cantFilas) | \
                    (colFuncion < 0) | (colFuncion >= cantColumnas) | \
                    ((filaFuncion == posFila) & (colFuncion == posCol)):
                continue
            if matriz[filaFuncion][colFuncion] == 1:
                cantVivas += 1

    return cantVivas


def mostrarMatrizNueva():
    # Generar matriz de cuadrados
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):

            colores = colorMuerto

            if matrizNueva[filaFuncion][columnaFuncion] == 1:
                colores = colorVivo

            dibujarRectangulo(colores, columnaFuncion, filaFuncion)
    # hacerUnLogearMatrizNueva()


def dibujarRectangulo(colores, columna, fila):
    pygame.draw.rect(ventana,
                     colores,  # Color
                     (x + columna * (ancho + 3), y + fila * (alto + 3), ancho,
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


def generarMatrizVieja():
    # Generar matriz de cuadrados
    for filaFuncion in range(0, cantFilas):
        for columnaFuncion in range(0, cantColumnas):

            colores = colorMuerto

            # Evaluar las posiciones de los bloques iniciales
            for (unaFila, unaCol) in bloquesGrises:
                if (filaFuncion == unaFila) & (columnaFuncion == unaCol):
                    colores = colorVivo
                    matrizVieja[filaFuncion][columnaFuncion] = 1
                    break
                else:
                    matrizVieja[filaFuncion][columnaFuncion] = 0

            dibujarRectangulo(colores, columnaFuncion, filaFuncion)


def pasarMatrizNuevaAVieja():
    # Pasar todos los datos de matrizNueva a matrizVieja para repetir ciclo
    for laFila in range(0, cantFilas):
        for laColumna in range(0, cantColumnas):
            matrizVieja[laFila][laColumna] = matrizNueva[laFila][laColumna]


def manejarPausa(estaPausado):
    radioCirculo = 20
    anchoCirculo = 10

    while True:
        for unEvento in pygame.event.get():
            if unEvento.type == pygame.KEYDOWN:
                estaPausado = not estaPausado
                hacerUnLog("El estado de PAUSA es: " + str(estaPausado))
            if unEvento.type == pygame.QUIT:
                pygame.quit()
            if unEvento.type == pygame.MOUSEBUTTONDOWN:
                modificarCelda(pygame.mouse.get_pos())
                clickearBotonCeleste(pygame.mouse.get_pos())
                clickearBotonNaranja(pygame.mouse.get_pos())

        if not estaPausado:
            # NO está en pausa
            generarCirculo((50, 255, 50), radioCirculo, anchoCirculo)
            return estaPausado

        # SI está en pausa
        generarCirculo((255, 40, 40), radioCirculo, anchoCirculo)

        # Actualizar display
        pygame.display.update()

        pygame.time.delay(200)


def generarCirculo(color, radio, grosor):
    pygame.draw.circle(ventana, color, (anchoVentana - 35, 50), radio, grosor)


def modificarCelda(unaPos):
    posX = unaPos[0]
    posY = unaPos[1]

    for laFila in range(0, cantFilas):
        for laColumna in range(0, cantColumnas):
            posXEsperada = x + laColumna * (ancho + 3)
            posYEsperada = y + laFila * (alto + 3)
            if posXEsperada < posX < posXEsperada + ancho and posYEsperada < posY < posYEsperada + alto:
                hacerUnLog("Tocaste un cuadrado: Fila: " + str(laFila) + " Columna:" + str(laColumna))
                if matrizVieja[laFila][laColumna] == 1:
                    matrizVieja[laFila][laColumna] = 0
                    dibujarRectangulo(colorMuerto, laColumna, laFila)
                else:
                    matrizVieja[laFila][laColumna] = 1
                    dibujarRectangulo(colorVivo, laColumna, laFila)
                return


def escribirArchivo():  # Prueba
    with open('matriz.txt', 'w') as archivo:
        for laFila in range(0, cantFilas):
            for laColumna in range(0, cantColumnas):
                archivo.write("%i " % matrizVieja[laFila][laColumna])
            archivo.write("\n")


def leerArchivo():
    with open('matriz.txt', 'r') as archivo:
        lineas = archivo.readlines()

        matrizLeidaArchivo = [[0 for vx in range(cantFilas)] for vy in range(cantColumnas)]

        cantLineas = 0
        for unaLinea in lineas:
            listaNums = obtenerListaNums(unaLinea)

            cantNumeros = 0
            for unNumero in listaNums:
                matrizLeidaArchivo[cantLineas][cantNumeros] = unNumero
                cantNumeros += 1
            cantLineas += 1

    '''
    for laFila in range(0, cantFilas):
        for laColumna in range(0, cantColumnas):
            print(matrizLeidaArchivo[laFila][laColumna], end=" ")
        print("")
    '''


def obtenerListaNums(unaLinea):
    listaNums = []

    for unCaracter in unaLinea:
        if unCaracter == '0' or unCaracter == '1':
            listaNums.append(unCaracter)

    return listaNums


def generarBotonCeleste():
    pygame.draw.rect(ventana, (50, 200, 200), (anchoVentana - 60, 100, 50, 35))


def clickearBotonCeleste(unaPos):
    posX = unaPos[0]
    posY = unaPos[1]

    if anchoVentana - 60 < posX < anchoVentana - 10 and 100 < posY < 135:
        escribirArchivo()
        hacerUnLog("Clickeaste boton celeste")


def generarBotonNaranja():
    pygame.draw.rect(ventana, (255, 165, 0), (anchoVentana - 60, 155, 50, 35))


def clickearBotonNaranja(unaPos):
    posX = unaPos[0]
    posY = unaPos[1]

    if anchoVentana - 60 < posX < anchoVentana - 10 and 155 < posY < 190:
        escribirArchivo()
        hacerUnLog("Clickeaste boton naranja")


pygame.init()

# Comienza ejecucion

# Variables Importantes [Globales]
# Posicion Bloques
x = 20
y = 20
# Tamaño bloques
ancho = 7
alto = 7
# Matriz
cantFilas = 80  # Default 60 # fixear problema con rectangulos
cantColumnas = 80
# Configuracion
anchoVentana = 1000  # Default 900x900
altoVentana = 1000
segundosDelay = 1
run = True
estaEnPausa = True
colorMuerto = (50, 50, 50)
colorVivo = (255, 50, 50)

pygame.display.set_caption("El juego de la vida de Conway")

bloquesGrises = [(2, 2), (2, 4), (25, 29), (25, 28), (25, 27), (25, 26), (25, 25), (0, 0), (0, 1), (0, 2), (1, 1),
                 (1, 0), (15, 16), (15, 17), (15, 18), (15, 19), (16, 16), (16, 17), (16, 18), (16, 19), (17, 16),
                 (17, 17), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (17, 26)]

cantBloques = 1
desde = 30

for unaFila in range(0, cantColumnas):

    if 10 < unaFila < 20:

        for unBloque in range(desde, cantBloques + desde):
            bloquesGrises.append((unaFila, unBloque))

        cantBloques += 1

matrizVieja = [[0 for vx in range(cantFilas)] for vy in range(cantColumnas)]
matrizNueva = [[0 for nx in range(cantFilas)] for ny in range(cantColumnas)]

# Setup Inicial
ventana = pygame.display.set_mode((anchoVentana, altoVentana))

generarMatrizVieja()
pygame.display.update()

leerArchivo()

generarBotonCeleste()
generarBotonNaranja()

# Bucle infinito
while run:

    estaEnPausa = manejarPausa(estaEnPausa)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            modificarCelda(pygame.mouse.get_pos())
            clickearBotonCeleste(pygame.mouse.get_pos())
            clickearBotonNaranja(pygame.mouse.get_pos())
            continue

    generarMatrizNueva()

    pasarMatrizNuevaAVieja()

    mostrarMatrizNueva()

    # Actualizar display
    pygame.display.update()

    pygame.time.delay(segundosDelay * 300)

pygame.quit()
