from data_stark import lista_personajes
from funciones import *

#Nombre: Iara
#Apellido: Gonzalez

while True:
    respuesta = input("Ingrese una opción desde la A a la J. Presione 1 para salir: ")
    if respuesta == "A":
        lista = encontrar_superheroes_NB ("genero" , "NB")
        print(lista)
    elif (respuesta == "B"):
        nombre = encontrar_maximos("genero" , "F")
        print(nombre)
    elif (respuesta == "C"):
        nombre = encontrar_maximos("genero" , "M")
        print(nombre)
    elif (respuesta == "D"):
        nombre = encontrar_minimos("genero" , "M")
        print(nombre)
    elif (respuesta == "E"):
        nombre = encontrar_minimos("genero" , "NB")
        print(nombre)
    elif (respuesta == "F"):
        promedio = encontrar_promedio("genero" , "NB")
        print(promedio)
    elif (respuesta == "G"):
        diccionario = determinar_tipos("color_ojos" , "cantidad")
        print(diccionario)
    elif (respuesta == "H"):
        diccionario = determinar_tipos("color_pelo" , "cantidad")
        print(diccionario)
    elif (respuesta == "I"):
        diccionario = determinar_tipos("color_ojos" , "agrupar")
        print(diccionario)
    elif (respuesta == "J"):
        diccionario = determinar_tipos("inteligencia" , "agrupar")
        print(diccionario)
    elif (respuesta == "1"):
        break