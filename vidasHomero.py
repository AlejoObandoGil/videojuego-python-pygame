import pygame
from colors import *
from constantes import *
from jugador import *
from plataformas import PlataformaEnMovimiento


class Cerveza(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.image = pygame.image.load('imagenes/objetosYplataformas/cerveza.png')
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = - 100
        self.rect.y = - 100
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar


class Almas(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self, m):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.m = m  # matriz para guardar cada sprite recortado
        self.con = 2  # contador para las transiciones de la animacion
        self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = -550
        self.rect.y = -435
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar
        self.rango = 50

    def update(self):
        if randint(0, 100) < self.rango:
            self.image = self.m[self.con]  # la imagen cambia respecto a las posiciones de m
            if self.con < 3:  # este sprite es de 3 imagenes
                self.con += 1
            else:
                self.con = 0  # reinicia el contador


class Exit(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.image = pygame.image.load('imagenes/objetosYplataformas/exit.png')
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = 120
        self.rect.y = 470
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar

class Fuego(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.image = pygame.image.load('imagenes/objetosYplataformas/fuego.png')
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = 120
        self.rect.y = 470
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar


class Puerta(pygame.sprite.Sprite):
    # -- Métodos
    def __init__(self):  # Constructor
        super().__init__()  # Llama al constructor padre

        self.image = pygame.image.load('imagenes/objetosYplataformas/puerta.png')
        self.rect = self.image.get_rect()  # posicion del rectangulo que pertenece a el sprite en la pantalla
        self.rect.x = -300
        self.rect.y = -300
        self.nivel = None  # Lista de todos los sprites contra los que podemos botar



