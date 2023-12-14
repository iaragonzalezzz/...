import pygame
import random
from constantes import *
from imagenes import *


pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

class Pou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("arch.imagenes/img_pou_1.png")
        self.rect = self.image.get_rect()
        # Atributo
        self.rect.topleft = (ANCHO_VENTANA // 2, ALTO_VENTANA - 100)
        # Atributo
        self.velocidad = 10
        # Atributo
        self.vidas = 3

    # Metodo
    def actualizar(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO_VENTANA - self.rect.width:
            self.rect.x = ANCHO_VENTANA - self.rect.width

    # Metodo
    def cambiar_imagen(self, numero_imagen):
        self.image = pygame.image.load(f"arch.imagenes/img_pou_{numero_imagen}.png")


class ComidaBuena(pygame.sprite.Sprite):
    def __init__(self, food, velocidad_comida):
        super().__init__()
        self.imagenes = food  
        self.image = random.choice(self.imagenes)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, ANCHO_VENTANA - self.rect.width), 0)
        self.velocidad = velocidad_comida

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO_VENTANA:
            self.reset()

    def reset(self):
        self.image = random.choice(self.imagenes)
        self.rect.topleft = (random.randint(0, ANCHO_VENTANA - self.rect.width), 0)

class ComidaMala(pygame.sprite.Sprite):
    def __init__(self, bad, velocidad_comida):
        self.imagenes = bad
        super().__init__()
        self.image = random.choice(self.imagenes)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, ANCHO_VENTANA - self.rect.width), 0)
        self.velocidad = velocidad_comida

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO_VENTANA:
            self.reset()

    def reset(self):
        self.image = random.choice(self.imagenes)
        self.rect.topleft = (random.randint(0, ANCHO_VENTANA - self.rect.width), 0)


#sonidos
comida_buena_s = pygame.mixer.Sound("sonidos/comida_buena.mp3")
comida_mala_s = pygame.mixer.Sound("sonidos/comida_mala.mp3")
game_over_s = pygame.mixer.Sound("sonidos/game_over.mp3")

#sprites
todos_los_sprites = pygame.sprite.Group()
pou = Pou()
comida_buena = ComidaBuena(food, velocidad_comida = 3)
comida_mala = ComidaMala(bad, velocidad_comida = 3)
todos_los_sprites.add(pou, comida_buena, comida_mala)




