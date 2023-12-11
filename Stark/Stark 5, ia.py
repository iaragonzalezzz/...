''' Nombre: Iara
Apellido: Gonzalez '''
from data_stark import lista_personajes
import os
import json

'''va a reibir por parámetro un string que va a representar el nombre del archivo que va a leer. La funcion va abrir el archivo en modo 
lectura y va a devolver la informacion que contiene el mismo'''
def leer_archivo(nombre_archivo:str):
    try:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo: #abrir el archivo en modo lectura y utiliza la codificación UTF-8. 
            retornar = archivo.read()
    except FileNotFoundError:
        retornar = False
        print("ERROE! El archivo no existe")
    return retornar

'''va a recibir por parámetro un string que va a representar el nombre con el que se va a guardar el archivo y un string con el 
contenido del archivo. Lo que hace la función es crear el archivo en caso de que no exista y lo va a reescribir si existe. Si el archivo
se creo, va a devolver True, si no se creo va a devolver False. Se va a mostrar por consola un mensaje indicando
la situacion.'''

def guardar_archivo(nombre_a_guardar: str, contenido_a_guardar: str):
        try:
            with open(nombre_a_guardar,"w+",encoding="utf-8") as archivo: #abre el archivo en modo "escritura"
                archivo.write(contenido_a_guardar)
            retornar = True
            print("Se creó el archivo:{0}".format(nombre_a_guardar))
        except FileNotFoundError:
            retornar = False
            print("Error al crear el archivo:{0}".format(nombre_a_guardar))
        return retornar

'''Se reutiliza la funcion de starks anteriores para sanitizar los datos'''

def stark_normalizar_datos(lista_personajes:list): 
    resultado = False
    if lista_personajes == []:
        print("ERROR!. Lista vacía")
        return False
    else:
        for personaje in lista_personajes:
            if type(personaje["altura"]) == float or type(personaje["peso"]) == float or type(personaje["fuerza"]) == int:
                resultado = False
            else:
                personaje["altura"] = float(personaje["altura"])
                personaje["peso"] = float(personaje["peso"])
                personaje["fuerza"] = int(personaje["fuerza"])
                resultado = True
        if resultado == True:
            print("Datos normalizados")
    return resultado

'''se pasa por parametro la ruta del archivo y la lista de personajes. La función va a guardar la info y va a crear un archivo en 
formato csv. Si la lista está vacia va a devolver False y si se creo el archivo va a devolver True.'''
def generar_csv(ruta_de_archivo: str, lista_personajes: list):
    if lista_personajes != []:
        lista_de_claves = list(map(str, lista_personajes[0].keys())) #convierte la lista de claves en cadena
        cabecera = ",".join(lista_de_claves) #creamos cadena de texto separada por comas
        with open(ruta_de_archivo, "w", encoding="utf-8") as archivo:    #modo "w" para escribir la cabecera modo a para agregar datos
            archivo.write("{0}\n".format(cabecera))
        with open(ruta_de_archivo, "a", encoding="utf-8") as archivo:
            for heroe in lista_personajes:
                lista_datos = list(map(str, heroe.values())) #obtiene lista de valores de los heroes
                datos = ",".join(lista_datos)
                archivo.write("{0}\n".format(datos))
        retornar = True
    else:
        retornar = False
    return retornar

'''se pasa por parametro la ruta del cvs a leer. La función va a generar una lista de heroes con los datos del archivo que se le 
pasaron. Va a devolver la lista de hereoes, y en caso de que el archivo no exista va a retornar False.'''

def leer_cvs(ruta_de_archivo:str):
    lista_heroes = []
    if os.path.exists(ruta_de_archivo):   # verifica si el archivo existe
        with open(ruta_de_archivo,'r') as archivo:
            claves = archivo.readline().strip().split(',') #lee la línea para obtener las claves/columnas
            for linea in archivo:
                heroe = {}
                valores = linea.strip().split(',') # divide la línea en valores y usa la coma como separador
                # va a iterar sobre las claves y valores para agregarlos al diccionario del héroe
                for i in range (len(claves)): 
                    heroe[claves[i]] = valores[i]
                lista_heroes.append(heroe)
        retornar = lista_heroes
    else: 
        retornar = False
    return retornar

'''se pasa por parametro la Ruta del archivo, la lista de los héroes y el nombre de la lista.
si la lista no se enecuntra vacia va a retonar la clave la lista de superhéroes, el supuesto nombre de clave tendria que ser la del
tercer parámetro, que esta es el nombre de la lista.'''

def generar_json(ruta_archivo:str,lista_personajes: list, nombre_lista:str):
    if lista_personajes != []:
        stark_normalizar_datos(lista_personajes)
        diccionario = {}
        diccionario[nombre_lista] =[]  # incializamos un diccionario con una clave dada por el parámetro el mismo parametro de nombre
        for i in range(len(lista_personajes)):
            diccionario[nombre_lista].append(lista_personajes[i]) # agrega cada elemento a la lista con la clave que le pasamos en el diccionario diccionario
        with open(ruta_archivo, "w", encoding = "utf-8") as archivo:
                    json.dump(diccionario, archivo,  indent = 4) #toma el diccionario y escribe su representación JSON en el archivo, 
                    #usando una sangría de 4 espacios para formatear el JSON

'''recibe la ruta del archivo y el nombre de la lista a leer.
Si el archivo existe, va a leer el json y va a retornar la lista, en cambio, si no existe va a retornar false.'''

def leer_json(ruta_de_archivo:str, nombre_lista:str):
    retornar = False 
    try:
        with open(ruta_de_archivo, "r", encoding = "utf-8") as archivo:
            diccionario = json.load(archivo) #cargar el contenido del archivo en el diccionario
            if nombre_lista in diccionario: #verifica si la clave nombre_lista está en el diccionario cargado del archivo JSON
                lista = diccionario[nombre_lista] #si la clave esta presente, la va asignar a la lista
                retornar = lista
    except FileNotFoundError:
        retornar = False #si no encuentra el archivo retorna falso 
    return retornar

'''se pasa la lista de personajes y la clave que va a hacer que se ordenen. Va a ordenar la lista de héroes con 
la clave pasada por paramentro de manera ascendente. Va a devolver la lista ordenada'''
def ordenar_clave_asc(lista_personajes:list, clave:str):
    stark_normalizar_datos(lista_personajes)
    if clave != "altura" and clave != "fuerza" and clave != "peso":
        retornar = False
    else: 
        for i in range(len(lista_personajes) - 1):
            for j in range(i + 1, len(lista_personajes)):
                if lista_personajes[i][clave] > lista_personajes[j][clave]: #compara los valores
                    aux = lista_personajes[i] #almacena el valor de la posicion
                    lista_personajes[i] = lista_personajes[j]
                    lista_personajes[j] = aux
        retornar = lista_personajes
    return retornar

'''recibe la lista de personajes y la clave con la que se los va a ordenar. Va a ordenar la lista de héroes con 
la clave que pasamos por paramentro de manera descendente. Va a devolver la lista ordenada '''
def ordenar_clave_des(lista_personajes:list, clave:str):
    stark_normalizar_datos(lista_personajes)
    if clave != "altura" and clave != "fuerza" and clave != "peso":
        retornar = False
    else: 
        for i in range(len(lista_personajes) - 1):
            for j in range(i + 1, len(lista_personajes)):
                if lista_personajes[i][clave] < lista_personajes[j][clave]:
                    aux = lista_personajes[i]
                    lista_personajes[i] = lista_personajes[j]
                    lista_personajes[j] = aux
        retornar = lista_personajes
    return retornar

'''recibe la lista de personajes y la clave con la que se los va a ordenar. Va a ordenar la lista de héroes con 
la clave que pasamos por paramentro de manera descendente. Va a devolver la lista ordenada '''
'''Recibe la lista de personajes y la clave por la que se los va a ordenar. La funcion va a preguntar si se quiere ordenar
de forma ascendente o descendente'''
def ordenar_clave_segun_parameto(lista_personajes: list, clave: str):
        opcion = input("\n¿Como quiere ordenar la lista de manera ascendente ('asc') o descendente ('desc'): ")
        if opcion == "asc":
            print(ordenar_clave_asc(lista_personajes, clave))
        elif opcion == "desc":
            print(ordenar_clave_des(lista_personajes, clave))
        else:
            print("Ingrese una opcion que sea valida")

#menu
flag_menu = True
flag_json = True
flag_opcion_normalizar = True
while flag_menu:

    print(''' 1- Normalizar datos
2-Generar CSV (Tiene que guardar la lista generada en otra variable)
3- Listar heroes del archivo CSV ordenados por altura ASC (Tiene que validar si el
mismo existe)
4-Generar JSON (Guardar la lista generada en otra variable)
5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si existe)
6-Ordenar Lista por fuerza (Tiene que preguntar al usuario si lo quiere
ordenar de manera DESC o ASC
7-Salir''')
    
    opcion = input("Ingrese una opcion: ")
    while flag_opcion_normalizar == True:
            if opcion != "1":
                print("ERROR. Falta normalizar los datos")
                opcion = print('''1-Normalizar datos 
2-Generar CSV 
3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)
4-Generar JSON (Guardar la lista generada en otra variable)
5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)
6-Ordenar Lista por fuerza
7-Salir''')

                opcion = input("Ingrese una opcion: ")
            else:
                flag_opcion_normalizar = False

    if opcion == "1":
        print(stark_normalizar_datos(lista_personajes))
    elif opcion == "2":
        csv_generado = generar_csv("Opcion_2.CSV", lista_personajes)
        print("Archivo CSV generado")
    elif opcion == "3":
        ruta_csv = 'Opcion_2.CSV'
        if os.path.exists(ruta_csv):
            lista_csv = leer_cvs(ruta_csv)
            print(ordenar_clave_asc(lista_csv, 'altura'))
        else:
            print("El archivo CSV es inexistente.")
    elif opcion == "4":
        json_generado = generar_json('Opcion_4.JSON',lista_personajes , "lista_personajes")
        print("ERROR! Archivo JSON generado")
    elif opcion == "5":
        ruta_json = "Opcion_4.JSON"
        if os.path.exists(ruta_json):
            lista_json = leer_json('Opcion_4.JSON', "lista_personajes")
            print( ordenar_clave_des(lista_json, 'peso'))
        else:
            print("El archivo JSON es inexistente.")
    elif opcion == "6":
        print(ordenar_clave_segun_parameto(lista_personajes,'fuerza'))
    elif opcion == "7":
        break
    else:
        print("ERROE! Opcion no valida")