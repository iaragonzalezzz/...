import pygame
import random
from constantes import *
from personajes import *
import sqlite3
import sys

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("FOOD DROP")

def imagen_fondo():
    imagen_fondo = pygame.image.load("/Users/iargonzalez/Desktop/Trabajos facu/Juego PYGAME./imagens/imagen fondo de menu.jpeg")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    return imagen_fondo

with sqlite3.connect('base_puntajes.db') as conexion:
    try:
        sentencia = '''create table puntos
        (
        id integer primary key autoincrement, nombre text, puntaje int    
        )
        '''
        conexion.execute(sentencia)
        print('Se creo la tabla de puntos')

    except sqlite3.OperationalError:
        print('La tabla de puntos existe!!')

    def cerrar_conexion(conexion):
        if conexion:
            conexion.close()

conexion = sqlite3.connect('base_puntajes.db')


    #INSERT
def guardar_datos(nombre_usuario:str, puntos:int):
        try:
            conexion.execute('INSERT into puntos(nombre,puntaje) values (?,?)', (nombre_usuario, puntos))
            conexion.commit()
            print("guardo datos en base")
        except:
            print('error')
    
    #SELECT
def obtener_datos():
        cursor = conexion.execute("SELECT * FROM PUNTOS order by puntaje desc LIMIT 3")
        datos = [{'nombre': fila[1], 'puntos': fila[2]} for fila in cursor]

        return datos
    
def mostrar_datos():
        corriendo = True

        while corriendo:
            pantalla.fill((COLOR_AZUL))
            fuente = pygame.font.SysFont("Arial", 50)   
            text = fuente.render("Ranking", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (400, 100)
            pantalla.blit(text, textRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        corriendo = False
                        menu()

            # Muestra los puntajes en la pantalla
            puntajes = obtener_datos()
            for i, puntaje in enumerate(puntajes):
                fuente = pygame.font.SysFont("Arial", 50)
                texto_puntaje = fuente.render(f"{i + 1}. Nombre: {puntaje['nombre']}, Puntos: {puntaje['puntos']}", True, (0, 0, 0))

                pantalla.blit(texto_puntaje, (ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 - 100 + i * 100))

            pygame.display.update()

        pygame.quit()

def score():
    global puntos 
    fuente = pygame.font.SysFont("Arial", 50)   
    texto = fuente.render("puntos: " + str(puntos), True, (0, 0, 0))
    textoRect = texto.get_rect()
    textoRect.center = (1000, 40)
    pantalla.blit(texto, textoRect)

def ganaste():
    corriendo = True

    guardar_datos(nombre_usuario, puntos)

    while corriendo:

        pantalla.fill((255, 255, 255))
        fuente = pygame.font.SysFont("Arial", 50)
        texto_ganaste = fuente.render('Ganaste! Presiona ESC para volver al menú', True, (0, 0, 0))
        score = fuente.render("Tu Puntaje: " + str(puntos), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        pantalla.blit(score, scoreRect)
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ALTO_VENTANA // 2, ANCHO_VENTANA // 2)
        pantalla.blit(texto_ganaste, ganasteRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()

        pygame.display.update()

def ingresar_usuario():
    global nombre_usuario
    corriendo = True
    nombre_usuario = " "

    while corriendo:
        imagen_fondo = pygame.image.load("Pou.PYGAME./arch.imagenes/fondo_usua.jpeg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        pantalla.blit(imagen_fondo, (0, 0))
        fuente = pygame.font.SysFont("Arial", 25)
        texto_ingreso = fuente.render("Ingresar nombre del jugador:", True, (0, 0, 0))
        pantalla.blit(texto_ingreso, (ANCHO_VENTANA // 2 - 250, ALTO_VENTANA // 3))
        input_rect = pygame.Rect(ANCHO_VENTANA // 2 - 100, ALTO_VENTANA // 3 + 30, 200, 30)
        pygame.draw.rect(pantalla, (0, 0, 0), input_rect, 2)
        texto_input = fuente.render(nombre_usuario, True, (0, 0, 0))
        pantalla.blit(texto_input, (input_rect.x + 5, input_rect.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    corriendo = False
                    menu()

                elif event.key == pygame.K_RETURN:
                    if nombre_usuario:
                        corriendo = False
                        nivel_uno()
                        return nombre_usuario
                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += event.unicode
        
        pygame.display.update()
    
    pygame.quit()       

    return nombre_usuario   

def pasar_nivel():
    global corriendo, nivel_actual
    
    corriendo = True
    
    while corriendo:
        pantalla.fill((255, 255, 255))
        fuente = pygame.font.SysFont("Arial", 50)
        texto_ganaste = fuente.render('Pasaste al siguiente nivel! Presiona Enter para continuar o ESC para volver al menú', True, (0, 0, 0))
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
        pantalla.blit(texto_ganaste, ganasteRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nivel_actual == 1:
                        nivel_dos()
                    elif nivel_actual == 2:
                        nivel_tres()
                elif event.key == pygame.K_ESCAPE:
                    menu()

        pygame.display.update()
    pygame.quit()

def mostrar_gameover():
    corriendo_go = True
    guardar_datos(nombre_usuario, puntos)

    while corriendo_go:
        pantalla.fill((255, 255, 255))

        fuente = pygame.font.SysFont("Arial", 40)
        text = fuente.render("Game Over", True, (0, 0, 0))
        score = fuente.render("Tu Puntaje: " + str(puntos), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (ALTO_VENTANA // 2, ANCHO_VENTANA // 2 + 50)
        pantalla.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
        pantalla.blit(text, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo_go = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    corriendo_go = False
                    reiniciar_juego()

        pygame.display.update()
        
    pygame.quit()

def reiniciar_juego():
    global puntos
    puntos = 300
    menu()

def nivel_tres():
    global puntos, nivel_actual, nombre_usuario
    nivel_actual = 3
    corriendo = True
    clock = pygame.time.Clock()
    puntos = 160
    vida = 3
    velocidad_comida =  7
    flag = True

    fondo = pygame.image.load("Pou.PYGAME./arch.imagenes/nivel_tres.png")  
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA)) 

    todos_los_sprites = pygame.sprite.Group()
    pou = Pou()
    comida_buena = ComidaBuena(velocidad_comida)
    comida_mala = ComidaMala(velocidad_comida)
    todos_los_sprites.add(pou, comida_buena, comida_mala)

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        todos_los_sprites.update()

        colisiones_buenas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_buenas:
            puntos += 10
            comida_buena_s.play()

        colisiones_malas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_malas:
            vida -= 1
            comida_mala_s.play()
        if vida == 0:
            game_over_s.play()
            mostrar_gameover()
        if puntos == 300:
        #guardar_puntaje()
            ganaste()
            corriendo = False

        todos_los_sprites.draw(pantalla)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        score()

        clock.tick(30)
        pygame.display.update()
    pygame.quit()



def nivel_dos():
    global velocidad_juego, puntos, nivel_actual, nombre_usuario
    nivel_actual = 2
    corriendo = True
    clock = pygame.time.Clock()
    puntos = 90
    vida = 3
    velocidad_comida = 7
    flag = True

    fondo = pygame.image.load("Pou.PYGAME./arch.imagenes/nivel_dos.jpeg")  
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA)) 

    todos_los_sprites = pygame.sprite.Group()
    pou = Pou()
    comida_buena = ComidaBuena(velocidad_comida)
    comida_mala = ComidaMala(velocidad_comida)
    todos_los_sprites.add(pou, comida_buena, comida_mala)

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        # Actualizar todos los sprites
        todos_los_sprites.update()
        colisiones_buenas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_buenas:
            puntos += 10
            comida_buena_s.play()

        colisiones_malas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_malas:
            vida -= 1
            comida_mala_s.play()
        if vida == 0:
            game_over_s.play()
            mostrar_gameover()
        if puntos >= 150:
            pasar_nivel()
            corriendo = False

        todos_los_sprites.draw(pantalla)
        pygame.display.flip()
        score()
        clock.tick(30)
        pygame.display.update()
    pygame.quit()

def nivel_uno():
    global puntos, nivel_actual, nombre_usuario
    nivel_actual = 1
    corriendo = True
    clock = pygame.time.Clock()
    puntos = 0
    vida = 3
    velocidad_comida = 5
    flag = True

    fondo = pygame.image.load("Pou.PYGAME./arch.imagenes/nivel_uno.jpeg")
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    todos_los_sprites = pygame.sprite.Group()
    pou = Pou()
    comida_buena = ComidaBuena(food, velocidad_comida)
    comida_mala = ComidaMala(bad, velocidad_comida)
    todos_los_sprites.add(pou, comida_buena, comida_mala)

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        # Verificar colisiones entre Pou y ComidaBuena
        colisiones_buenas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_buenas:
            puntos += 10
            comida_buena_s.play()

        colisiones_malas = pygame.sprite.spritecollide(pou, todos_los_sprites, False)
        for colision in colisiones_malas:
            vida -= 1
            comida_mala_s.play()

        if vida == 0:
            game_over_s.play()
            mostrar_gameover()
        if puntos >= 80:
            pasar_nivel()
            corriendo = False

        todos_los_sprites.update()

        pantalla.blit(fondo, (0, 0))
        todos_los_sprites.draw(pantalla)

        score()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def menu():
    global puntos
    corriendo = True
    puntos = 0
    boton_inicio = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 25, 100, 50)
    boton_salir = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 + 50, 100, 50)
    boton_puntajes = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 + 125, 100, 50)

    imagen_fondo_menu = pygame.image.load("Pou.PYGAME./arch.imagenes/imagen fondo de menu.jpeg")
    imagen_fondo_menu = pygame.transform.scale(imagen_fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    corriendo = False

        if pygame.mouse.get_pressed()[0]:
            if boton_inicio.collidepoint(pygame.mouse.get_pos()):
                ingresar_usuario()
            elif boton_salir.collidepoint(pygame.mouse.get_pos()):
                corriendo = False
            elif boton_puntajes.collidepoint(pygame.mouse.get_pos()):
                print(obtener_datos())
                mostrar_datos()

        pantalla.blit(imagen_fondo_menu, (0, 0))

        fuente = pygame.font.SysFont("Arial", 50)
        text = fuente.render("FOOD DROP", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (400, 100)
        pantalla.blit(text, textRect)

        pygame.draw.rect(pantalla, (0, 0, 0), boton_inicio)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_salir)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_puntajes)

        fuente = pygame.font.SysFont("Arial", 20)
        texto_inicio = fuente.render("Inicio", True, (255, 255, 255))
        texto_salir = fuente.render("Salir", True, (255, 255, 255))
        texto_puntajes = fuente.render("Puntajes", True, (255, 255, 255))

        pantalla.blit(texto_inicio, (boton_inicio.x + 25, boton_inicio.y + 15))
        pantalla.blit(texto_salir, (boton_salir.x + 30, boton_salir.y + 15))
        pantalla.blit(texto_puntajes, (boton_puntajes.x + 8, boton_puntajes.y + 15))

        pygame.display.flip()

    pygame.quit()

menu()
cerrar_conexion(conexion)
