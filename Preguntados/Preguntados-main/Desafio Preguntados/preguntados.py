import pygame
from constantes import *
from datos import lista

lista_preguntas = [] 
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_correcta = []
pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
posicion = 0
score = 0



for dato in lista:
    lista_preguntas.append(dato['pregunta'])
    lista_opcion_a.append(dato['a'])
    lista_opcion_b.append(dato['b'])
    lista_opcion_c.append(dato['c'])
    lista_correcta.append(dato['correcta'])




pygame.init()
pantalla = pygame.display.set_mode((900, ALTO_VENTANA), 0, 15)
pygame.display.set_caption("Preguntados")

imagen = pygame.image.load("preguntados.png")
imagen = pygame.transform.scale(imagen,(275,200))
imagen_fondo = pygame.image.load("PERSONAJES.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(1450,650))
sonido_correcto = pygame.mixer.Sound("correct.mp3")
sonido_incorrecto = pygame.mixer.Sound("fail.mp3")
fuente = pygame.font.Font('HVD Fonts  MikadoUltra.otf', 30)
#fuente = pygame.font.SysFont("MikadoUltra", 30)
texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
texto_pregunta = fuente.render("PREGUNTA",True, COLOR_GRIS)
texto_reiniciar = fuente.render("REINICIAR",True, COLOR_GRIS)
texto_SCORE = fuente.render("SCORE: ",True, COLOR_GRIS)
texto_opcion_a = fuente.render(str(opcion_a),True, COLOR_NEGRO)
texto_opcion_b = fuente.render(str(opcion_b),True, COLOR_NEGRO)
texto_opcion_c = fuente.render(str(opcion_c),True, COLOR_NEGRO)
texto_score = fuente.render(str(score),True, COLOR_GRIS)
texto_finish = fuente.render(str(pregunta),True, COLOR_GRIS)


bandera = True

while bandera: 


    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            if posicion > len(lista_preguntas):
                texto_finish = fuente.render(f"No hay más preguntas que responder. Tu puntuación es {score}",True, COLOR_NEGRO)
                texto_preguntas = fuente.render(' ' ,True, COLOR_NEGRO)
            #boton de preguntas(300, 10)(499, 108)
            if posicion_click[0] > 300 and posicion_click[0] < 499 and posicion_click[1] > 10 and posicion_click[1] < 108:
                if posicion >= len(lista_preguntas):
                    texto_finish = fuente.render(f"No hay más preguntas que responder. Tu puntuación es {score}",True, COLOR_NEGRO)
                    texto_preguntas = fuente.render(' ' ,True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(' ' ,True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render(''  ,True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render(' ' ,True, COLOR_NEGRO)
                    posicion = 0
                    score = 0
                else:  
                    texto_finish = fuente.render(' ',True,COLOR_NEGRO)   
                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                    
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    oportunidad = 2

                    posicion += 1


            #boton de reiniciar (300, 490)(500, 589)
            if posicion_click[0] > 300 and posicion_click[0] < 500 and posicion_click[1] > 490 and posicion_click[1] < 589:
                posicion = 0
                texto_finish = fuente.render(' ',True,COLOR_NEGRO)
                pregunta = lista_preguntas[posicion]
                opcion_a = lista_opcion_a[posicion]
                opcion_b = lista_opcion_b[posicion]
                opcion_c = lista_opcion_c[posicion]
                texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                score = 0
                texto_score = fuente.render(str(score),True, COLOR_GRIS)
                oportunidad = 2
                posicion +=1

            #boton opcion a 
            if posicion_click[0] > 37 and posicion_click[0] < 186 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'a' :
                    score += 10
                    texto_score = fuente.render(str(score),True, COLOR_GRIS)
                    sonido_correcto.play()
                    oportunidad = 2
                    
                    if posicion >= len(lista_preguntas):
                        texto_finish = fuente.render(f"No hay más preguntas que responder. Tu puntuación es {score}",True, COLOR_NEGRO)
                        texto_preguntas = fuente.render(' ' ,True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render(' ' ,True, COLOR_NEGRO)
                        texto_opcion_b = fuente.render(''  ,True, COLOR_NEGRO)
                        texto_opcion_c = fuente.render(' ' ,True, COLOR_NEGRO)
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
                        posicion += 1

                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_a = fuente.render(' ' ,True, COLOR_NEGRO)
                    sonido_incorrecto.play()

            #boton opcion b
            if posicion_click[0] > 297 and posicion_click[0] < 470 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'b' :
                    score += 10
                    texto_score = fuente.render(str(score),True, COLOR_GRIS)
                    sonido_correcto.play()
                    oportunidad = 2

                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                        
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    posicion += 1
                    
                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_b = fuente.render(''  ,True, COLOR_NEGRO)
                    sonido_incorrecto.play()

            #boton opcion c
            if posicion_click[0] > 568 and posicion_click[0] < 778 and posicion_click[1] > 300 and posicion_click[1] < 326:
                if lista_correcta[posicion - 1] == 'c' :
                    score += 10 
                    texto_score = fuente.render(str(score),True, COLOR_GRIS)
                    sonido_correcto.play()
                    oportunidad = 2

                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                        
                    texto_preguntas = fuente.render(str(pregunta),True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render('A) ' + str(opcion_a),True, COLOR_NEGRO)
                    texto_opcion_b = fuente.render('B) ' + str(opcion_b),True, COLOR_NEGRO)
                    texto_opcion_c = fuente.render('C) ' + str(opcion_c),True, COLOR_NEGRO)
                    posicion += 1
                    
                else: 
                    oportunidad = oportunidad - 1
                    texto_opcion_c = fuente.render(' ' ,True, COLOR_NEGRO)
                    sonido_incorrecto.play()


            if oportunidad <= 0:
                texto_finish = fuente.render(f'Fin del juego, su puntuación fue de {score}', True, COLOR_GRIS)
                texto_preguntas = fuente.render(' ' ,True, COLOR_NEGRO)
                texto_opcion_a = fuente.render(' ' ,True, COLOR_NEGRO)
                texto_opcion_b = fuente.render(''  ,True, COLOR_NEGRO)
                texto_opcion_c = fuente.render(' ' ,True, COLOR_NEGRO)
                posicion = 0
                score = 0
                texto_score = fuente.render(str(score),True, COLOR_GRIS) 
            pygame.display.flip()





    pantalla.fill(COLOR_VERDEAGUA)
    
    pantalla.blit(imagen_fondo,(-500,0))
    pygame.draw.rect(pantalla,COLOR_AMARILLO, (300, 10, 200, 100), 0, 15)#(300, 10)(499, 108)
    
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 490, 200, 100), 0, 15)#(300, 490)(500, 589)

    pantalla.blit(imagen,(0,0))
    pantalla.blit(texto_preguntas,(40,225))
    pantalla.blit(texto_pregunta,(320,40))
    pantalla.blit(texto_opcion_a,(40,300))
    pantalla.blit(texto_opcion_b,(300,300))
    pantalla.blit(texto_opcion_c,(565,300))
    pantalla.blit(texto_reiniciar,(320,520))
    pantalla.blit(texto_SCORE,(650,20))
    pantalla.blit(texto_score,(800,20))
    pantalla.blit(texto_finish,(100,225))


    pygame.display.flip()

pygame.quit()
