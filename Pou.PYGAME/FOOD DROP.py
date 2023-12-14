import pygame
from constantes import *
from clases import *
import sqlite3


pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("FOOD DROP")

def imagen_fondo():
    imagen_fondo = pygame.image.load("arch.imagenes/imagen fondo de menu.jpeg")
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
        print('se creo el ranking')

    except sqlite3.OperationalError:
        print('existe el ranking')

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
        fuente = pygame.font.SysFont("Comic Sans", 50)   
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
            fuente = pygame.font.SysFont("Comic Sans", 25)
            texto_puntaje = fuente.render(f"{i + 1}. Nombre: {puntaje['nombre']}, Puntos: {puntaje['puntos']}", True, (0, 0, 0))

            pantalla.blit(texto_puntaje, (ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 - 100 + i * 100))

        pygame.display.update()

    pygame.quit()


def score():
    global puntos 
    fuente = pygame.font.SysFont("Comic Sans", 50)   
    texto = fuente.render("puntos: " + str(puntos), True, (0, 0, 0))
    textoRect = texto.get_rect()
    textoRect.center = (1000, 40)
    pantalla.blit(texto, textoRect)

def ganaste():
    corriendo = True
    guardar_datos(nombre_usuario, puntos)

    while corriendo:

        pantalla.fill((COLOR_MAGENTA))
        fuente = pygame.font.SysFont("Comic Sans", 30)
        texto_ganaste = fuente.render('¡Ganaste! Para volver al menú, presiona ESC', True, (0, 0, 0))
        score = fuente.render("Score: " + str(puntos), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        pantalla.blit(score, scoreRect)
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 5)
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
        imagen_fondo = pygame.image.load("arch.imagenes/fondo_usuario.webp")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        pantalla.blit(imagen_fondo, (0, 0))
        fuente = pygame.font.SysFont("Comic Sans", 25)
        texto_ingreso = fuente.render("Ingresar nombre del jugador:", True, (0, 0, 0))
        pantalla.blit(texto_ingreso, (ANCHO_VENTANA // 2 - 240, ALTO_VENTANA // 4))
        input_rect = pygame.Rect(ANCHO_VENTANA // 2 - 100, ALTO_VENTANA // 3 + 1, 300, 50)
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
                        niveles(1, 7)
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
        pantalla.fill((COLOR_CELESTE))
        fuente = pygame.font.SysFont("Comic Sans", 20)
        texto_ganaste = fuente.render('¡Nivel superado! Para pasar al siguiente nivel, presione Enter. Para volver al menu, ESC', True, (0, 0, 0))
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        ganasteRect = texto_ganaste.get_rect()
        ganasteRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 5)
        pantalla.blit(texto_ganaste, ganasteRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nivel_actual == 1:
                        niveles(2, 9)
                    elif nivel_actual == 2:
                        niveles(3, 11)
                elif event.key == pygame.K_ESCAPE:
                    menu()

        pygame.display.update()
    pygame.quit()

def mostrar_gameover():
    corriendo_go = True
    guardar_datos(nombre_usuario, puntos)

    while corriendo_go:

        pantalla.fill((COLOR_GRIS))
        fuente = pygame.font.SysFont("Comic Sans", 30)
        text = fuente.render("¡Game Over! Para volver al menú, presionar ESC", True, (0, 0, 0))
        score = fuente.render("Score: " + str(puntos), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
        pantalla.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 20)
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
    menu()

pygame.mixer.music.load("sonidos/sonido_principal.mp3")  
pygame.mixer.music.set_volume(0.2)

def niveles(nivel, velocidad_comida):
    global puntos, nivel_actual, nombre_usuario
    nivel_actual = nivel
    corriendo = True
    clock = pygame.time.Clock()
    vida = 3
    velocidad_comida = velocidad_comida
    pygame.mixer.music.play(-1)

    if nivel == 1:
        puntos = 0
    elif nivel == 2:
        puntos = 60
    elif nivel == 3:
        puntos = 120

    fondo = pygame.image.load(f"arch.imagenes/nivel_{nivel}.jpeg")
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    todos_los_sprites = pygame.sprite.Group()
    # instancia de pou
    pou = Pou()
    # instancia de comidas
    comida_buena = ComidaBuena(food, velocidad_comida)
    comida_mala = ComidaMala(bad, velocidad_comida)
    
    todos_los_sprites.add(pou, comida_buena, comida_mala)
    comidas_buenas = pygame.sprite.Group()
    comidas_buenas.add(comida_buena)
    comidas_malas = pygame.sprite.Group()
    comidas_malas.add(comida_mala)
    tiempo_delay_imagen = 500
    cambiar_imagen = False

    tiempo_inicio = pygame.time.get_ticks()

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        keys = pygame.key.get_pressed()
        # Método
        pou.actualizar(keys)
        todos_los_sprites.update()
        if cambiar_imagen:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - hora_cambio_imagen >= tiempo_delay_imagen:
                pou.actualizar(keys)
                pou.cambiar_imagen(1)
                cambiar_imagen = False

        colisiones_buenas = pygame.sprite.spritecollide(pou, comidas_buenas, False)
        for colision in colisiones_buenas:
            cambiar_imagen = True
            hora_cambio_imagen = pygame.time.get_ticks()
            pou.actualizar(keys)
            pou.cambiar_imagen(2)
            puntos += 10
            colision.reset()
            comida_buena_s.play()

        colisiones_malas = pygame.sprite.spritecollide(pou, comidas_malas, False)
        for colision in colisiones_malas:
            cambiar_imagen = True
            hora_cambio_imagen = pygame.time.get_ticks()
            vida -= 1
            pou.cambiar_imagen(3)
            pou.actualizar(keys)
            colision.reset()
            comida_mala_s.play()

        if vida == 0:
            pygame.mixer.music.stop()
            game_over_s.play()
            mostrar_gameover()

        if puntos == 60 and nivel_actual == 1:
            pasar_nivel()
            corriendo = False
        elif puntos == 120 and nivel_actual == 2:
            pasar_nivel()
            corriendo = False
        elif puntos == 220 and nivel_actual == 3:
            ganaste()

        pantalla.blit(fondo, (0, 0))
        todos_los_sprites.draw(pantalla)

        # Mostrar vidas
        fuente_vidas = pygame.font.SysFont("Comic Sans", 20)
        texto_vidas = fuente_vidas.render("Vidas: " + str(vida), True, (COLOR_VERDE))
        pantalla.blit(texto_vidas, (100, 40))

        # Mostrar tiempo transcurrido
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - tiempo_inicio) // 1000
        fuente_tiempo = pygame.font.SysFont("Comic Sans", 20)
        texto_tiempo = fuente_tiempo.render("Tiempo: " + str(tiempo_transcurrido) + "s", True, (COLOR_VERDE))
        pantalla.blit(texto_tiempo, (300, 40))

        # Mostrar score
        fuente_score = pygame.font.SysFont("Comic Sans", 20)
        texto_score = fuente_score.render("Score: " + str(puntos), True, (COLOR_VERDE))
        pantalla.blit(texto_score, (600, 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def menu():
    global puntos
    corriendo = True
    boton_inicio = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 25, 100, 50)
    boton_salir = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 + 50, 100, 50)
    boton_puntajes = pygame.Rect(ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 + 125, 100, 50)

    imagen_fondo_menu = pygame.image.load("arch.imagenes/imagen fondo de menu.jpeg")
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

        fuente = pygame.font.SysFont("Comic Sans", 50)
        text = fuente.render("FOOD DROP", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (400, 100)
        pantalla.blit(text, textRect)

        pygame.draw.rect(pantalla, (0, 0, 0), boton_inicio)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_salir)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_puntajes)

        fuente = pygame.font.SysFont("Comic Sans", 20)
        texto_inicio = fuente.render("Inicio", True, (COLOR_BLANCO))
        texto_salir = fuente.render("Salir", True, (COLOR_BLANCO))
        texto_puntajes = fuente.render("Ranking", True, (COLOR_BLANCO))

        pantalla.blit(texto_inicio, (boton_inicio.x + 25, boton_inicio.y + 15))
        pantalla.blit(texto_salir, (boton_salir.x + 30, boton_salir.y + 15))
        pantalla.blit(texto_puntajes, (boton_puntajes.x + 8, boton_puntajes.y + 15))

        pygame.display.flip()

    pygame.quit()

menu()
