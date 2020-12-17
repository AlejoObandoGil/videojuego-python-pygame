import pygame
from random import randint
from pygame.locals import *

from colors import *
from constantes import *
from jugador import *
from niveles import *
from enemigos import *
from vidasHomero import *
from controlMultimedia import *
from main import *
"""
# ------------------------------FUNCIONES----------------------------------------
def HomeroGana(jugador):
    controlSonido = ControlSonido()
    controlSprites = ControlSprites()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sonidos/musicaDeFondo/canserbero_esEpico.mp3')
    # (-1 = reproduce siempre, 0.0 = la musica empieza cuando inicia el juego)
    pygame.mixer.music.play(-1, 0.0)
    #controlSonido.sonidoHomeroMuerto.play()
    fuenteSistema = pygame.font.Font(None, 50)
    textoPantalla = fuenteSistema.render("Tu puntaje es:" + str(jugador.puntaje), 0, (GRAY))

    pausado = True

    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                #despausamos el juego
                if evento.key == pygame.K_r:
                     main()
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pantalla.blit(controlSprites.homeroGana, (300, 100))
        pantalla.blit(textoPantalla, (300, 440))
        pygame.display.flip()


def GameOver(jugador):
    controlSonido = ControlSonido()
    controlSprites = ControlSprites()
    pygame.mixer.music.stop()
    controlSonido.sonidoHomeroMuerto.play()
    fuenteSistema = pygame.font.Font(None, 30)
    textoPantalla = fuenteSistema.render("Presiona R para reiniciar el juego "
                                         " Tu Puntaje es:" + str(jugador.puntaje), 0, (GRAY))

    pausado = True

    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                #despausamos el juego
                if evento.key == pygame.K_r:
                     main()
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pantalla.blit(controlSprites.gameOver, (200, 100))
        pantalla.blit(textoPantalla, (200, 440))
        pygame.display.flip()


def Pausar():
    controlSonido = ControlSonido()
    controlSprites = ControlSprites()
    pygame.mixer.music.stop()
    controlSonido.sonidoPausa.play()

    pausado = True

    while pausado:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                #despausamos el juego
                if evento.key == pygame.K_p:
                    pausado = False
                    pygame.mixer.music.play(-1, 0.0)
                    controlSonido.sonidoPausa.stop()
                if evento.key == pygame.K_r:
                    controlSonido.SonidoComenzarJuego.play()
                    main()
                elif evento.key == pygame.K_m:
                    if controlSonido.músicaSonando:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                        controlSonido.músicaSonando = not controlSonido.músicaSonando
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pantalla.blit(controlSprites.Imagenpausa, (300, 200))
        pygame.display.flip()
"""




