import pygame
import random
import sys
import json
from constantes import *
from imagenes import *
from classpou import Pou
from classjuego import Juego
from classfood import *
from classfoodbad import *

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Food Drop")

#se carga la musica
pygame.mixer.music.load("Juego PYGAME./imagens/Y2meta.app - Soundtrack from Pou _-_ - Food Drop (Good Quality) (128 kbps).mp3")
pygame.mixer.music.set_volume(0.3)

def cargar_musica(self):
        pygame.mixer.music.load("Juego PYGAME./imagens/Y2meta.app - Soundtrack from Pou _-_ - Food Drop (Good Quality) (128 kbps).mp3")
        pygame.mixer.music.set_volume(0.5)


def mostrar_menu_opciones(self):
        fondo_menu = pygame.image.load("/Users/iargonzalez/Desktop/Trabajos facu/Juego PYGAME./imagens/imagen fondo de menu.jpeg")
        fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))
        pantalla.blit(fondo_menu, (0, 0))

        fuente_titulo = pygame.font.Font(None, 75)
        texto_titulo = fuente_titulo.render("Food Drop", True, COLOR_MAGENTA)
        pantalla.blit(texto_titulo, (ANCHO_VENTANA // 2 - texto_titulo.get_width() // 2, ALTO_VENTANA // 4))

        fuente_opciones = pygame.font.Font(None, 36)
        texto_empezar = fuente_opciones.render("1. Empezar juego", True, COLOR_MAGENTA)
        texto_ranking = fuente_opciones.render("2. Ranking de puntuaciones", True, COLOR_MAGENTA)
        texto_salir = fuente_opciones.render("3. Salir", True, COLOR_MAGENTA)

        pantalla.blit(texto_empezar, (ANCHO_VENTANA // 2 - texto_empezar.get_width() // 2, ALTO_VENTANA // 2))
        pantalla.blit(texto_ranking, (ANCHO_VENTANA // 2 - texto_ranking.get_width() // 2, ALTO_VENTANA // 2 + 50))
        pantalla.blit(texto_salir, (ANCHO_VENTANA // 2 - texto_salir.get_width() // 2, ALTO_VENTANA // 2 + 100))

        pygame.display.flip()

        esperando_tecla = True
        while esperando_tecla:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.en_juego = True
                        self.reset_juego()
                        esperando_tecla = False
                    elif evento.key == pygame.K_2:
                        self.mostrar_ranking()
                    elif evento.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()


        
def run(self):
        self.mostrar_menu_opciones()
        self.cargar_musica()
        pygame.mixer.music.play(-1) 

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == self.evento_generar_comida and self.en_juego:   #verifica que sea ese evento  
                    comida = Comida() #objeto que va a representar la comida
                    comida.velocidad = self.dificultad * 2 #aumenta la dificultad
                    self.todos_sprites.add(comida) #agrego la comida a todos los sprites
                    self.comida_sprites.add(comida)
                elif evento.type == self.evento_subir_nivel and self.en_juego:
                    self.subir_nivel()

            if self.en_juego:
                tiempo_actual = pygame.time.get_ticks()
                self.tiempo_juego = tiempo_actual - self.tiempo_inicial

                self.todos_sprites.update()
                self.verificar_colisiones() #verifica si hubo colision

                pantalla.fill(COLOR_BLANCO)
                self.todos_sprites.draw(pantalla)

                fuente = pygame.font.Font(None, 36)
                texto_puntuacion = fuente.render(f"Puntuación: {self.pou.puntuacion}", True, COLOR_NEGRO)
                pantalla.blit(texto_puntuacion, (10, 10))
                texto_vidas = fuente.render(f"Vidas: {self.pou.vidas}", True, COLOR_NEGRO)
                pantalla.blit(texto_vidas, (ANCHO_VENTANA - 150, 10))

                tiempo_segundos = self.tiempo_juego // 1000
                texto_tiempo = fuente.render(f"Tiempo: {tiempo_segundos}s", True, COLOR_NEGRO)
                pantalla.blit(texto_tiempo, (ANCHO_VENTANA // 2 - texto_tiempo.get_width() // 2, 10))

                pygame.display.flip()
                self.reloj.tick(30)  

def subir_nivel(self):
        self.dificultad += 1
        if self.dificultad % 2 == 0:
            self.pou.boca_timer = 30

        pygame.time.set_timer(self.evento_generar_comida, 3000 // self.dificultad)

def verificar_colisiones(self):
        rectangulo_boca_pou = self.pou.rectangulo_boca()
        for comida in self.comida_sprites:
            if comida.rect.colliderect(rectangulo_boca_pou):#Comprueba si hay una colisión entre el rectángulo de la boca del Pou 
                self.pou.puntuacion += self.incremento_puntuacion #
                comida.kill() #
            elif comida.rect.bottom >= ALTO_VENTANA: #si el pou no agarra la comida
                self.pou.vidas -= 1 #descuenta una vida
                comida.kill()

                if self.pou.vidas <= 0:
                    self.mostrar_mensaje("¡PERDISTE, SE TE ACABARON LOS INTENTOS!")
                    self.mostrar_menu_opciones()

        if self.pou.puntuacion >= 100:
            for comida in self.comida_sprites:
                comida.velocidad = self.dificultad * 2
                self.dificultad = 2

        if self.pou.puntuacion >= 200:
            for comida in self.comida_sprites:
                comida.velocidad = self.dificultad * 3
                self.dificultad = 3

def mostrar_mensaje(self, mensaje):
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(mensaje, True, COLOR_NEGRO)
        pantalla.blit(texto, (ANCHO_VENTANA // 2 - len(mensaje) * 10, ALTO_VENTANA // 2))
        pygame.display.flip()
        pygame.time.delay(2000)

        if mensaje.startswith("¡GANASTE!"):
            self.en_juego = False
            self.mostrar_menu_opciones()  # Mostrar el menú de opciones después de ganar
        elif mensaje.startswith("¡PERDISTE!"):
            self.en_juego = False
            self.mostrar_menu_opciones()  # Mostrar el menú de opciones después de perder


def reset_juego(self):
        self.todos_sprites.empty()
        self.comida_sprites.empty()
        self.todos_sprites.add(self.pou)
        self.dificultad = 1
        self.flag_ejecutar_ranking = True
        self.tiempo_inicial = pygame.time.get_ticks()
        self.tiempo_juego = 0



