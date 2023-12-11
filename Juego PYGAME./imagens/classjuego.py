import pygame
from constantes import *
from classpou import *
from estado_juego import *
class Juego:
    def __init__(self):
        self.todos_sprites = pygame.sprite.Group() #almacena sprites en general
        self.comida_sprites = pygame.sprite.Group() #almacena sprites de la comida
        self.pou = Pou() #agrega al pou a los sprites
        self.todos_sprites.add(self.pou)
        self.reloj = pygame.time.Clock() #controla la velocidad de actualización del juego.
        self.evento_generar_comida = pygame.USEREVENT + 1
        pygame.time.set_timer(self.evento_generar_comida, 3000) #lo que genera la comida de nuevo
        self.incremento_puntuacion = 10 #se suma de a 10 el score
        vida_pou = 3
        self.en_juego = False
        self.flag_ejecutar_ranking = True
        self.tiempo_inicial = pygame.time.get_ticks() #rastrear el tiempo transcurrido desde el inicio del juego
        self.tiempo_juego = 0  
        self.estado_juego = Estado_juego()