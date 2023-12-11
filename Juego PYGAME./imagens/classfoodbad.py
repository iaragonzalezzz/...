import pygame
from constantes import *
import random
from imagenes import *

class ComidaMala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        numero_comida_mala = random.randint(0, len(bad) - 1)
        self.image = bad[numero_comida_mala]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
        self.rect.y = 0
        self.velocidad_base = 3
        self.velocidad = self.velocidad_base

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO_VENTANA:
            self.kill()

