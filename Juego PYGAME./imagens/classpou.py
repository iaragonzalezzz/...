import pygame
from constantes import *
from pou import *
from imagenes import *


class Pou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = sprites_pou
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA - 50))
        self.rect.inflate_ip(-10, -20)
        self.vidas = 3
        self.puntuacion = 0
        self.boca_abierta = False
        self.boca_timer = 0

    def update(self):
        self.mover()
        self.actualizar_boca()

    def mover(self):
        teclas = pygame.key.get_pressed()
        velocidad_movimiento = 8

        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= velocidad_movimiento
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO_VENTANA:
            self.rect.x += velocidad_movimiento

    def actualizar_boca(self):
        if self.boca_timer > 0:
            self.boca_timer -= 1
        else:
            self.boca_abierta = not self.boca_abierta
            self.image = self.images[int(self.boca_abierta)]
            self.boca_timer = 10

    def rectangulo_boca(self):
        rectangulo_boca = self.rect.inflate(-10, -20)
        if not self.boca_abierta:
            rectangulo_boca.move_ip(5, 0)
        return rectangulo_boca
    

    