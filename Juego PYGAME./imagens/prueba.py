import pygame
import random
import sys 
from constantes import *

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Food Drop")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Directorio de imágenes
DIRECTORIO_IMAGENES = [
    pygame.image.load("Juego PYGAME./imagens/chicken_leg.png"),
    pygame.image.load("Juego PYGAME./imagens/bacon.png"),
    pygame.image.load("Juego PYGAME./imagens/chocolate_croissant.png"),
    pygame.image.load("Juego PYGAME./imagens/burger.png"),
    pygame.image.load("Juego PYGAME./imagens/avocado_maki.png"),
    pygame.image.load("Juego PYGAME./imagens/candy_cane.png"),
    pygame.image.load("Juego PYGAME./imagens/banana_donut.png"),
    pygame.image.load("Juego PYGAME./imagens/chocolate_balls.png"),
    pygame.image.load("Juego PYGAME./imagens/cherries.png"),
    pygame.image.load("Juego PYGAME./imagens/chocolate_cereal.png"),
    pygame.image.load("Juego PYGAME./imagens/chocolate_cereal.png")
]

bad = [
        pygame.image.load("Juego PYGAME./imagens/avion_pou-removebg-preview-removebg-preview.png") ,
        pygame.image.load("Juego PYGAME./zapa pou.jpeg") ,
        pygame.image.load("Juego PYGAME./pelota pou.webp")
        ] 

class Pou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load("Juego PYGAME./imagens/movimientopouBOCABIERTA-removebg-preview.jpeg"),
            pygame.image.load("Juego PYGAME./imagens/POUbocacerrada-removebg-preview.png")
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)
        self.ancho = 2
        self.alto = 10
        self.vidas = 3
        self.puntuacion = 0
        self.boca_abierta = False
        self.boca_timer = 0
    
    def blitear(self, pantalla):
            pygame.draw.rect(pantalla, (255, 0, 255), self.rect)  # Corregir el uso de draw.rect
            pantalla.blit(self.image, self.rect.topleft)  # Blitear el sprite de Pou


    def update(self):
        teclas = pygame.key.get_pressed()
        velocidad_movimiento = 8  # Ajusta este valor para cambiar la velocidad de movimiento

        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= velocidad_movimiento
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += velocidad_movimiento

        if self.boca_timer > 0:
            self.boca_timer -= 1
        else:
            self.boca_abierta = not self.boca_abierta
            self.image = self.images[int(self.boca_abierta)]
            self.boca_timer = 10

    def rectangulo_boca(self):
        rectangulo_boca = self.rect.inflate(-1, -2)  # Ajuste del tamaño del rectángulo
        if not self.boca_abierta:
            rectangulo_boca.move_ip(5, 0)
        return rectangulo_boca

class Comida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        numero_comida = random.randint(0, len(DIRECTORIO_IMAGENES) - 1)
        self.image = DIRECTORIO_IMAGENES[numero_comida]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = 0
        self.velocidad_base = 3
        self.velocidad = self.velocidad_base
        self.mostrar_comida = True


    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > ALTO:
            self.kill()

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


class Juego:
    def __init__(self):
        self.todos_sprites = pygame.sprite.Group()
        self.comida_sprites = pygame.sprite.Group()
        self.pou = Pou()
        self.todos_sprites.add(self.pou)
        self.dificultad = 1
        self.reloj = pygame.time.Clock()
        self.evento_generar_comida = pygame.USEREVENT + 1
        pygame.time.set_timer(self.evento_generar_comida, 3000)  # Ajuste el tiempo de generación a 3000 ms (3 segundos)
        self.incremento_puntuacion = 10
        self.umbral_intermedio = 100
        self.umbral_dificil = 200
        self.umbral_vidas = 3
        self.evento_subir_nivel = pygame.USEREVENT + 2
        pygame.time.set_timer(self.evento_subir_nivel, 10000)
        self.en_juego = False

    def mostrar_menu_principal(self):
        fondo_menu = pygame.image.load("/Users/iargonzalez/Desktop/Trabajos facu/Juego PYGAME./imagens/imagen fondo de menu.jpeg")
        pantalla.blit(fondo_menu, (0, 0))

        fuente_titulo = pygame.font.Font(None, 72)
        texto_titulo = fuente_titulo.render("Food Drop", True, BLANCO)
        pantalla.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        fuente_instrucciones = pygame.font.Font(None, 36)
        texto_instrucciones = fuente_instrucciones.render("Presiona cualquier tecla para empezar", True, BLANCO)
        pantalla.blit(texto_instrucciones, (ANCHO // 2 - texto_instrucciones.get_width() // 2, ALTO // 2))

        pygame.display.flip()

        esperando_tecla = True
        while esperando_tecla:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    esperando_tecla = False
                    self.en_juego = True
                    self.reset_juego()  # Reiniciar el juego al presionar cualquier tecla

    def run(self):
        self.mostrar_menu_principal()
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == self.evento_generar_comida and self.en_juego:
                    comida = Comida()
                    comida.velocidad = self.dificultad * 2
                    self.todos_sprites.add(comida)
                    self.comida_sprites.add(comida)
                elif evento.type == self.evento_subir_nivel and self.en_juego:
                    self.subir_nivel()

            self.todos_sprites.update()
            self.verificar_colisiones()

            # Dibujar
            pantalla.fill(BLANCO)
            self.todos_sprites.draw(pantalla)

            # Mostrar puntuación y vidas
            fuente = pygame.font.Font(None, 36)
            texto_puntuacion = fuente.render(f"Puntuación: {self.pou.puntuacion}", True, NEGRO)
            pantalla.blit(texto_puntuacion, (10, 10))
            texto_vidas = fuente.render(f"Vidas: {self.pou.vidas}", True, NEGRO)
            pantalla.blit(texto_vidas, (ANCHO - 150, 10))

            pygame.display.flip()
            self.reloj.tick(30)

    def subir_nivel(self):
        self.dificultad += 1
        if self.dificultad % 2 == 0:
            self.pou.boca_timer = 30  # Cambiar el tiempo de cambio de boca

        pygame.time.set_timer(self.evento_generar_comida, 3000 // self.dificultad)  # Ajustar la frecuencia de generación

        if self.dificultad > 3:
            self.dificultad = 3

    def verificar_colisiones(self):
        rectangulo_boca_pou = self.pou.rectangulo_boca()

        for comida in self.comida_sprites:
            if comida.rect.colliderect(rectangulo_boca_pou):
                # El Pou atrapó la comida
                self.pou.puntuacion += self.incremento_puntuacion
                comida.kill()  # Eliminar la comida atrapada
            elif comida.rect.bottom >= ALTO:
                # La comida tocó el suelo y no fue atrapada
                self.pou.vidas -= 1
                comida.kill()  # Eliminar la comida que tocó el suelo

                if self.pou.vidas <= 0:
                    self.mostrar_mensaje("¡PERDISTE, SE TE ACABARON LOS INTENTOS!")
                    self.reset_juego()

        if self.pou.puntuacion >= 100:
            for comida in self.comida_sprites:
                comida.velocidad = self.dificultad * 2

        if self.pou.puntuacion >= 300:  # Cambio del puntaje final necesario para ganar
            self.mostrar_mensaje("¡GANASTE! Presiona cualquier tecla para volver al menú principal")

        if self.pou.puntuacion >= self.umbral_intermedio:
            self.dificultad = 2
            self.umbral_intermedio = self.umbral_dificil  # Ajustar el umbral para dificultad intermedia
        if self.pou.puntuacion >= self.umbral_dificil:
            self.dificultad = 3

    def verificar_colisiones_malas(self):
        rectangulo_boca_pou = self.pou.rectangulo_boca()

        for comida in self.comida_sprites:
            if comida.rect.colliderect(rectangulo_boca_pou):
                # El Pou atrapó la comida
                self.pou.puntuacion += self.incremento_puntuacion
                comida.kill()  # Eliminar la comida atrapada
            elif comida.rect.bottom >= ALTO:
                # La comida tocó el suelo y no fue atrapada
                self.pou.vidas -= 1
                comida.kill()  # Eliminar la comida que tocó el suelo

                if self.pou.vidas <= 0:
                    self.mostrar_mensaje("¡PERDISTE, SE TE ACABARON LOS INTENTOS!")
                    self.reset_juego()

        # Incrementar la velocidad de caída de la comida cuando se alcanza una puntuación de 100
        if self.pou.puntuacion >= 100:
            for comida in self.comida_sprites:
                comida.velocidad = self.dificultad * 2

        if self.pou.puntuacion >= 300:  # Cambio del puntaje final necesario para ganar
            self.mostrar_mensaje("¡GANASTE! Presiona cualquier tecla para volver al menú principal")

        if self.pou.puntuacion >= self.umbral_intermedio:
            self.dificultad = 2
            self.umbral_intermedio = self.umbral_dificil  # Ajustar el umbral para dificultad intermedia
        if self.pou.puntuacion >= self.umbral_dificil:
            self.dificultad = 3

    def mostrar_mensaje(self, mensaje):
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(mensaje, True, NEGRO)
        pantalla.blit(texto, (ANCHO // 2 - len(mensaje) * 10, ALTO // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Mostrar el mensaje durante 2 segundos
        if mensaje.startswith("¡GANASTE!"):
            self.en_juego = False
            self.mostrar_menu_principal()
            self.reset_juego()

    def reset_juego(self):
        self.todos_sprites.empty()
        self.comida_sprites.empty()
        self.pou = Pou()
        self.todos_sprites.add(self.pou)
        self.dificultad = 1
        self.boca_abierta = False
        self.incremento_puntuacion = 10
        self.umbral_intermedio = 100
        self.umbral_dificil = 200
        self.umbral_vidas = 3
        self.evento_subir_nivel = pygame.USEREVENT + 2
        pygame.time.set_timer(self.evento_subir_nivel, 10000)

if __name__ == "__main__":
    juego = Juego()
    juego.run()


