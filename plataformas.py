import pygame
from colors import *
from constantes import *
from recortarSprite import *

# Tipos de plataformas = (ubicacion x sprite,ubiacion y sprite, ancho sprite, alto sprite)


# 914 ancho imagen tiles / 12 sprites = 76 pixeles
# 936 alto imagen tiles / 13 = 72 pixeles
class Plataforma(pygame.sprite.Sprite):

    METAL2_IZQ = (6 * 36, 10 * 35.9, 38, 20)
    METAL2_DER = (11 * 36, 9 * 35.9, 40, 20)
    METAL2_MED = (2 * 36, 2 * 35.9, 36, 20)
    CAJONDORADO = (0, 0, 36, 36)
    CERRADURA = (6 * 35.9, 5 * 35.9, 37, 37)
    VERDEROCA = (0, 13 * 36, 105, 30)
    VERDEROCAGRANDE = (108, 13 * 36, 107, 68)
    PIEDRAGRIS = (215, 13 * 35.9, 45, 105)
    CAJONCAFE = (3*36, 0, 36, 36)
    BOLASLOCAS = (4 * 36, 9*36, 36, 36)
    PALO =(2 * 36, 1 * 35.9, 38, 20)
    PASTOVERDE = (9*36, 0, 36, 36)


    def __init__(self, sprite_sheet_data):

        super().__init__()

        recortarSprite = RecortarSprite("imagenes/objetosYplataformas/tiles_spritesheet1.png")

        self.image = recortarSprite.get_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

    print("Plataforma READY")



class PlataformaEnMovimiento(Plataforma):
    cambio_x = 0
    cambio_y = 0

    limite_superior = 0
    limite_inferior = 0
    limite_izquierda = 0
    limite_derecha = 0

    jugador = None

    Nivel = None

    def update(self):
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # Comprobamos si hemos chocado contra el protagonista
        impacto = pygame.sprite.collide_rect(self, self.jugador)
        if impacto:
            # Hemos impactado contra el protagonista. Lo empujamos a un lado
            # y asumimos que no impactará con ninguna otra cosa.

            # Si nos estamos desplazando hacia la derecha, establece que nuestro lado
            # derecho se coloque al lado izquierdo del objeto contra el que hemos
            # impactado
            if self.cambio_x < 0:
                self.jugador.rect.right = self.rect.left
            else:
                # En caso contrario (desplazamiento a la izquierda), hacemos lo opuesto
                self.jugador.rect.left = self.rect.right

        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y

        # Comprobamos si hemos impactado con el protagonista
        impacto = pygame.sprite.collide_rect(self, self.jugador)
        if impacto:
            # Hemos impactado contra el protagonista. Lo empujamos a un lado
            # y asumimos que no impactará con ninguna otra cosa.

            # Restablecemos nuestra posición basándonos en la parte superior/inferior
            # del objeto
            if self.cambio_y < 0:
                self.jugador.rect.bottom = self.rect.top
            else:
                self.jugador.rect.top = self.rect.bottom

        # Comprobamos los límites y vemos si es necesario invertir el sentido

        if self.rect.bottom > self.limite_inferior or self.rect.top < self.limite_superior:
            self.cambio_y *= -1

        cur_pos = self.rect.x - self.nivel.desplazar_escenario
        if cur_pos < self.limite_izquierda or cur_pos > self.limite_derecha:
            self.cambio_x *= -1

    print("Plataforma en Movimiento READY")
