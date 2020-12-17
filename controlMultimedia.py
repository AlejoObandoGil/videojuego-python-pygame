import pygame
from random import randint
from pygame.locals import *

from colors import *
from constantes import *
from jugador import *
from niveles import *
from enemigos import *
from vidasHomero import *
from controlFunciones import*
from main import *


# recortar Jugador
def recortarMatriz(s, r1, r2, x, y):
    m = []
    for j in range(r1):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(r2):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro = s.subsurface(i * x, j * y, x, y)  # variable que almacena cada sprite recortado
            ls.append(cuadro)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m

# recortar Jugador
def recortarLista(lista, corte, rango, posSprite, tamañoX):
    for i in range(rango):  # ancho de imagen / 32 pixeles = N sprites filas
        cuadro = corte.subsurface(i * posSprite, 0, posSprite, tamañoX)  # variable que almacena cada sprite recortado
        lista.append(cuadro)  # agregamos esos cuadros a la lista filas
    return lista


# recortar Enemigo
def recortar2(m, s):
    for j in range(8):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(12):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro = s.subsurface(i * 32, j * 32, 32, 32)  # variable que almacena cada sprite recortado
            ls.append(cuadro)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m

class ControlSonido():
    def __init__(self):
        super().__init__()

        # MUSICA
        pygame.mixer.music.load('sonidos/musicaDeFondo/Kevin MacLeod - Monkeys Spinning Monkeys.mp3')
        # (-1 = reproduce siempre, 0.0 = la musica empieza cuando inicia el juego)
        # Efectos de sonido
        self.sonidoCerveza = pygame.mixer.Sound('sonidos/efectosDeSonido/homero_erupto.wav')
        self.sonidoSalto = pygame.mixer.Sound('sonidos/efectosDeSonido/big_jump.wav')
        self.sonidoOuch = pygame.mixer.Sound('sonidos/efectosDeSonido/homero-ouch.wav')
        self.sonidoPausa = pygame.mixer.Sound('sonidos/efectosDeSonido/homeroPausa.wav')
        self.sonidoCaminar = pygame.mixer.Sound('sonidos/efectosDeSonido/homero-caminar.wav')
        self.sonidoMaso = pygame.mixer.Sound('sonidos/efectosDeSonido/kick.wav')
        self.sonidoFuego = pygame.mixer.Sound('sonidos/efectosDeSonido/homero-grito.wav')
        self.sonidoHomeroMuerto = pygame.mixer.Sound('sonidos/efectosDeSonido/homero_borracho.wav')
        self.sonidoAlmas = pygame.mixer.Sound('sonidos/efectosDeSonido/sonidoAlmas.wav')

        self.enemigoMano = pygame.mixer.Sound('sonidos/efectosDeSonido/enemigoMano.wav')
        self.enemigoEsqueleto = pygame.mixer.Sound('sonidos/efectosDeSonido/esqueleto.wav')
        self.enemigoDracula = pygame.mixer.Sound('sonidos/efectosDeSonido/enemigoDracula.wav')

        self.SonidoComenzarJuego = pygame.mixer.Sound('sonidos/efectosDeSonido/homeroFeo.wav')

        self.músicaSonando = False  # el jugador puede desactivar la musica
        self.músicaPausaSonando = False

class ControlSprites():
    def __init__(self):
        super().__init__()
        # IMAGENES DE SPRITE PARA RECORTAR
        self.spriteJugadorCaminar = pygame.image.load(
            'imagenes/Jugador/homer_caminando.png')  # cargamos la imagen con su extension
        self.spriteJugadorCaminarIzq = pygame.image.load(
            'imagenes/Jugador/homer_caminarIzq.png')  # cargamos la imagen con su extension
        self.spriteJugadorSalto = pygame.image.load(
            'imagenes/Jugador/homer_salto1.png')  # cargamos la imagen con su extension
        self.spriteJugadorSaltoIzq = pygame.image.load(
            'imagenes/Jugador/homer_salto1Izq.png')  # cargamos la imagen con su extension
        self.spriteJugadorMaso = pygame.image.load('imagenes/Jugador/homer_maso.png')  # cargamos la imagen con su extension
        self.spriteJugadorMasoIzq = pygame.image.load('imagenes/Jugador/homer_masoIzq2.png')  # cargamos la imagen con su extension

        self.spriteJugadorCaida = pygame.image.load(
            'imagenes/Jugador/homer_caida.png')  # cargamos la imagen con su extension
        self.homeroFrito = pygame.image.load("imagenes/Jugador/homeroMuerto.png").convert_alpha()
        self.homeroBaile = pygame.image.load("imagenes/Jugador/homer_baile.png").convert_alpha()


        self.sangreHomero = pygame.image.load("imagenes/sangre.jpg").convert_alpha()

        self.cuadrovida1 = pygame.image.load("imagenes/objetosYplataformas/cuadrovida1.png").convert_alpha()
        self.cuadrovida2 = pygame.image.load("imagenes/objetosYplataformas/cuadrovida2.png").convert_alpha()

        self.spriteEnemigo1 = pygame.image.load('imagenes/Enemigos/esqueleto.png')  # cargamos la imagen con su extension
        self.spriteEnemigo2 = pygame.image.load('imagenes/Enemigos/hand.png')  # cargamos la imagen con su extension
        self.spriteEnemigo3 = pygame.image.load('imagenes/Enemigos/Dracula.png')  # cargamos la imagen con su extension
        self.disparoDracula = pygame.image.load('imagenes/Enemigos/disparo.png')  # cargamos la imagen con su extension

        self.spriteAlmas = pygame.image.load('imagenes/objetosYplataformas/almaDolares.png')
        self.puerta = pygame.image.load("imagenes/objetosYplataformas/puerta.png")

        self.Imagenpausa = pygame.image.load("imagenes/pausa.png")
        self.gameOver = pygame.image.load("imagenes/Game_over.png")
        self.homeroGana = pygame.image.load("imagenes/homeroGana.png")

        # listas donde guardaremos los sprites recortados
        self.lsCaminar = []
        self.lsCaminarIzq = []
        self.lsSalto = []
        self.lsSaltoIzq = []
        self.lsMaso = []
        self.lsMuerto = []
        self.lsBaile = []
        self.lsMasoIzq = []

        self.lsAlmas = []
        self.lsSangreHomero = []

        self.matriz1 = []
        self.matriz2 = []
        self.matriz3 = []
        self.lsDisparo = []
        # NUEVA LISTA CON SPRITES YA RECORTADOS CON LA FUNCION RECORTAR
        self.ls1 = recortarLista(self.lsCaminar, self.spriteJugadorCaminar, 9, 45.1, 65)
        self.ls1Izq = recortarLista(self.lsCaminarIzq, self.spriteJugadorCaminarIzq, 9, 45.1, 65)
        self.ls2 = recortarLista(self.lsSalto, self.spriteJugadorSalto, 3, 63, 70)
        self.ls2Izq = recortarLista(self.lsSaltoIzq, self.spriteJugadorSaltoIzq, 3, 63, 70)
        self.ls3 = recortarLista(self.lsMaso, self.spriteJugadorMaso, 5, 81.5, 75)
        self.ls4 = recortarLista(self.lsMuerto, self.homeroFrito, 2, 85, 105)
        self.ls5 = recortarLista(self.lsBaile, self.homeroBaile, 4, 48, 86)
        self.ls3Izq = recortarLista(self.lsMasoIzq, self.spriteJugadorMasoIzq, 5, 79.9, 75)
        self.m = [self.ls1, self.ls2, self.ls3, self.ls1Izq, self.ls2Izq, self.ls4, self.ls5, self.ls3Izq]
        # ALMAS
        self.mAlmas = recortarLista(self.lsAlmas, self.spriteAlmas, 4, 45, 40)
        self.lsSangreHomero = recortarMatriz(self.sangreHomero, 4, 4, 224, 224)
        self.puntajeAlmas = self.mAlmas[2]
        # LISTAS DE SPRITES ENEMIGOS
        self.matrizEnemigo1 = recortarLista(self.matriz1, self.spriteEnemigo1, 6, 32.95, 67)
        self.matrizEnemigo2 = recortarLista(self.matriz2, self.spriteEnemigo2, 9, 50, 36)
        self.matrizEnemigo3 = recortarLista(self.matriz3, self.spriteEnemigo3, 8, 69, 83)
        self.matrizDisparoDracula = recortarLista(self.lsDisparo, self.disparoDracula, 4, 80, 32)

        self.pausaImagen = False