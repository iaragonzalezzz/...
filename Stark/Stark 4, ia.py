'''Apellido : Gonzalez
Nombre : Iara '''
from data_stark import *
import re

'''Recibe un string que en este caso es el nombre del personaje, extrae sus iniciales (las del nombre) y las devuelve'''
def extraer_iniciales(nombre_heroe:str):
    if nombre_heroe == " ": #verifica si la cadena es un espacio en blanco 
        respuesta = "n/a"
    else:
        if re.search("the", nombre_heroe) != None: #busca la subcadena "The" en nombre_superheroe 
            cambio_nombre = re.sub("The", " ", nombre_heroe) #la reemplaza la subcadena "The" en nombre_superheroe 
            respuesta = cambio_nombre
        elif re.search("-", nombre_heroe) != None:
            cambio_nombre = re.sub("-", " ", nombre_heroe) 
            respuesta = cambio_nombre
        else:
            cambio_nombre = nombre_heroe
        inicial = re.sub("[a-z]+", "", cambio_nombre) #elimina las letras minusculas
        espacio = re.sub(r"\s+", " ", inicial) #reemplaza los espacios en blanco con un solo espacio
        punto = re.sub(" ","." , espacio) #se reemplazan los espacios en blanco con puntos
        respuesta = (punto + ".")

    return respuesta

'''Se le pasa por parametro un string, lo que hace la funcion es convertirlo a minuscula y con formato snake_case
si el dato no es un str va a retornar false, si es lo devuelve en minuscula y snake_case '''

def obtener_dato_formato(dato: str):
    if type(dato) != str:
        respuesta = False
    else:
        minuscula = dato.lower()
        respuesta = re.sub(" ","_", minuscula) #reemplaza los espacios en blanco con _ en la cadena en minúsculas

    return respuesta

'''Se le pasa por parametro un diccionario de x personaje, este va a verificar si es un diccionario y si tiene la clave nombre, si pasa eso te devuelve el nombre de una forma determinada. Si este no es diccionario o no tiene clave nombre va a retornar
false'''
def imprimir_nombre_con_iniciales(nombre_personaje:dict): 
    if type(nombre_personaje) == dict:
        if "nombre" in nombre_personaje:
            nombre = nombre_personaje["nombre"]
            minuscula = obtener_dato_formato(nombre)
            iniciales = extraer_iniciales(nombre)
            respuesta =("* {0} ({1})".format(minuscula,iniciales)) 
    else:
        respuesta = False
    return respuesta

'''Se le pasa por parametro la lista de personajes, si esta no es una lista o si esta vacia retorna False, si la lista no esta vacia y tiene
personajes devuelve los nombres usando la funcion anterior'''

def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if type(lista_heroes) == list:
        if lista_heroes != None: 
            for heroe in lista_heroes: 
                print(imprimir_nombre_con_iniciales(heroe))
    else:
        return False

'''se le va a pasar por parametro un diccionario de un personaje y una identificacion, dependiendiendo el genero del personaje se le va a asignar un
determinado codigo y va a retornar el género, el código va a ir seguido de ceros y finaliza con la
identificacion que corresponda. Si el diccionario esta vacio o no tiene alguno de los generos especificados va a retornar N/A '''

def generar_codigo_heroe(dic_heroe: dict, id:int): 
    if dic_heroe["genero"] == ' ' or dic_heroe["genero"] != "M" and dic_heroe["genero"] != "F" and dic_heroe["genero"] != "NB": 
        respuesta = "N/A"
    else:
        id= str(id)
        if dic_heroe["genero"] == "M": 
            codigo = 1
            ceros = id.zfill(7) #rellena con 7 ceros
        elif dic_heroe["genero"] == "F": 
            codigo = 2
            ceros = id.zfill(7)
        elif dic_heroe["genero"] == "NB": 
            codigo = 0
            ceros = id.zfill(6) #lo mismo pero con 6
        respuesta = ("{0}-{1}{2}") .format(dic_heroe["genero"],codigo,ceros)
    return respuesta

"""se le va a pasar por parametro una lista de personajes, si la lista esta vacia o un elemento de la lista no es de tipo
diccionario va a retornar false, si no va a recorrer la lista y  va a generar el codigo de cada personaje usando las funciones
que ya se usaron anteriormente, va a devolver un string con el nombre y el codigo del persoanje en un formato especifico"""""

def stark_generar_codigos_heroes(lista_personaje: list): 
    id_heroe = 0
    if lista_personaje == []:
        respuesta = False
    else:
        for personajes in lista_personaje:
            if type(personajes) != dict:
                respuesta = False
            else:
                id_heroe += 1 #contador que va asignar un identificador único a cada héroe
                codigo_heroe = generar_codigo_heroe(personajes, id_heroe)
                nombre_heroe = imprimir_nombre_con_iniciales(personajes)
                print ("{0} | {1}".format(nombre_heroe,codigo_heroe))
                respuesta = "BIEN! Codigos generados"
    return respuesta

'''se le pasa por parámetro un string que representa un posible número.
La función va a analizar el string, le va a sacar el espacio en blanco del principio y el final (si tiene) y 
si es un numero entero positivo lo devuelve casteado a str, si tiene carácteres no numéricos retornar -1,
si es un número negativo retorna -2 y si presenta otro carácter devuelve -3'''
def sanitizar_entero (numero_str: str):
    numero_str = numero_str.strip() 
    if re.search('[A-Za-z]+',numero_str): #busca caracteres no numéricos en numero_str
        respuesta = - 1 #si encuentra va a -1
    elif re.search('[0-9]+',numero_str): #busca carac. numericos
        if re.search('^-',numero_str): #busca num negativo
            respuesta = - 2 #i encuentra queda en -2
        else:
            respuesta = int(numero_str) #Si no encuentra, se convierte la cadena a un entero.
    else: 
        respuesta = -3 #si no se cumple ninguna condicion queda en -3
    return respuesta

'''Va a recibir por parámetro un string que va a representar un posible número decimal.
La función va a analiza el string, le saca los espacios en blanco del principio y el final (si tiene) y 
si es un numero flotante positivo lo devuelve casteado a float, si tiene carácteres no numéricos retornar -1,
si es un número negativo retorna -2 y si presenta otro carácter devuelve -3'''
def sanitizar_flotante(numero_str:str):
    numero_str = numero_str.strip() 
    if re.search('[A-Za-z]+',numero_str):
        respuesta = -1
    elif re.search('\.',numero_str):
        if re.search('^-',numero_str):
            respuesta = - 2
        else: #Si no encuentra, se convierte la cadena a un decimal.
            respuesta = float(numero_str) 
    else: 
        respuesta = -3
    return respuesta

'''se pasa por parámetro un string que representa el texto a validar y un string opcional que va a representar un valor por
defecto. La función va a analizar el string le saca los espacios en blanco del principio y del final (si tiene)
si el string es solo de texto lo va a retornar en minuscula, si tiene numeros retorna “N/A”, si tiene una / la
reemplaza por un espacio en blanco. Si el string esta vacio devuelve el valor por defecto en minuscula'''

def sanitizar_str(valor:str, valor_defecto:str):
    valor = valor.strip() #va a eliminar los espacios en blanco al principio y al final 
    valor_defecto = valor_defecto.strip()
    if re.search('[0-9]+', valor): #busca digitos 
        respuesta = 'N/A'
    elif re.search('\/', valor): #busca /
        respuesta = re.sub("\/"," ", valor) #se reemplaza por un espacio en blanco en la respuesta.
    elif valor == " ": 
        if type(valor_defecto) == str:
                respuesta= valor_defecto.lower()
    else:
        respuesta = valor.lower()
    return respuesta

'''Se pasa por parámetros un diccionario de personaje, un string que va a ser el dato a sanitizar y el 
tipo del dato. La función va a verificar que el tipo de dato se encuentre en lo establecido y que tambien encuentre o exista la clave en el 
diccionario, si no devuelve un mensaje de error y va a retornar False. Si los datos estan correctos lo sanitiza y va a
retornar True '''
def sanitizar_dato(personaje: dict, clave:str, tipo_de_dato):
    tipo_de_dato = tipo_de_dato.lower()
    dato_sanitizado = False
    if clave in personaje:
        if tipo_de_dato == "string":
            personaje[clave] = sanitizar_str(personaje[clave]," ") 
            dato_sanitizado = True
        elif tipo_de_dato == "entero":
            personaje[clave] = sanitizar_entero(personaje[clave])
            dato_sanitizado = True
        elif tipo_de_dato == "flotante":
            personaje[clave] = sanitizar_flotante(personaje[clave],)
            dato_sanitizado = True
        else:
            print("ERROR! Tipo de dato no reconocido")
    else:
        print("La clave especificada es inexistente")
    return dato_sanitizado

'''se pasa por parametro una lista de personajes. La función va a recorrer la lista y sanitiza los valores que se piden,
si todos los datos se normalizaron va a retornar un "Datos normalizados", si no se normalizaron todos devuelve
"ERROR! No se pudieron normalizar todos los datos" y si la lista esta vacía devuelve 'Error: Lista de héroes vacía'''
def stark_normalizar_datos(lista_personajes:list):
    if lista_personajes == []:
        print("Error: Lista de héroes vacía")
    else:
        for heroe in lista_personajes:
            altura = sanitizar_dato(heroe,"altura" , "flotante")
            peso = sanitizar_dato(heroe,"peso","flotante")
            color_ojos = sanitizar_dato(heroe,"color_ojos" , "string")
            color_pelo = sanitizar_dato(heroe,"color_pelo" , "string")
            fuerza = sanitizar_dato(heroe,"fuerza" , "entero")
            inteligencia = sanitizar_dato(heroe,"inteligencia" , "entero")
        if altura == True and peso == True and color_ojos == True and color_pelo == True and fuerza == True and inteligencia == True:
            print("Exito! Datos normalizados")
        else:
            print("ERROR! No se pudieron normalizar todos los datos")

'''se pasa por parámetro una lista de personajes, la funcion va a ignorar la palabra "the" (si la tiene) y
devuelve cada palabra de los nombres de los personajes con un "-" '''
def stark_imprimir_indice_nombre(lista_personajes):
    lista_nombres = []
    for personaje in lista_personajes:
        nombre = personaje["nombre"]
        nombre = re.sub("the","",nombre)
        nombre = re.sub(r"\s+","-",nombre)
        lista_nombres.append(nombre)
    unificador = "-"
    respuesta = unificador.join(lista_nombres)
    return respuesta

'''se pasa por parámetro un patron quien va a generar el separador, un numero que va a representar la
cantidad de veces que se repite ese patron y un booleano que va a indicar si se puede imprimir la respuesta.
La funcion va a repetir este patron tantas veces como el largo dado y va a devolver la cadena de texto, en caso de que no se
cumplan las indicaciones va a devolver' N/A' '''

def generar_separador(patron:str, largo:int , imprimir = True):
    if len(patron) >= 1 and  len(patron) <= 2:
        if type(largo)== int and largo >=  1 or largo <= 235:
            respuesta = patron * largo
    else:
        respuesta = 'N/A'
    if imprimir:
        print(respuesta)
    return respuesta

'''se pasa por parámetro un titulo, la funcion va a generar un separador y va a devolver el titulo en mayuscula entre
los separadores'''

def generar_encabezado(titulo:str):
    palabra_de_encabezado = titulo.upper()
    separador_de_encabezado = generar_separador('*',151,False)
    encabezado = "{0}{1}\n{2}".format(separador_de_encabezado, palabra_de_encabezado , separador_de_encabezado)
    return encabezado

'''se pasa por parámetro un diccionario de un personaje, la funcion va a recorrer los datos y los va a devolver como formato con un encabezado'''

def  imprimir_ficha_heroe(personaje:dict):
    encabezado_principal = generar_encabezado("principal")
    nombre = obtener_dato_formato(personaje["nombre"])
    iniciales = extraer_iniciales(personaje["nombre"])
    identidad = obtener_dato_formato(personaje["identidad"])
    consultora = obtener_dato_formato(personaje["empresa"]) 
    codigo = generar_codigo_heroe(personaje,2)
    encabezado_fisico = generar_encabezado("fisico")
    altura = (personaje["altura"] )
    peso = (personaje["peso"] )
    fuerza = (personaje["fuerza"] )
    encabezado_señas = generar_encabezado("señas particulares")
    ojos = (personaje["color_ojos"]) 
    pelo = (personaje["color_pelo"]) 
    respuesta = ('''{0}NOMBRE DEL HEROE: {1} ({2})\nIDENTIDAD SECRETA: {3}\nCONSULTORA: {4}\nCÓDIGO DE HÉROE: {5}
{6}ALTURA: {7}\nFUERZA: {8} \nPESO: {9}\n{10}\nCOLOR DE PELO: {11}\nCOLOR DE OJOS: {12} '''.format(encabezado_principal,nombre,iniciales,identidad,consultora,codigo,encabezado_fisico,altura,peso,fuerza,encabezado_señas,ojos,pelo))
    return respuesta


'''se pasa por parámetro la lista de personajes. La funcion va a imprimir la primer ficha y te va a pedir que ingreses una opcion,
si es 1 te va a mostrar la ficha de la izquierda, si es 2 te va a mostrar la de la derecha, si es 3 sale del programa y si no ingresas 
ninguna de esas opciones, vuelve a pedirte un ingreso valido. Va a devolver la ficha del personaje segun corresponda
'''
def stark_navegar_fichas(lista_personajes:list):
    indice = 0
    flag_navegar = True
    print(imprimir_ficha_heroe(lista_personajes[indice ]))
    while flag_navegar:
        opcion = input("Ingrese alguna de las siguientes opciones ([ 1 ] Ir a la izquierda, [ 2 ] Ir a la derecha, [ 3 ] Salir): ")
        if opcion == "1":
            if indice == 0:
                indice = len(lista_personajes) - 1
            else:
                indice -= 1
                if indice not in range (len(lista_personajes)):
                    indice = len(lista_personajes) 
        elif opcion == "2":
            indice += 1
            if indice not in range (len(lista_personajes)):
                indice = len(lista_personajes) - len(lista_personajes)
        elif opcion == "3":
            break
        else:
            opcion = input("Ingrese una opcion valida: ")
        print(imprimir_ficha_heroe(lista_personajes[indice ]))

#menu
flag_menu = True
while flag_menu:
    print('''1- Imprimir la lista de nombres junto con sus iniciales
2 - Imprimir la lista de nombres y el código
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6- Salir''')
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        print(stark_imprimir_nombres_con_iniciales(lista_personajes))
    elif opcion == '2':
        print(stark_generar_codigos_heroes(lista_personajes))
    elif opcion == '3':
        print(stark_normalizar_datos(lista_personajes))
    elif opcion == '4':
        print(stark_imprimir_indice_nombre(lista_personajes))
    elif opcion == '5':
        stark_navegar_fichas(lista_personajes)
    elif opcion == '6':
        break
    else:
        print("Opcion no valida")