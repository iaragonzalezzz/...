import pygame
from datos import lista
from constantes import *


lista_preguntas = [] 
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_correcta = []
pregunta = " "
opcion_a = " "
opcion_b = " "
opcion_c = " "
posicion = 0
score = 0


for pregunta in lista:
    lista_preguntas.append(pregunta["pregunta"])
    lista_opcion_a.append(pregunta["a"])
    lista_opcion_b.append(pregunta["b"])
    lista_opcion_c.append(pregunta["c"])
    lista_correcta.append(pregunta["correcta"])


pygame.init()
pantalla = pygame.display.set_mode((900, ALTO_VENTANA), 0, 15)
pygame.display.set_caption("Preguntados")
icono = pygame.image.load("iconopregun.webp")
pygame.display.set_icon(icono)

imagen = pygame.image.load("preguntados.logo.png")
imagen = pygame.transform.scale(imagen, (120 , 120))
imagen_fondo = pygame.image.load("/Users/iargonzalez/Desktop/Trabajos facu/Preguntados/Preguntados.jpeg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(1500,700))

fuente = pygame.font.SysFont("Arial Narrow", 25)

texto_preguntas = fuente.render(str("Clickee en PREGUNTA para iniciar el juego"),True, COLOR_NEGRO)
texto_pregunta = fuente.render("PREGUNTA", True, COLOR_NEGRO)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_NEGRO)
texto_SCORE = fuente.render("SCORE: ", True, COLOR_NEGRO)
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_NEGRO)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_NEGRO)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_NEGRO)
texto_score = fuente.render(str(score),True, COLOR_NEGRO)



correr_juego = True
while correr_juego: 

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            correr_juego = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            if posicion > len(lista_preguntas):
                texto_preguntas = fuente.render(" ", True, COLOR_NEGRO)
            
            #boton de preguntas
            if posicion_click[0] > 10 and posicion_click[0] < 210 and posicion_click[1] > 20 and posicion_click[1] < 90:
                if posicion >= len(lista_preguntas):
                    texto_preguntas = fuente.render(" ", True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(" ", True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render(" ", True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render(" ", True, COLOR_NEGRO)
                    posicion = 0
                    score = 0

                else:  
                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                    
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    oportunidad = 2

                    posicion = posicion + 1

            #boton de reiniciar 
            if posicion_click[0] > 300 and posicion_click[0] < 500 and posicion_click[1] > 460 and posicion_click[1] < 525:
                posicion = 0
                pregunta = lista_preguntas[posicion]
                opcion_a = lista_opcion_a[posicion]
                opcion_b = lista_opcion_b[posicion]
                opcion_c = lista_opcion_c[posicion]
                texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                score = 0
                texto_score = fuente.render(str(score), True, COLOR_NEGRO)
                oportunidad = 2
                posicion = posicion + 1

            #boton opcion a 
            if posicion_click[0] > 35 and posicion_click[0] < 185 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == "a" :
                    score = score + 10
                    texto_score = fuente.render(str(score), True, COLOR_NEGRO)
                    oportunidad = 2
                    
                    if posicion >= len(lista_preguntas):
                        texto_preguntas = fuente.render(" ", True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render(" ", True, COLOR_NEGRO)
                        texto_opcion_b = fuente.render(" ", True, COLOR_NEGRO)
                        texto_opcion_c = fuente.render(" ", True, COLOR_NEGRO)
                        posicion = 0
                        score = 0
                    else:   
                        pregunta = lista_preguntas[posicion]
                        opcion_a = lista_opcion_a[posicion]
                        opcion_b = lista_opcion_b[posicion]
                        opcion_c = lista_opcion_c[posicion]

                        texto_preguntas = fuente.render(str(pregunta), True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render('A) ' + str(opcion_a), True, COLOR_NEGRO)
                        texto_opcion_b = fuente.render('B) ' + str(opcion_b), True, COLOR_NEGRO)
                        texto_opcion_c = fuente.render('C) ' + str(opcion_c), True, COLOR_NEGRO)
                        posicion = posicion + 1
                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_a = fuente.render(" ", True, COLOR_NEGRO)

            #boton opcion b
            if posicion_click[0] > 297 and posicion_click[0] < 470 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == "b" :
                    score = score + 10
                    texto_score = fuente.render(str(score),True, COLOR_NEGRO)
                    oportunidad = 2

                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                        
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    posicion = posicion + 1
                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_b = fuente.render(" ", True, COLOR_NEGRO)

            #boton opcion c
            if posicion_click[0] > 568 and posicion_click[0] < 778 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == "c" :
                    score = score + 10 
                    texto_score = fuente.render(str(score), True, COLOR_NEGRO)
                    oportunidad = 2

                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                        
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    posicion = posicion + 1
                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_c = fuente.render(" ", True, COLOR_NEGRO)

            if oportunidad <= 0:
                texto_preguntas = fuente.render(" ", True, COLOR_NEGRO)
                texto_opcion_a = fuente.render(" ", True, COLOR_NEGRO)
                texto_opcion_b = fuente.render(" ", True, COLOR_NEGRO)
                texto_opcion_c = fuente.render(" ", True, COLOR_NEGRO)
                posicion = 0
                score = 0
                texto_score = fuente.render(str(score),True, COLOR_NEGRO) 
            pygame.display.flip()


    pantalla.fill(CIAN)
        
    pantalla.blit(imagen_fondo,(-500,0))

    pygame.draw.rect(pantalla, COLOR_BLANCO , (10 , 20 , 200 , 70 ))
    pygame.draw.rect(pantalla, COLOR_BLANCO , (300 , 455 , 200 , 70 ))

    pantalla.blit(imagen,(350,10))
    pantalla.blit(texto_preguntas,(40,225))
    pantalla.blit(texto_pregunta,(40,40))
    pantalla.blit(texto_opcion_a,(40,300))
    pantalla.blit(texto_opcion_b,(300,300))
    pantalla.blit(texto_opcion_c,(565,300))
    pantalla.blit(texto_reiniciar,(335,470))
    pantalla.blit(texto_SCORE,(650,20))
    pantalla.blit(texto_score,(800,20))

    pygame.display.flip()

pygame.quit()
