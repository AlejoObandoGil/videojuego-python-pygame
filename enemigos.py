import pygame
from pygame.locals import *
from random import randint

from colors import *
from constantes import *
from plataformas import PlataformaEnMovimiento
from niveles import *

# 384 ancho / 12 sprites = 32 pix
# 256 alto / 8 sprites = 32 pix
""" Super clase genérica usada para definir un enemigo.
    Crea una clase hija para cada nivel con una info específica. """


class Enemigos(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self, m):  # Constructor
        super().__init__()  # Llama al constructor padre
        self.m = None  # matriz para guardar cada sprite recortado
        self.limites = None
        self.accion = None  # animacion por accion(correr, saltar, etc)
        self.con = None  # contador para las transiciones de la animacion
        self.image = None  # la imagen cambia respecto a las posiciones de m
        self.rect = None  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.velx = 0  # Establecemos el vector velocidad del jugador
        self.vely = 0
        self.fric = 1
        self.muerto = 0  # todos empiezan el juego vivos
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar

        self.tiempoCambio = 1

    def animacion(self):  # metodo que cambia la transicion de la animacion
        # if self.tiempoCambio == tiempo:
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.tiempoCambio += 1
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.con < self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.accion = 1
            self.con = 9  # reinicia el contador

    def update(self):  # Movimientos del jugador
        # self.calc_grav()  # Gravedad
        #self.disparo()
        #self.calc_grav()
        self.rect.x -= self.velx  # Desplazar izquierda/derecha
        self.animacion()


        """""
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado
            # izquierdo del objeto que hemos tocado
            if self.velx > 0:
                self.rect.right = bloque.rect.left
            elif self.velx < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/izquierda
        self.rect.y += self.vely

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.vely > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vely < 0:
                self.rect.top = bloque.rect.bottom

            # Detenemos nuestro movimiento vertical
            self.vely = 0
            if isinstance(bloque, PlataformaEnMovimiento):
                self.rect.x += bloque.velx

    def calc_grav(self):  # Calculamos el efecto de la gravedad.
        if self.vely == 0:
            self.vely = 1
        else:
            self.vely += .35

        # Observamos si nos encontramos sobre el suelo.
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.vely >= 0:
            self.vely = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height

    def saltar(self):
        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien
        # si solo descendemos uno).
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2

        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
            self.cambio_y = -10
    """""
    print("Enemigos READY")


class Enemigos1(Enemigos):

    def __init__(self, m):

        Enemigos.__init__(self,m)

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.move_ip(-900, 515)
        self.velx = 2  # Establecemos el vector velocidad del jugador
        self.vely = 0
        self.fric = 1
        self.muerto = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.tiempoCambio = 100
        self.rango = 50

    def animacion(self):  # metodo que cambia la transicion de la animacion
        if randint(0, 100) < self.rango:
            self.rect.x -= self.velx
            self.tiempoCambio += 100
            self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
            if self.con < 5:  # este sprite es de 3 imagenes
                self.con += 1
            else:
                self.con = 0  # reinicia el contador

class Enemigos2(Enemigos):

    def __init__(self, m):

        Enemigos.__init__(self,m)

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.move_ip(300, 515)
        self.velx = 5  # Establecemos el vector velocidad del jugador
        self.vely = 0
        self.muerto = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.rango = 10


    def animacion(self):  # metodo que cambia la transicion de la animacion
        if randint(0, 100) < self.rango:
            self.rect.x -= self.velx
            self.tiempoCambio += 100
            self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
            if self.con < 7:  # este sprite es de 3 imagenes
                self.con += 1
            else:
                self.con = 0  # reinicia el contador

class Enemigos3(Enemigos):

    def __init__(self, m):

        Enemigos.__init__(self,m)

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.move_ip(100, 515)
        self.velx = 0  # Establecemos el vector velocidad del jugador
        self.vely = 0
        self.muerto = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.rango = 45
        self.rangoDisparos = 9


    def animacion(self):  # metodo que cambia la transicion de la animacion
        if randint(0, 100) < self.rango:
            self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
            if self.con < 7:  # este sprite es de 3 imagenes
                self.con += 1
            else:
                self.con = 0  # reinicia el contador

class Disparos(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self, m):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.velx = 10  # Establecemos el vector velocidad del jugador
        self.rangoDisparos = 2

    def animacion(self):  # metodo que cambia la transicion de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        if self.con < 3:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.con = 0  # reinicia el contador

    def update(self):
        self.animacion()
        if self.rect.x > - self.velx:
            self.rect.x -= self.velx

    print("Disparos READY")

class EnemigoFlanders(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = pygame.image.load("imagenes/Enemigos/Devil_Flanders.png").convert_alpha()  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.move_ip(800, 50)
        self.velx = 8  # Establecemos el vector velocidad del jugador
        self.vely = 0
        self.muerto = 0
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.rango = 45
        self.rangoDisparos = 9
        self.bandera = 0

    def update(self):
        if self.rect.x == 100:
            self.bandera = 0
        elif self.rect.x == 800:
            self.bandera = 1

        if self.bandera == 0:
            self.rect.x += 10
        elif self.bandera == 1:
            self.rect.x -= 10


class DisparoFlanders(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self, m):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.vely = 20  # Establecemos el vector velocidad del jugador
        self.rangoDisparos = 8

    def animacion(self):  # metodo que cambia la transicion de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        if self.con < 3:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.con = 0  # reinicia el contador

    def update(self):
        self.animacion()
        if self.rect.y > - self.vely:
            self.rect.y += self.vely


class Barravida2(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("imagenes/objetosYplataformas/barravida2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(836, 4)
        self.flandersMuerto = False

    def update(self):
        if self.rect.x >= 1010:  # pierde toda la vida
            self.flandersMuerto = True
