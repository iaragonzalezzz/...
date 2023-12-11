import pygame
from imagenes import *
from constantes import *
import random

class Comida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        numero_comida = random.randint(0, len(food) - 1)
        self.image = food[numero_comida]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
        self.rect.y = 0
        self.velocidad_base = 3
        self.velocidad = self.velocidad_base

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO_VENTANA:
            self.kill()
