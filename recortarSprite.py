import pygame
from colors import *
from constantes import *


class RecortarSprite(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, nombreArchivo):
        """ Constructor. Pass in the file name of the sprite sheet. """
        # Load the sprite sheet.
        self.cargarSprite = pygame.image.load(nombreArchivo).convert()

    def get_imagen(self, x, y, ancho, alto):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image
        imagen = pygame.Surface([ancho, alto]).convert()
        # Copy the sprite from the large sheet onto the smaller image
        imagen.blit(self.cargarSprite, (0, 0), (x, y, ancho, alto))
        imagen.set_colorkey(BLACK)
        return imagen