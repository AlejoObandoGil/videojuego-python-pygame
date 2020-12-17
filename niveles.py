import pygame
from pygame.locals import *
from random import randint

from colors import *
from constantes import *
from jugador import *
from plataformas import *
from enemigos import *
from vidasHomero import *

""" Super clase genérica usada para definir un nivel.
    Crea una clase hija para cada nivel con una info específica. """


class Nivel():
    # Background image

    def __init__(self, jugador, enemigo1, enemigo2, enemigo3, almas):
        """ Constructor.  Requerido para cuando las plataformas
            que se desplazan colisionan con el protagonista. """
        self.fondo = None
        self.fondoEscalado = None  # escalamos la imagen de fondo
        self.desplazar_escenario = 0  # C uán lejos se ha desplazado a la izquierda/derecha el escenario
        self.level_limit = - 1000  # limite hasta donde llega el jugador
        # listas
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos1 = pygame.sprite.Group()
        self.listade_enemigos2 = pygame.sprite.Group()
        self.listade_enemigos3 = pygame.sprite.Group()
        self.listade_Flanders = pygame.sprite.Group()

        self.listaDisparos = pygame.sprite.Group()

        self.listade_vidasHomero = pygame.sprite.Group()
        self.listade_almasHomero = pygame.sprite.Group()
        self.listade_exit = pygame.sprite.Group()
        self.listade_fuego = pygame.sprite.Group()
        self.listade_puerta = pygame.sprite.Group()

        self.listade_dracula = []
        self.listade_puertas = []




        # obejetos
        self.jugador = jugador
        self.enemigo1 = enemigo1
        self.enemigo2 = enemigo2
        self.enemigo3 = enemigo3
        self.almas = almas

        self.matrizAlmas = self.almas.m
        self.matrizEnemigo1 = self.enemigo1.m
        self.matrizEnemigo2 = self.enemigo2.m
        self.matrizEnemigo3 = self.enemigo3.m

    # Actualizamos todo en este nivel
    def update(self):
        self.listade_plataformas.update()
        self.listade_enemigos1.update()
        self.listade_enemigos2.update()
        self.listade_enemigos3.update()
        self.listade_Flanders.update()
        self.listaDisparos.update()

        self.listade_vidasHomero.update()
        self.listade_almasHomero.update()
        self.listade_fuego.update()

        self.listade_exit.update()
        self.listade_puerta.update()


    # Dibujamos todo en  este nivel
    def draw(self, pantalla):
        # Dibujamos el fondo
        pantalla.fill(BLUE)
        pantalla.blit(self.fondoEscalado, (self.desplazar_escenario // 2, 0))
        # Dibujamos todas las listas de sprites que tengamos
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos1.draw(pantalla)
        self.listade_enemigos2.draw(pantalla)
        self.listade_enemigos3.draw(pantalla)
        self.listade_Flanders.draw(pantalla)
        self.listaDisparos.draw(pantalla)

        self.listade_vidasHomero.draw(pantalla)
        self.listade_almasHomero.draw(pantalla)
        self.listade_fuego.draw(pantalla)

        self.listade_exit.draw(pantalla)
        self.listade_puerta.draw(pantalla)


    def escenario_desplazar(self, desplazar_x):
        """ Para cuando el jugador se desplaza a la izquierda/derecha y necesitamos mover
        todo: """
        # Llevamos la cuenta de la cantidad de desplazamiento
        self.desplazar_escenario += desplazar_x

        # Iteramos a través de todas las listas de sprites y desplazamos
        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x

        for enemigo1 in self.listade_enemigos1:
            enemigo1.rect.x += desplazar_x

        for enemigo2 in self.listade_enemigos2:
            enemigo2.rect.x += desplazar_x

        for enemigo3 in self.listade_enemigos3:
            enemigo3.rect.x += desplazar_x

        for flanders in self.listade_Flanders:
            flanders.rect.x += desplazar_x

        for cerveza in self.listade_vidasHomero:
            cerveza.rect.x += desplazar_x

        for almas in self.listade_almasHomero:
            almas.rect.x += desplazar_x

        for fuego1 in self.listade_fuego:
            fuego1.rect.x += desplazar_x

        for exit in self.listade_exit:
            exit.rect.x += desplazar_x

        for puerta in self.listade_puerta:
            puerta.rect.x += desplazar_x



class Nivel_01(Nivel):
    """ Definición para el nivel 1. """

    def __init__(self, jugador, enemigo1, enemigo2, enemigo3, almas):
        """ Creamos el nivel 1. """

        # Llamamos al constructor padre
        Nivel.__init__(self, jugador, enemigo1, enemigo2, enemigo3, almas)
        # 2048 x 276 tamaño de fondo
        self.fondo = pygame.image.load("imagenes/Demon'sCrest-Murkland-Cemetery.png").convert()
        self.fondoEscalado = pygame.transform.scale(self.fondo, (2048 * 2, 300 * 2))
        self.rect = self.fondoEscalado.get_rect()
        self.rect.x = 2048
        self.rect.y = 276
        self.limitedel_nivel_final = - 5500
        self.limitedel_nivel_inicio = 30
        self.rangoDisparos = 2
        self.listade_dracula = []
        self.listade_puertas = []
        self.listade_salidas = []

        self.rango = 10

        # Array con el largo, alto, y posiciones(x, y) de la plataforma
        nivel = [
            [Plataforma.VERDEROCA, 400, 430],
             [Plataforma.VERDEROCA, 500, 380],
             [Plataforma.VERDEROCA, 600, 380],
             [Plataforma.VERDEROCA, 700, 380],
                [Plataforma.VERDEROCAGRANDE, 900, 473],
                [Plataforma.VERDEROCAGRANDE, 1005, 473],
                [Plataforma.VERDEROCAGRANDE, 1110, 473],
            [Plataforma.VERDEROCAGRANDE, 1005, 405],
            [Plataforma.VERDEROCAGRANDE, 1110, 405],
                [Plataforma.VERDEROCA, 1006, 375],
                [Plataforma.VERDEROCA, 1111, 375],
                    [Plataforma.VERDEROCA, 900, 130],
                    [Plataforma.VERDEROCA, 1005, 130],
                    [Plataforma.VERDEROCA, 1110, 130],
            [Plataforma.VERDEROCA, 1300, 375],
             [Plataforma.VERDEROCA, 1450, 275],
              [Plataforma.VERDEROCA, 1600, 175],

            [Plataforma.VERDEROCA, 2700, 510],
            [Plataforma.VERDEROCA, 2750, 480],
            [Plataforma.VERDEROCA, 2800, 450],
            [Plataforma.VERDEROCA, 2850, 420],
                [Plataforma.VERDEROCA, 3050, 420],
                [Plataforma.VERDEROCA, 3100, 450],
                [Plataforma.VERDEROCA, 3150, 480],
                [Plataforma.VERDEROCA, 3200, 510],

            [Plataforma.METAL2_IZQ, 3600, 240],
            [Plataforma.METAL2_IZQ, 3600, 260],
            [Plataforma.METAL2_IZQ, 3600, 280],
            [Plataforma.METAL2_IZQ, 3600, 300],
            [Plataforma.METAL2_IZQ, 3600, 220],
            [Plataforma.METAL2_IZQ, 3600, 200],
            [Plataforma.METAL2_IZQ, 3650, 200],
            [Plataforma.METAL2_IZQ, 3700, 200],
            [Plataforma.METAL2_IZQ, 3750, 200],
            [Plataforma.METAL2_IZQ, 3800, 200],
            [Plataforma.METAL2_IZQ, 3850, 200],
            [Plataforma.METAL2_IZQ, 3900, 200],
            [Plataforma.METAL2_IZQ, 3950, 200],
            [Plataforma.METAL2_IZQ, 4000, 200],
            [Plataforma.METAL2_IZQ, 4000, 220],
            [Plataforma.METAL2_IZQ, 4000, 240],
            [Plataforma.METAL2_IZQ, 4000, 260],
            [Plataforma.METAL2_IZQ, 4000, 280],
            [Plataforma.METAL2_IZQ, 4000, 300],
                [Plataforma.CAJONCAFE, 4200, 200],
                [Plataforma.CAJONCAFE, 4250, 250],
                [Plataforma.CAJONCAFE, 4300, 200],
            [Plataforma.VERDEROCA, 4380, 100],
            [Plataforma.VERDEROCA, 4480, 100],
            [Plataforma.METAL2_IZQ, 4600, 140],
            [Plataforma.METAL2_IZQ, 4640, 160],
            [Plataforma.METAL2_IZQ, 4680, 180],
            [Plataforma.METAL2_IZQ, 4720, 200],
            [Plataforma.VERDEROCA, 4760, 240],
            [Plataforma.VERDEROCA, 4860, 240],
                [Plataforma.BOLASLOCAS, 4210, 400],
                [Plataforma.BOLASLOCAS, 4260, 400],
                [Plataforma.BOLASLOCAS, 4310, 400],
                [Plataforma.BOLASLOCAS, 4160, 400],
                [Plataforma.BOLASLOCAS, 4310, 400],
            [Plataforma.PALO, 2700, 60],
            [Plataforma.PALO, 2750, 60],
            [Plataforma.PALO, 2800, 60],
            [Plataforma.PALO, 2850, 60],
            [Plataforma.PALO, 3050, 100],
            [Plataforma.PALO, 3100, 100],
            [Plataforma.PALO, 3150, 100],
            [Plataforma.PALO, 3200, 100],
            [Plataforma.PALO, 3250, 100],
                [Plataforma.PASTOVERDE, 5300, 100],
                [Plataforma.PASTOVERDE, 5330, 100],
                [Plataforma.PASTOVERDE, 5360, 100],
                [Plataforma.PASTOVERDE, 5390, 100],
                [Plataforma.PASTOVERDE, 5420, 100],
                [Plataforma.PASTOVERDE, 5450, 100],
                [Plataforma.PASTOVERDE, 5480, 100],
                [Plataforma.PASTOVERDE, 5510, 100],
                [Plataforma.PASTOVERDE, 5540, 100],
                [Plataforma.PASTOVERDE, 5570, 100],
                [Plataforma.PASTOVERDE, 5600, 100],
                [Plataforma.PASTOVERDE, 5630, 100],
                [Plataforma.PASTOVERDE, 5660, 100],
                [Plataforma.PASTOVERDE, 5690, 100],
                [Plataforma.PASTOVERDE, 5720, 100],
                [Plataforma.PASTOVERDE, 5750, 100],
            [Plataforma.VERDEROCAGRANDE, 5320, 480],
            [Plataforma.VERDEROCAGRANDE, 5420, 480],
            [Plataforma.VERDEROCAGRANDE, 5520, 480],
            [Plataforma.VERDEROCAGRANDE, 5620, 480],
        ]

        # Iteramos a través del array anterior y añadimos plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0])
            # print(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.listade_plataformas.add(bloque)
        # Creamos las plataformas para el nivel

        # agregamos una plataforma en movimiento hacia arriba y abajo

        # lista de plataformas personalizadas
        nivelArriba = [
            [Plataforma.METAL2_MED, 840, 300, 500],
            [Plataforma.METAL2_MED, 1750, 300, 400],
            [Plataforma.METAL2_MED, 1900, 120, 400],
            [Plataforma.METAL2_MED, 2050, 350, 400],
            [Plataforma.METAL2_MED, 2300, 250, 400],
            [Plataforma.METAL2_MED, 2500, 150, 400],
            [Plataforma.METAL2_MED, 3500, 300, 500],
            [Plataforma.METAL2_MED, 4060, 300, 500],
            [Plataforma.METAL2_MED, 5100, 300, 500],
        ]
        for plataforma in nivelArriba:
            bloque = PlataformaEnMovimiento(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.limite_superior = 100
            bloque.limite_inferior = plataforma[3]
            bloque.cambio_y = - 5
            bloque.jugador = self.jugador
            bloque.nivel = self
            self.listade_plataformas.add(bloque)

        # agregamos una plataforma en movimiento hacia los lados
        bloque = PlataformaEnMovimiento(Plataforma.METAL2_MED)
        bloque.rect.x = 1350
        bloque.rect.y = 130
        bloque.limite_izquierda = 1250
        bloque.limite_derecha = 1600
        bloque.cambio_x = 3
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.listade_plataformas.add(bloque)

        # agregamos una plataforma en movimiento hacia los lados
        bloque = PlataformaEnMovimiento(Plataforma.METAL2_MED)
        bloque.rect.x = 3350
        bloque.rect.y = 130
        bloque.limite_izquierda = 2600
        bloque.limite_derecha = 3500
        bloque.cambio_x = 3
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.listade_plataformas.add(bloque)

        # agregamos una plataforma en movimiento hacia los lados
        bloque = PlataformaEnMovimiento(Plataforma.METAL2_MED)
        bloque.rect.x = 4850
        bloque.rect.y = 130
        bloque.limite_izquierda = 4750
        bloque.limite_derecha = 5250
        bloque.cambio_x = 3
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.listade_plataformas.add(bloque)

        cervezas = [
            [750, 460],
            [600, 120],
            [1300, 50],
            [1900, 50],
            [2100, 100],
            [2300, 100],
            [2500, 100],
            [2850, 375],
            [2950, 95],
            [3100, 375],
            [3800, 400],
            [3600, 50],
            [3700, 50],
            [3800, 50],

            [4240, 200],
            [4645, 110],
            [5470, 430],
        ]

        # Iteramos a través del array anterior y añadimos cervezas
        for lista in cervezas:
            cerveza = Cerveza()
            cerveza.rect.x = lista[0]
            cerveza.rect.y = lista[1]
            self.listade_vidasHomero.add(cerveza)

        almas = [
            [550, 450],
            [600, 450],
            [650, 450],
            [600, 300],
            [650, 300],
            [700, 300],
            [600, 200],
            [650, 200],
            [700, 200],
            [1000, 200],
            [1050, 200],
            [1100, 200],
            [1150, 200],
            [1200, 200],
            [950, 50],
            [1000, 50],
            [1050, 50],
            [2000, 100], [2050, 100], [2100, 100], [2150, 100], [2200, 100], [2250, 100], [2300, 100], [2350, 100], [2400, 100], [2450, 100],
            [2000, 200], [2050, 200], [2100, 200], [2150, 200], [2200, 200], [2250, 200], [2300, 200], [2350, 200], [2400, 200], [2450, 200],
            [1300, 330], [1450, 230], [1600, 130],
            [2900, 300], [2950, 300], [3000, 300],
            [3650, 150], [3700, 150], [3750, 150], [3800, 150], [3850, 150], [3900, 150],
            [4195, 150],
            [4295, 150],
            [4210, 360], [4260, 360], [4310, 360], [4160, 360],
            [4390, 60], [4450, 60], [4510, 60], [4550, 60],
            [4760, 200], [4820, 200], [4880, 200], [4940, 200],
            [2700, 20], [2750, 20], [2800, 20], [2850, 20], [3050, 60], [3100, 60], [3150, 60], [3200, 60], [3250, 60],
            [5300, 60], [5360, 60], [5420, 60],  [5480, 60], [5540, 60], [5600, 60], [5660, 60], [5720, 60], [5780, 60], [5840, 60], [5900, 60],  [59600, 60],
            [5320, 440], [5420, 440], [5520, 440], [5620, 440],
        ]
        # Iteramos a través del array anterior y añadimos almas
        for lista in almas:
            alma = Almas(self.matrizAlmas)
            alma.rect.x = lista[0]
            alma.rect.y = lista[1]
            self.listade_almasHomero.add(alma)

        lsfuego = [
            [1150, 500],
            [1350, 500],
            [1550, 500],
            [1750, 500],
            [1850, 500],
            [2200, 500],
                [5000, 500],
                [5200, 500],
                [5400, 500],
                [5550, 500],
        ]
        for lista in lsfuego:
            fuego = Fuego()
            fuego.rect.x = lista[0]
            fuego.rect.y = lista[1]
            self.listade_fuego.add(fuego)

        # Iteramos a través del array anterior y añadimos enemigos
        for i in range(50):
            self.enemigo1 = Enemigos1(self.matrizEnemigo1)
            self.enemigo1.rect.x = i * 1000
            self.enemigo1.rect.y = 480
            self.listade_enemigos1.add(self.enemigo1)

        # Iteramos a través del array anterior y añadimos enemigos
        for i in range(100):
            self.enemigo2 = Enemigos2(self.matrizEnemigo2)
            self.enemigo2.rect.x = i * 500
            self.enemigo2.rect.y = 505
            self.listade_enemigos2.add(self.enemigo2)

        enemigos3 = [
            [1010, 280],
            [1120, 50],
            [3050, 320],
            [3970, 110]
        ]
        # Iteramos a través del array anterior y añadimos enemigos
        for lista in enemigos3:
            self.enemigo3 = Enemigos3(self.matrizEnemigo3)
            self.enemigo3.rect.x = lista[0]
            self.enemigo3.rect.y = lista[1]
            self.listade_enemigos3.add(self.enemigo3)
            self.listade_dracula.append(self.enemigo3)

        # sprite de salida
        salir = Exit()
        self.listade_exit.add(salir)
        self.listade_salidas.append(salir)

        puerta = Puerta()
        puerta.rect.x = 6500
        puerta.rect.y = 480
        self.listade_puerta.add(puerta)
        self.listade_puertas.append(puerta)




    print("Nivel 1 READY")


class Nivel_02(Nivel):

    def __init__(self, jugador, enemigo, enemigo2, enemigo3, almas):
        """ Creamos el nivel 1. """

        # Llamamos al constructor padre
        Nivel.__init__(self, jugador, enemigo, enemigo2, enemigo3, almas)

        self.fondoEscalado = pygame.image.load('imagenes/batallaFlanders.jpg')
        self.limitedel_nivel_final = -2000


        self.flanders = EnemigoFlanders()
        self.flanders.rect.x = 800
        self.flanders.rect.y = 50
        self.listade_Flanders.add(self.flanders)


        bloque = PlataformaEnMovimiento(Plataforma.METAL2_MED)
        bloque.rect.x = 100
        bloque.rect.y = 400
        bloque.limite_superior = 100
        bloque.limite_inferior = 500
        bloque.cambio_y = - 5
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.listade_plataformas.add(bloque)

        bloque = PlataformaEnMovimiento(Plataforma.METAL2_MED)
        bloque.rect.x = 850
        bloque.rect.y = 400
        bloque.limite_superior = 100
        bloque.limite_inferior = 500
        bloque.cambio_y = - 5
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.listade_plataformas.add(bloque)

        nivel2 = [
            [Plataforma.VERDEROCA, 250, 450],
             [Plataforma.VERDEROCA, 350, 350],
              [Plataforma.VERDEROCA, 450, 270],
               [Plataforma.VERDEROCA, 600, 350],
                [Plataforma.VERDEROCA, 700, 450],
           ]

        # Iteramos a través del array anterior y añadimos plataformas
        for plataforma in nivel2:
            bloque = Plataforma(plataforma[0])
            # print(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.listade_plataformas.add(bloque)

        cervezas = [
            [350, 300],
            [450, 200],
            [600, 300],
        ]
        # Iteramos a través del array anterior y añadimos cervezas
        for lista in cervezas:
            cerveza = Cerveza()
            cerveza.rect.x = lista[0]
            cerveza.rect.y = lista[1]
            self.listade_vidasHomero.add(cerveza)