import pygame
from constantes import *
import json
from textbox import TextBox1
from estado_juego import estado_juego
from pou import * 
from classfoodbad import *
from classfood import *


pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("juego")

def imagen_fondo():
    imagen_fondo = pygame.image.load("/Users/iargonzalez/Desktop/Trabajos facu/Juego PYGAME./imagens/imagen fondo de menu.jpeg")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    return imagen_fondo

def imagen_fondo_juego():
    imagen_fondo = pygame.image.load("Juego PYGAME./imagens/FondoFlappyBird.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    return imagen_fondo

def fin_juego(estado_juego):

    flag_ejecutar_fin_juego = True
    while flag_ejecutar_fin_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_fin_juego = False
        pygame.display.set_caption("FOOD DROP")
        fuente = pygame.font.SysFont("Arial", 100)
        texto_ganaste= fuente.render("Ganaste", True , COLOR_NEGRO)
        imagen = imagen_fondo_juego
        pantalla.blit(imagen,imagen.get_rect())
        pantalla.blit(texto_ganaste,(250,300))
        estado_juego.actualizar_progreso()
        estado_juego.guardar_progreso()
        pygame.display.flip()
    pygame.quit()

def fin_nivel_tres (estado_juego):
    pygame.display.set_caption("JUEGO")
    fuente = pygame.font.SysFont("Arial", 100)
    texto_perdiste = fuente.render("Game over ",True, COLOR_AZUL)
    imagen = imagen_fondo()
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_perdiste,(250,300))
    estado_juego.actualizar_progreso()
    estado_juego.guardar_progreso()
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()

def siguiente_nivel(proximo_nivel , estado_juego):
    pygame.display.set_caption("FOOD DROP")
    imagen = imagen_fondo()
    fuente = pygame.font.SysFont("Arial", 50)
    texto_ganaste = fuente.render("¡BIEN! Ganaste este nivel", True , COLOR_NEGRO)
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_ganaste,(250,300))
    pygame.display.flip()
    pygame.time.delay(3000)
    proximo_nivel(estado_juego)

def fin_nivel (siguiente_nivel,estado_juego):
    pygame.display.set_caption("FOOD DROP")
    imagen = imagen_fondo()
    fuente = pygame.font.SysFont("Arial", 50)
    texto_perdiste = fuente.render("¡MALA SUERTE! Perdiste." , True , COLOR_NEGRO)
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_perdiste,(250,300))
    pygame.display.flip()
    pygame.time.delay(3000)
    siguiente_nivel(estado_juego)

def nivel_uno(estado_juego , self):

    flag_ejecutar_jugar = True

    while flag_ejecutar_jugar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar = False

            pygame.init()
            pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
            imagen_fondo = pygame.image.load("Juego PYGAME./imagens/FondoFlappyBird.png")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("FOOD DROP")

            flag_correr = True  # bandera inical del juego
            tiempo = pygame.USEREVENT 
            pygame.time.set_timer(tiempo , 1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje), True, COLOR_NEGRO)#PUNTOS

            personaje = Pou()
            comida_buena = Comida()
            comida_mala = ComidaMala()
            vidas = 3
            velocidad = velocidad_base
            velocidad_base = 3
            score = 0
            incrementacion_score = 10

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos:
                    #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    teclas = pygame.key.get_pressed()
                    velocidad_movimiento = 8  # Ajusta este valor para cambiar la velocidad de movimiento

                    if teclas[pygame.K_LEFT] and self.rect.left > 0:
                        self.rect.x -= velocidad_movimiento
                        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO_VENTANA:
                            self.rect.x += velocidad_movimiento

                        if self.boca_timer > 0:
                            self.boca_timer -= 1
                    else:
                        self.boca_abierta = not self.boca_abierta
                        self.image = self.images[int(self.boca_abierta)]
                        self.boca_timer = 10
                
                        rectangulo_boca_pou = self.pou.rectangulo_boca()

        for comida in comida_sprites:
            if comida.rect.colliderect(rectangulo_boca_pou):
                # El Pou atrapó la comida
                score = score + incrementacion_score
                comida.kill()  # Eliminar la comida atrapada
            elif comida.rect.bottom >= ALTO_VENTANA:
                # La comida tocó el suelo y no fue atrapada
                vidas = vidas - 1
                comida.kill()  # Eliminar la comida que tocó el suelo

                if (score > 100):
                    nivel_dos ()
                elif (vidas <= 0):
                    fin_juego()

                personaje.mostrar_personaje(pantalla)
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 

                siguiente_nivel(nivel_dos , estado_juego)

                pygame.display.flip()

            pygame.quit()
        
def  nivel_dos(estado_juego , self):
    flag_ejecutar_jugar_nivel_2 = True

    while flag_ejecutar_jugar_nivel_2:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar_nivel_2 = False

            imagen_fondo = pygame.image.load("Juego PYGAME./fondo_nivel_dos.avif")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("FOOD DROP")

            flag_correr = True  # bandera inical del juego

            tiempo = pygame.USEREVENT
            pygame.time.set_timer(tiempo,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_NEGRO)

            personaje = Pou()
            comida_buena = Comida()
            comida_mala = ComidaMala()
            vidas = 3
            velocidad = velocidad_base
            velocidad_base = 4
            score = 0
            incrementacion_score = 10

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos:
                    #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False


                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    teclas = pygame.key.get_pressed()
                    velocidad_movimiento = 8  # Ajusta este valor para cambiar la velocidad de movimiento

                    if teclas[pygame.K_LEFT] and self.rect.left > 0:
                        self.rect.x -= velocidad_movimiento
                        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO_VENTANA:
                            self.rect.x += velocidad_movimiento

                        if self.boca_timer > 0:
                            self.boca_timer -= 1
                    else:
                        self.boca_abierta = not self.boca_abierta
                        self.image = self.images[int(self.boca_abierta)]
                        self.boca_timer = 10
                
                        rectangulo_boca_pou = self.pou.rectangulo_boca()

            for comida in comida_sprites:
                if comida.rect.colliderect(rectangulo_boca_pou):
                    # El Pou atrapó la comida
                    score = score + incrementacion_score
                    comida.kill()  # Eliminar la comida atrapada
                elif comida.rect.bottom >= ALTO_VENTANA:
                    # La comida tocó el suelo y no fue atrapada
                    vidas = vidas - 1
                    comida.kill()  # Eliminar la comida que tocó el suelo

                    if (score > 200):
                        nivel_tres ()
                    elif (vidas <= 0):
                        fin_juego()

                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
                personaje.mostrar_personaje(pantalla)
                pantalla.blit(texto_puntos,(50,50))

                siguiente_nivel(nivel_tres , estado_juego)

                pygame.display.flip()

            pygame.quit()

def nivel_tres(estado_juego , self):
    flag_ejecutar_jugar_nivel_3 = True

    while flag_ejecutar_jugar_nivel_3:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar_nivel_3 = False

            imagen_fondo = pygame.image.load("Juego PYGAME./fondo_nivel_tres.avif")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("FOOD DROP")

            flag_correr = True  # bandera inical del juego

            tiempo = pygame.USEREVENT
            pygame.time.set_timer(tiempo,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_NEGRO)

            personaje = Pou()
            comida_buena = Comida()
            comida_mala = ComidaMala()
            vidas = 3
            velocidad = velocidad_base
            velocidad_base = 4
            score = 0
            incrementacion_score = 10

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos: #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    teclas = pygame.key.get_pressed()
                    velocidad_movimiento = 8  # Ajusta este valor para cambiar la velocidad de movimiento

                    if teclas[pygame.K_LEFT] and self.rect.left > 0:
                        self.rect.x -= velocidad_movimiento
                        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO_VENTANA:
                            self.rect.x += velocidad_movimiento

                        if self.boca_timer > 0:
                            self.boca_timer -= 1
                    else:
                        self.boca_abierta = not self.boca_abierta
                        self.image = self.images[int(self.boca_abierta)]
                        self.boca_timer = 10
                
                        rectangulo_boca_pou = self.pou.rectangulo_boca()

            for comida in comida_sprites:
                if comida.rect.colliderect(rectangulo_boca_pou):
                    # El Pou atrapó la comida
                    score = score + incrementacion_score
                    comida.kill()  # Eliminar la comida atrapada
                elif comida.rect.bottom >= ALTO_VENTANA:
                    # La comida tocó el suelo y no fue atrapada
                    vidas = vidas - 1
                    comida.kill()  # Eliminar la comida que tocó el suelo

                    if evento.type == pygame.USEREVENT:
                        if evento.type == tiempo:
                            if fin_tiempo == False:
                                segundos = segundos - 1
                                if segundos == 0:
                                    fin_tiempo = True


                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 


                if (score > 300):
                    fin_nivel_tres(estado_juego)
                if (vidas <= 0):
                    fin_juego(estado_juego)

                pygame.display.flip()

            pygame.quit()

def cargar_nombre(estado_juego) :
    pygame.display.set_caption("Options")
    textbox = TextBox1(150,100,600,400,"Arial","Juego PYGAME./boton.png")

    flag_ejecutar_opciones = True 

    while flag_ejecutar_opciones:
        lista_evento = pygame.event.get()
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                flag_ejecutar_opciones = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 500 < posicion_click[1] < 600:
                    estado_juego.nombre = textbox.obtener_texto()
                    estado_juego.guardar_progreso()
                    (estado_juego)

        pantalla.fill(COLOR_BLANCO)
        pygame.draw.rect(pantalla, COLOR_NEGRO, (580, 500, 200, 100))
        fuente = pygame.font.SysFont("Arial", 25)
        texto_jugar = fuente.render("Jugar", True, COLOR_BLANCO)
        pantalla.blit(texto_jugar, (640, 540))
        textbox.update(pantalla,lista_evento)
        pygame.display.flip()

    pygame.quit()

def ordenar_puntaje(lista: list, clave: str): 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][1][clave] < lista[j][1][clave]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista
def ranking():
    pygame.display.set_caption("Options")
    imagen = imagen_fondo()
    flag_ejecutar_ranking = True 

    with open('archivo.json', 'r') as file:
        datos_ranking = json.load(file)

        lista_ranking = list(datos_ranking.items())
        ranking_ordenado =  ordenar_puntaje(lista_ranking , "puntaje")

    while flag_ejecutar_ranking:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_ranking = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                print(posicion_click)

                if  470  > posicion_click[0] > 347 and posicion_click[0] and 611 < posicion_click[1] < 645:
                    flag_ejecutar_ranking = False
                    menu()

        pantalla.blit(imagen,imagen.get_rect())
        fuente = pygame.font.SysFont("Gabriola", 60)
        fuente_titulo = pygame.font.SysFont("Gabriola", 80)
        texto_ranking = fuente_titulo.render("Ranking", True, COLOR_NEGRO)
        texto_volver = fuente.render("Volver", True, COLOR_NEGRO)
        pantalla.blit(texto_ranking,(350,100))
        pantalla.blit(texto_volver,(350, 600))
        y_pos = 250  

        # Mostrar los primeros 5 jugadores en el ranking
        for i in range(5):
            id = i + 1
            nombre = ranking_ordenado[i][0]
            jugador = ranking_ordenado[i][1]
            texto_jugador = fuente.render("{0}. {1}: {2}".format(id,nombre,jugador['puntaje']), True, COLOR_NEGRO)
            pantalla.blit(texto_jugador, (300, y_pos))
            y_pos += 50  

        pygame.display.flip()

    pygame.quit()
def menu():
    pygame.display.set_caption("menu")
    flag_ejecutar_menu = True
    imagen = imagen_fondo()
    pantalla.blit(imagen,imagen.get_rect())
    while flag_ejecutar_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_menu = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 100 < posicion_click[1] < 200:
                    ranking()
                if posicion_click[0] > 580 and posicion_click[0] < 780 and 300 < posicion_click[1] < 400:
                    cargar_nombre(estado_juego)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 500 < posicion_click[1] < 600:
                    flag_ejecutar_menu = False
        
        pygame.draw.rect(pantalla, COLOR_NEGRO, (580, 100, 200, 100))
        pygame.draw.rect(pantalla, COLOR_NEGRO, (580, 300, 200, 100))
        pygame.draw.rect(pantalla, COLOR_NEGRO, (580, 500, 200, 100))
        fuente = pygame.font.SysFont("Arial", 25)
        texto_ranking = fuente.render("Ranking", True, COLOR_BLANCO)
        texto_jugar = fuente.render("Iniciar juego", True, COLOR_BLANCO)
        texto_salir = fuente.render("Salir", True, COLOR_BLANCO)
        pantalla.blit(texto_ranking, (620, 140))
        pantalla.blit(texto_jugar, (610, 330))
        pantalla.blit(texto_salir, (620, 540))
        pygame.display.flip()

menu()
pygame.quit()