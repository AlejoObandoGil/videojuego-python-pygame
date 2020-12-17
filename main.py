""" codigo principal, contiene el ciclo principal del juego """


# -------------------------LIBRERIAS---------------------------------

import pygame
from random import randint
from pygame.locals import *

from colors import *
from constantes import *
from jugador import *
from niveles import *
from enemigos import *
from vidasHomero import *
from controlFunciones import *
from controlMultimedia import *


# GLOBALES
dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
pantalla = pygame.display.set_mode(dimensiones)

# -------------------------FUNCION PRINCIPAL---------------------------------
def main():
    pygame.init()

    # Nombre de la ventana
    pygame.display.set_caption("Homero Epico")

    # FUENTES DE TEXTO
    fuenteSistema = pygame.font.Font(None, 30)
    # EFECTOS DE SONIDOS Y MUSICA
    controlSonido = ControlSonido()
    #SPRITES E IMAGENES
    controlSprites = ControlSprites()

    # -------------------OBJETOS Y LISTAS GROUP------------------------------
    # Creamos objeto de HOMERO
    jugador = Jugador(controlSprites.m)
    barravida1 = Barravida1()
    barravida2 = Barravida2()
    cerveza = Cerveza()
    almas = Almas(controlSprites.mAlmas)
    sangre = Sangre()
    salida = Exit()
    fuego = Fuego()
    puerta = Puerta()

    # creamos objetos de enemigos
    enemigo1 = Enemigos1(controlSprites.matrizEnemigo1)
    enemigo2 = Enemigos2(controlSprites.matrizEnemigo2)
    enemigo3 = Enemigos3(controlSprites.matrizEnemigo3)
    disparoEnemigo = Disparos(controlSprites.matrizDisparoDracula)
    disparoFlanders = DisparoFlanders(controlSprites.matrizDisparoDracula)

    # Creamos todos los niveles
    listade_niveles = []
    nivel1 = Nivel_01(jugador, enemigo1, enemigo2, enemigo3, almas)
    listade_niveles.append(nivel1)
    nivel2 = Nivel_02(jugador, enemigo1, enemigo2, enemigo3, almas)
    listade_niveles.append(nivel2)

    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]

    listade_sprites_activas = pygame.sprite.Group()
    # Lista de cada proyectil
    lista_proyectiles = pygame.sprite.Group()
    listaDisparos_flanders = pygame.sprite.Group()

    lista_sangre = pygame.sprite.Group()

    jugador.nivel = nivel_actual
    enemigo1.nivel = nivel_actual
    enemigo2.nivel = nivel_actual
    enemigo3.nivel = nivel_actual
    cerveza.nivel = nivel_actual
    almas.nivel = nivel_actual
    salida.nivel = nivel_actual
    fuego.nivel = nivel_actual
    puerta.nivel = nivel_actual

    jugador.rect.x = 120
    jugador.rect.y = ALTO_PANTALLA - 600

    listade_sprites_activas.add(jugador)

    puntuacion = 0

    # Iteramos hasta que el usuario hace click sobre el botón de salir.
    hecho = False

    # Usado para gestionar cuán rápido se actualiza la pantalla.
    reloj = pygame.time.Clock()
    # play music
    pausado = False
    pygame.mixer.music.play(-1, 0.0)

    # ---------------- BUCLE PRINCIPAL DEL PROGRAMA  ------------------
    while not hecho:

        # --------------ACTUALIZACION DE CONFIGURACIONES------------------
        nivel_actual.update()
        listade_sprites_activas.update()
        barravida1.update()
        lista_proyectiles.update()
        listaDisparos_flanders.update()

        textoPantalla = fuenteSistema.render(str(jugador.puntaje), 0, (WHITE))

        # ------------------ACTUALIZACION DE GRAFICOS-------------------
        nivel_actual.draw(pantalla)
        listade_sprites_activas.draw(pantalla)
        listaDisparos_flanders.draw(pantalla)
        lista_proyectiles.draw(pantalla)
        pantalla.blit(barravida1.image, barravida1.rect)
        pantalla.blit(controlSprites.cuadrovida1, (0, 0))
        pantalla.blit(controlSprites.puntajeAlmas, (200, 0))
        pantalla.blit(textoPantalla, (260, 10))

        if barravida1.homeroMuerto:
            GameOver(jugador)

        # Limitamos la velocidad del juego a 20 fps
        reloj.tick(20)
        #tiempo = int(pygame.time.get_ticks())
        controlSonido.músicaSonando = True
        for evento in pygame.event.get():  # El usuario realizó alguna acción
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                hecho = True  # Marcamos como hecho y salimos de este bucle
            if evento.type == pygame.KEYDOWN:

                # pausar el juego
                if evento.key == pygame.K_p:
                    pausado = True
                    pausar = Pausar()
                # tecla M para pausar la musica
                if evento.key == pygame.K_m:
                    if controlSonido.músicaSonando:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                        controlSonido.músicaSonando = not controlSonido.músicaSonando

                # Eventos del teclado, movimientos de homero
                if evento.key == pygame.K_LEFT:
                    jugador.ir_izquierda()
                    if jugador.cambio_y <= 0:
                        jugador.accion = 4
                        jugador.con = 0
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoCaminar.play()
                if evento.key == pygame.K_RIGHT:
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoCaminar.play()
                    jugador.ir_derecha()

                if evento.key == pygame.K_UP:
                    if jugador.cambio_x >= 0:
                        if controlSonido.músicaSonando:
                            controlSonido.sonidoSalto.play()
                        jugador.saltar()
                        jugador.accion = 1
                        jugador.con = 0
                    if jugador.cambio_x < 0:
                        if controlSonido.músicaSonando:
                            controlSonido.sonidoSalto.play()
                        jugador.saltar()
                        jugador.accion = 4
                        jugador.con = 0

                if evento.key == pygame.K_x:
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoMaso.play()
                    if jugador.cambio_x >= 0:
                        jugador.accion = 2
                        jugador.con = 0
                    if jugador.cambio_x < 0:
                        jugador.accion = 7
                        jugador.con = 0
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador.cambio_x < 0:
                    jugador.stop()
                if evento.key == pygame.K_RIGHT and jugador.cambio_x > 0:
                    jugador.stop()

        # Si homero choca con un enemigo pierde vida
        listade_impactos_enemigo1 = pygame.sprite.spritecollide(jugador, nivel1.listade_enemigos1, False)
        for enemigo1 in listade_impactos_enemigo1:
            if jugador.rect.right >= enemigo1.rect.left:
                jugador.rect.right = enemigo1.rect.left
                jugador.rect.x -= jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoEsqueleto.play()
                    nivel1.listade_enemigos1.remove(enemigo1)
                    jugador.puntaje += 10

                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()
            # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
            if jugador.rect.left >= enemigo1.rect.right:
                jugador.rect.left = enemigo1.rect.right
                jugador.rect.x += jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoEsqueleto.play()
                    nivel1.listade_enemigos1.remove(enemigo1)
                    jugador.puntaje += 10
                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()

        listade_impactos_enemigo2 = pygame.sprite.spritecollide(jugador, nivel1.listade_enemigos2, False)
        for enemigo2 in listade_impactos_enemigo2:
            if jugador.rect.right >= enemigo2.rect.left:
                jugador.rect.right = enemigo2.rect.left
                jugador.rect.x -= jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoMano.play()
                    nivel1.listade_enemigos2.remove(enemigo2)
                    jugador.puntaje += 5
                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()
            if jugador.rect.left >= enemigo2.rect.right:
                jugador.rect.left = enemigo2.rect.right
                jugador.rect.x += jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoMano.play()
                    nivel1.listade_enemigos2.remove(enemigo2)
                    jugador.puntaje += 5
                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()

        listade_impactos_enemigo3 = pygame.sprite.spritecollide(jugador, nivel1.listade_enemigos3, False)
        for enemigo3 in listade_impactos_enemigo3:
            if jugador.rect.right >= enemigo3.rect.left:
                jugador.rect.right = enemigo3.rect.left
                jugador.rect.x -= jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoDracula.play()
                    jugador.rect.x = jugador.rect.x
                    nivel1.listade_enemigos3.remove(enemigo3)
                    if nivel1.listade_enemigos3.remove(enemigo3):
                        disparoEnemigo.rect.x = - 300
                        lista_proyectiles.remove(disparoEnemigo)
                    jugador.puntaje += 20
                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()
            if jugador.rect.left >= enemigo3.rect.right:
                jugador.rect.left = enemigo3.rect.right
                jugador.rect.x += jugador.fric
                if jugador.accion == 2:
                    if controlSonido.músicaSonando:
                        controlSonido.enemigoDracula.play()
                    jugador.rect.x = jugador.rect.x
                    nivel1.listade_enemigos3.remove(enemigo3)
                    if nivel1.listade_enemigos3.remove(enemigo3):
                        disparoEnemigo.rect.x = - 300
                        lista_proyectiles.remove(disparoEnemigo)
                    jugador.puntaje += 20
                else:
                    barravida1.rect.x -= 10
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    if controlSonido.músicaSonando:
                        controlSonido.sonidoOuch.play()

        listade_impactos_fuego = pygame.sprite.spritecollide(jugador, nivel1.listade_fuego, False)
        for fuego in listade_impactos_fuego:
            if jugador.rect.right >= fuego.rect.left or jugador.rect.bottom >= fuego.rect.top:
                barravida1.rect.x -= 200
                sangre = Sangre()
                pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                jugador.accion = 5
                jugador.con = 1
                if controlSonido.músicaSonando:
                    controlSonido.sonidoFuego.play()
            if jugador.rect.left >= enemigo3.rect.right or jugador.rect.bottom >= fuego.rect.top:
                barravida1.rect.x -= 200
                sangre = Sangre()
                pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                jugador.accion = 5
                jugador.con = 1
                if controlSonido.músicaSonando:
                    controlSonido.sonidoFuego.play()

        # Si homero coge una cerveza aumenta su sangre
        listade_impactos_cerveza = pygame.sprite.spritecollide(jugador, nivel1.listade_vidasHomero, False)
        for cerveza in listade_impactos_cerveza:
            cerveza.rect.x = - 100
            nivel1.listade_vidasHomero.remove(cerveza)
            if controlSonido.músicaSonando:
                controlSonido.sonidoCerveza.play()
            if barravida1.rect.x < 8:
                barravida1.rect.x += 20

        listade_impactos_almas = pygame.sprite.spritecollide(jugador, nivel1.listade_almasHomero, False)
        for almas in listade_impactos_almas:
            almas.rect.x = - 100
            nivel1.listade_almasHomero.remove(almas)
            jugador.puntaje += 1
            if controlSonido.músicaSonando:
                controlSonido.sonidoAlmas.play()

        # ------------------GENERADOR DE PROYECTIL---------------------
        for enemigo3 in nivel1.listade_dracula:
            # Disparo aleatorio dentro de un rango n de 0 a 100
            if enemigo3.con == 7 and enemigo3.rect.x > 0:
                if randint(0, 10) < disparoEnemigo.rangoDisparos:
                    disparoEnemigo = Disparos(controlSprites.matrizDisparoDracula)
                    disparoEnemigo.rect.x = enemigo3.rect.x + 20
                    disparoEnemigo.rect.y = enemigo3.rect.y + 20
                    lista_proyectiles.add(disparoEnemigo)

        # Calculamos la mecánica para cada proyectil
        for disparoEnemigo in lista_proyectiles:
            lista_bloques_alcanzados = pygame.sprite.spritecollide(disparoEnemigo, listade_sprites_activas, False)
            # Vemos si el proyectil alcanza a homero
            for jugador in lista_bloques_alcanzados:
                disparoEnemigo.rect.x = - 100
                lista_proyectiles.remove(disparoEnemigo)
                barravida1.rect.x -= 20
                sangre = Sangre()
                pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                jugador.velx = - 7

            # Eliminamos el proyectil si vuela fuera de la pantalla
            if disparoEnemigo.rect.x <= 0:
                lista_proyectiles.remove(disparoEnemigo)
            # lista_de_todos_los_sprites.remove(disparoEnemigo)


        # ------------------------EFECTO DESPLAZAR PANTALLA-------------------
        if nivel_actual_no < len(listade_niveles) - 1:
            # Si el protagonista se aproxima al borde derecho, desplazamos el escenario a la izquierda(-x)
            if jugador.rect.x >= 500:
                diff = jugador.rect.x - 500
                jugador.rect.x = 500
                nivel_actual.escenario_desplazar(-diff)
                # desplazamos los disparos de dracula
                for disparoEnemigo in lista_proyectiles:
                    disparoEnemigo.rect.x -= diff

            # Si el protagonista se aproxima al borde izquierdo, desplazamos el escenario a la derecha(+x)

            salidita = nivel1.listade_salidas[0]
            if jugador.rect.x <= salidita.rect.x:
                jugador.rect.x = salidita.rect.x

            if jugador.rect.x <= 120:
                diff = 120 - jugador.rect.x
                jugador.rect.x = 120
                nivel_actual.escenario_desplazar(diff)
        else:
            if jugador.rect.left <= 0:
                jugador.rect.left = 5
            if jugador.rect.right >= 1000:
                jugador.rect.right = 1000 - 5

            barravida2.update()
            pantalla.blit(barravida2.image, barravida2.rect)
            pantalla.blit(controlSprites.cuadrovida2, (832, 0))

            # ------------------GENERADOR DE PROYECTIL FLANDERS---------------------
            for flanders in nivel2.listade_Flanders:
                # Disparo aleatorio dentro de un rango n de 0 a 100
                if randint(0, 100) < disparoFlanders.rangoDisparos:
                    disparoFlanders = DisparoFlanders(controlSprites.matrizDisparoDracula)
                    disparoFlanders.rect.x = flanders.rect.x + 20
                    disparoFlanders.rect.y = flanders.rect.y + 20
                    listaDisparos_flanders.add(disparoFlanders)

            # Calculamos la mecánica para cada proyectil
            for disparoFlanders in listaDisparos_flanders:
                lista_bloques_alcanzados = pygame.sprite.spritecollide(disparoFlanders, listade_sprites_activas,
                                                                       False)
                # Vemos si el proyectil alcanza a homero
                for jugador in lista_bloques_alcanzados:
                    disparoFlanders.rect.y = - 200
                    listaDisparos_flanders.remove(disparoFlanders)
                    barravida1.rect.x -= 20
                    sangre = Sangre()
                    pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                    pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                    jugador.velx = - 7

                # Eliminamos el proyectil si vuela fuera de la pantalla
                if disparoFlanders.rect.y <= 600:
                    lista_proyectiles.remove(disparoFlanders)
                # lista_de_todos_los_sprites.remove(disparoEnemigo)

            listade_impactos_flanders = pygame.sprite.spritecollide(jugador, nivel2.listade_Flanders, False)
            for flanders in listade_impactos_flanders:
                if jugador.rect.right >= flanders.rect.left:
                    jugador.rect.right = flanders.rect.left
                    jugador.rect.x -= jugador.fric
                    if jugador.accion == 2:
                        jugador.puntaje += 5
                        barravida2.rect.x += 5
                    else:
                        barravida1.rect.x -= 10
                        sangre = Sangre()
                        pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                        pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                        if controlSonido.músicaSonando:
                            controlSonido.sonidoOuch.play()
                if jugador.rect.left >= flanders.rect.right:
                    jugador.rect.left = flanders.rect.right
                    jugador.rect.x += jugador.fric
                    if jugador.accion == 2:
                        jugador.puntaje += 5
                        barravida2.rect.x += 10
                    else:
                        barravida1.rect.x -= 10
                        sangre = Sangre()
                        pantalla.blit(sangre.image, (jugador.rect.x - 10, jugador.rect.y))
                        pantalla.blit(sangre.image, (jugador.rect.x - 40, jugador.rect.y + 20))
                        if controlSonido.músicaSonando:
                            controlSonido.sonidoOuch.play()

            listade_impactos_cerveza = pygame.sprite.spritecollide(jugador, nivel2.listade_vidasHomero, False)
            for cerveza in listade_impactos_cerveza:
                cerveza.rect.x = - 100
                nivel1.listade_vidasHomero.remove(cerveza)
                if controlSonido.músicaSonando:
                    controlSonido.sonidoCerveza.play()
                if barravida1.rect.x < 8:
                    barravida1.rect.x += 20

            if barravida2.flandersMuerto:
                HomeroGana(jugador)


        # Si el protagonista alcanza el final del nivel, pasa al siguiente
        posicion_actual = jugador.rect.x + nivel_actual.desplazar_escenario
        if posicion_actual < nivel_actual.limitedel_nivel_final:
            puertica = nivel1.listade_puertas[0]
            if jugador.rect.x >= puertica.rect.x:
                jugador.rect.x = 120
                if nivel_actual_no < len(listade_niveles) - 1:
                    nivel_actual_no += 1
                    nivel_actual = listade_niveles[nivel_actual_no]
                    jugador.nivel = nivel_actual
                    for enemigo1 in nivel1.listade_enemigos1:
                        enemigo1.rect.y = -2000
                        nivel1.listade_enemigos1.remove(enemigo1)

                    for enemigo2 in nivel1.listade_enemigos2:
                        enemigo2.rect.y = -2000
                        nivel1.listade_enemigos2.remove(enemigo2)

                    for enemigo3 in nivel1.listade_enemigos3:
                        enemigo3.rect.x = -2000
                        nivel1.listade_enemigos3.remove(enemigo3)

                    for disparoEnemigo in lista_proyectiles:
                        disparoEnemigo.rect.x = -2000
                        lista_proyectiles.remove(disparoEnemigo)

                    for fuego in nivel1.listade_fuego:
                        fuego.rect.x = -2000
                        nivel1.listade_fuego.remove(fuego)

        # Avanzamos y actualizamos la pantalla que ya hemos dibujado
        pygame.display.flip()
    # salir del ciclo
    pygame.quit()


def menuHistoria():
    pygame.init()
    # Nombre de la ventana
    pygame.display.set_caption("Homero Epico")
    # Efectos de sonido
    SonidoComenzarJuego = pygame.mixer.Sound('sonidos/efectosDeSonido/homero-informatico.wav')
    músicaSonando = True  # el jugador puede desactivar la musica

    fondoHistoria = pygame.image.load("imagenes/historia.png")

    reloj = pygame.time.Clock()
    hecho = False
    # ---------------- BUCLE PRINCIPAL DEL PROGRAMA  ------------------
    while not hecho:
        # Limitamos la velocidad del juego a 20 fps
        reloj.tick(20)

        for evento in pygame.event.get():  # El usuario realizó alguna acción
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                hecho = True  # Marcamos como hecho y salimos de este bucle
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if músicaSonando:
                        SonidoComenzarJuego.play()
                        main()
        pantalla.blit(fondoHistoria, (0, 0))  # refrescamos la pantalla
        pygame.display.flip()

    pygame.quit()


def menuInicio():
    pygame.init()
    # Nombre de la ventana
    pygame.display.set_caption("Homero Epico")
    # MUSICA
    pygame.mixer.music.load('sonidos/musicaDeFondo/the_simpsons.mp3')
    # (-1 = reproduce siempre, 0.0 = la musica empieza cuando inicia el juego)
    pygame.mixer.music.play(-1, 0.0)
    # Efectos de sonido
    SonidoComenzarJuego = pygame.mixer.Sound('sonidos/efectosDeSonido/homeroFeo.wav')
    músicaSonando = True  # el jugador puede desactivar la musica

    fondoInicio = pygame.image.load("imagenes/Inicio.jpg")

    reloj = pygame.time.Clock()
    hecho = False
    # ---------------- BUCLE PRINCIPAL DEL PROGRAMA  ------------------
    while not hecho:
        # Limitamos la velocidad del juego a 20 fps
        reloj.tick(20)

        for evento in pygame.event.get():  # El usuario realizó alguna acción
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                hecho = True  # Marcamos como hecho y salimos de este bucle
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if músicaSonando:
                        SonidoComenzarJuego.play()
                        menuHistoria()


        pantalla.blit(fondoInicio, (0, 0))  # refrescamos la pantalla
        pygame.display.flip()

    pygame.quit()


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


if __name__ == "__main__":
    menuInicio()
   # main()
