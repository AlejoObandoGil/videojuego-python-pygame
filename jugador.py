import pygame
from random import randint

from colors import *
from constantes import *
from plataformas import PlataformaEnMovimiento


class Jugador(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self, m):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.m = m  # matriz para guardar cada sprite recortado
        self.limites = [8, 2, 4, 8, 2, 1, 3, 4]
        self.accion = 0  # animacion por accion(correr, saltar, etc)
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = 350
        self.rect.y = 435
        self.fric = 30
        self.muerto = 0
        self.cambio_x = 0  # Establecemos el vector velocidad del jugador
        self.cambio_y = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.puntaje = 0

    def update(self):  # Movimientos del jugador
        # if self.tiempoCambio == tiempo:
        # self.tiempoCambio += 1
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.accion != 1 and self.accion != 4:  # si no esta saltando
            if self.cambio_x != 0 or self.accion == 2:
                if (self.accion == 2):
                    if self.con < (self.limites[self.accion]):
                         self.con += 1
                    else:
                        self.accion = 0
                        self.con = 0
                elif self.con < (self.limites[self.accion]):  # este sprite es de 3 imagenes
                    self.con += 1
                else:
                    self.accion = 0
                    self.con = 0  # reinicia el contador

        self.calc_grav()  # Gravedad

        self.rect.x += self.cambio_x  # Desplazar izquierda/derecha

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado
            # izquierdo del objeto que hemos tocado
            if self.cambio_x > 0:
                if self.rect.right >= bloque.rect.left:
                    self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                if self.rect.left <= bloque.rect.right:
                    self.rect.left = bloque.rect.right

        self.rect.y += self.cambio_y  # Desplazar arriba/izquierda

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
                if self.accion != 2:  # si no esta golpeando con el maso
                        if self.cambio_x >= 0:  # si camina a la derecha o esta quieto
                            self.accion = 0
                        if self.cambio_x < 0:  # si camina  a la izquierda
                            self.accion = 3
                self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom

            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0
            if isinstance(bloque, PlataformaEnMovimiento):
                self.rect.x += bloque.cambio_x

    print("Jugador READY")

    def calc_grav(self):  # Calculamos el efecto de la gravedad.
        if self.cambio_y == 0:
            self.cambio_y = 2
        else:
            self.cambio_y += 1.98

        # Observamos si nos encontramos sobre el suelo.
        if self.rect.y >= (ALTO_PANTALLA - self.rect.height) - 50 and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height - 50
            if self.accion != 2 and self.accion != 7:  # si no esta golpeando con el maso
                if self.cambio_x >= 0:  # si camina a la derecha o esta quieto
                    self.accion = 0
                if self.cambio_y == 0:
                    if self.cambio_x < 0: #si camina  a la izquierda
                        self.accion = 3
            self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m

    def saltar(self):
        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien
        # si solo descendemos uno).

        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2

        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA - 50:
            self.cambio_y = - 23
            #self.cambio_x = 2

    #  Movimiento controlado por el jugador:
    def ir_izquierda(self):
        self.cambio_x = -10

    def ir_derecha(self):
        self.cambio_x = 10

    def stop(self):
        self.cambio_x = 0


class Barravida1(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("imagenes/objetosYplataformas/barravida1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(18, 4)
        self.homeroMuerto = False

    def update(self):
        if self.rect.x <= -152:  # pierde toda la vida
            self.homeroMuerto = True


class Sangre(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self):  # Constructor
        super().__init__()  # Llama al constructor padre

        #self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 0  # animacion por accion(correr, saltar, etc)
        self.con = 0  # contador para las transiciones de la animacion
        self.image = pygame.image.load("imagenes/sangre1.png").convert_alpha()  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = - 200
        self.rect.y = - 200
        self.cambio_x = 0  # Establecemos el vector velocidad del jugador
        self.cambio_y = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar




