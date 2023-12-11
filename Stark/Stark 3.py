from data_stark import lista_personajes
# Gonzalez
# Iara

#Función Normalizar Datos:
"""Esta funcion nos permite normalizar los datos 'Fuerza', 'Peso' y 'Altura' ya que estos aparecen como tipo String, lo que hacemos es pasarlo a Int y Float, 
donde le paso una lista por parámetro y retorna valor True si los datos se normalizaron correctamente. 
En caso de que retorne False es porque la lista esta vacia, faltan datos, o porque ya se normalizo antes. """
def normalizar_datos_stark (lista_personajes: list):
    resultado = {"value": False}
    for superheroe in lista_personajes:
        if (superheroe == {}):
            print("ERROR. Verificar que no falte ningún dato en la lista")
            return False
    if (lista_personajes == []):
        print("ERROR. Verificar que la lista no esté vacía")
        return False
    else:
        for superheroe in lista_personajes:
            if (type(superheroe["fuerza"] == int) or (type(superheroe["peso"]) == float) or type(superheroe["altura"] == float)):
                print("ERROR. Verificar que los datos ya no se hayan normalizado anteriormente")
                return False
            else:
                superheroe["fuerza"] = int(superheroe["fuerza"])
                superheroe["peso"] = float(superheroe["peso"])
                superheroe["altura"] = float(superheroe["altura"])
                resultado["value"] = True
        if (resultado["value"] == True):
            print("CORRECTO. Los datos se normalizaron")
        return True

#Función Obtener Dato:
"""Esta funcion permite obtener el valor de una clave dentro de un diccionario, este le pasa al diccionario la misma clave por parámetro, retornando asi el valor True. 
Si nos devuelve False es porque el diccionario esta vacío o la clave nombre no exista. """

def obtener_dato(heroe:dict,clave:str):
    if (heroe == {}):
        return False
    dato = heroe[clave]
    return dato
    
#Función Obtener Nombre:
"""Esta funcion nos permite obtener el valor de la clave nombre dentro de un diccionario, donde tambien se pasa por parámetro, retornando el valor correcto. En caso de que retorne False
es porque el diccionario esta vacio o la clave no exista. """

def obtener_nombre(heroe:dict):
    if heroe == {}:
        return False
    nombre = heroe["nombre"]
    return "Nombre: {0}".format(nombre)

#Función Obtener Nombre Y Dato:
"""Esta funcion nos permite obtener el valor de la clave nombre. Este pasa la clave como el diccionario por parámetro, retornando el valor correcto o un False si el diccionario se encuentra vacío o las claves no existan. """
def obtener_nombre_y_dato(heroe:dict, clave:str):
    if heroe == {}:
        return False
    nombre = heroe["nombre"]
    dato = heroe[clave]

    return"Nombre: {0} | {1}: {2} ".format(nombre,clave,dato)

#Función Obtener Máximo:
"""Esta funcion nos permite obtener el valor del máximo de una clave. Este verifica que el valor sea un numero entero o un decimal, y
pasa la lista y la clave por parametro. En caso de que retorne False es porque la lista esta vacía o el valor que encontro no es ni int ni float.
En caso de que sea correcto, va a retornar el máximo junto con el nombre del superheroe. """
def obtener_maximo (value: str, lista_personajes: list):
    maximo = None
    nombre = " "
    if ((lista_personajes == [])):
        print("Verificar que la lista no esté vacía")
        return False
    else:
        for superheroe in lista_personajes:
            if (type(superheroe[value] == int) or type(superheroe[value]) == float):
                if ((maximo == None) or (maximo < superheroe[value])):
                    maximo = superheroe[value]
                    nombre = superheroe["nombre"]
            else:
                print("Verifique que el dato sea Int o Float")
                return False
    return (nombre, maximo)

#Función Obtener Mínimo:
""" Esta funcion nos permite obtener el valor mínimo de una clave. ESte verifica que el valor sea un número entero o un decimal, y
pasa la lista y la clave por parametro. En caso de que retorne False es porque la lista esta vacía o el valor que encontro no es ni int ni float.
En caso de que sea correcto, va a retornar el máximo junto con el nombre del superheroe. """

def obtener_minimo (value: str, lista_personajes: list):
    minimo = None
    nombre = " "
    if ((lista_personajes == [])):
        print("Verificar que la lista no esté vacía")
        return False
    else:
        for superheroe in lista_personajes:
            if (type(superheroe[value]) == int or type(superheroe[value]) == float):
                if (minimo == None or minimo > superheroe[value]):
                    minimo = superheroe[value]
                    nombre = superheroe["nombre"]
            else:
                print("Verificar que el dato sea Int o Float")
                return False
    return (nombre, minimo)

#Función Obtener Dato y Cantidad (0 mínimo, 1 máximo):
""" Esta funcion nos permite obtener el valor minimo,o el valor maximo. (tambien uno exacto) de una clave mostrando al superheroe. Este
verifica que el valor sea un número entero o un decimal. Pasando la clave, el número del maximo = 1, minimo = 0, o al valor exacto que le pasamos, y la lista por parametro. 
Va retornar False cuando la lista esté vacía o el valor que se encontro no sea ni int ni float.
En caso de que sea correctamente, va retorna la lista nueva con los superheroes que cumplan con los valores pasados."""

def obtener_dato_cantidad (value: str, number:int, lista_personajes: list):
    lista_nueva = []
    if (numero == 0):
        numero = obtener_minimo(value, lista_personajes)
    elif (numero == 1):
        numero = obtener_maximo(value, lista_personajes)
    else:
        numero = numero
    for superheroe in lista_personajes:
        if (superheroe[value] == number):
            lista_nueva.append(superheroe)
    if (lista_nueva == []):
        return("ERROR. No se encontraron resultados, la lista esta vacia")
    else:
        return lista_nueva

#Función Imprimir Héroes:
"""ESta funcion nos permite imprimir una lista completa que le pasemos por parametro. Va a retornar False si la lista se encuentra vacia."""
def stark_imprimir_heroes (lista_personajes: list):
    if ((lista_personajes == [])):
        print("Verificar que la lista no esté vacía")
        return False
    else:
        return(lista_personajes)

#Función Sumar Dato de Héroe:
""" Esta funcion nos permite realizar la suma de los valores de una clave, que esta se pasa por parametro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, va retornar False. Si es correcto retorna el resultado de la suma como entero."""
def sumar_dato_heroe (value: str, lista_personajes: list):
    sumar = 0
    for superheroe in lista_personajes:
        if (superheroe == {} or type(superheroe) != dict):
            print("ERROR. Verificar que el diccionario no esté vacío o que el dato sea Dict")
            return False
        else:
            sumar = sumar + int(float(superheroe[value]))
    return sumar

#Función Dividir:
""" Esta funcion nos permite realizar una división entre dos números enteros que le pasamos por parámetro, retornando el resultado. Si el divisor que pasamos es cero, retorna False."""
def dividir (dividendo: int, divisor: int):
    division = None
    if (divisor == 0):
        return False
    else:
        division = (dividendo / divisor)
    return (f"{division:.2f}")

#Función Calcular Promedio:
""" Esta funcion nos permite calcular el promedio de todos los valores de una determinada clave, que esta se pasa por parámetro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, va retornar False. Si no, va a retornar el promedio. """
def calcular_promedio (value: str, lista_personajes: list):
    contador = (len(lista_personajes))
    acumulador = (sumar_dato_heroe(value, lista_personajes))
    promedio = float((dividir(acumulador, contador)))
    return (f"{promedio:.2f}")

#Función Mostrar Dato Promedio:
""" ESta funcion nos permite calcular el promedio de todos los valores de una determinada clave,que esta se pasa por parámetro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, o que los valores no sean int o float, va a retornar False. Si no, va a retornar el promedio. """ 
def mostrar_promedio_dato (value: str, lista_personajes: list):
    if (lista_personajes == []):
        print("Verificar que la lista no esté vacía")
        return False
    for superheroe in lista_personajes:
        if (type(superheroe[value] == int) or type(superheroe[value]) == float):
            return calcular_promedio(value, lista_personajes)
        else:
            print("Verificar que el dato sea Int o Float")
            return False

#Función Imprimir Menu:
""" Esta funcion nos permite imprimir un menú de opciones sin de pasarle parámetros."""
def imprimir_menu ():
    print(
    "Opciones: \n"
    "1) Obtener Dato \n"
    "2) Obtener Nombre \n"
    "3) Obtener Nombre y Dato \n"
    "4) Obtener Máximo \n"
    "5) Obtener Mínimo \n"
    "6) Obtener Dato y Cantidad \n"
    "7) Imprimir Héroes \n"
    "8) Sumar Dato de Héroe \n"
    "9) Dividir \n"
    "10) Calcular Promedio \n"
    "11) Mostrar Dato Promedio \n"
    "12) Validar Entero \n"
    "13) Salir")

#Función Validar Entero:
"""Esta funcion nos permite reconocer digitos en un string, pasandoselo como parámetro. Si es verdadero va a retornar dígitos numéricos, si no, va retornar False. """
def validar_entero (numero: str):
    return numero.isdigit()

#Función Imprimir Menu Stark:
"""Esta funcion nos permite guardar la opción elegida sin tener de pasarle parámetros. Si la opción elegida no es un número, o no se encuentre dentro del rango puesto
va a retornar False, si no va retornar la opción elegida como un entero. """
def stark_menu_principal ():
    opcion = input("Ingrese la opción (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):")
    if ((validar_entero(opcion) == True) and ((int(opcion) > 0) and (int(opcion) <= 13))):
        return int(opcion)
    else:
        return False
    
#Función Stark Marvel App:
"""Esta funcion permite mostrarnos el menú de opciones, guarda la opción que pusimos e inicia la función, pasándole la lista por parámetro. """
def stark_marvel_app (lista_personajes: list):
    bandera = True
    normalizar = normalizar_datos_stark(lista_personajes)
    imprimir_menu()
    if (normalizar == True):
        while(bandera == True):
            opcion = stark_menu_principal()
            match (opcion):
                case (1):
                    print(obtener_dato("altura", lista_personajes[0]))
                case (2):
                    print(obtener_nombre(lista_personajes[1]))
                case (3):
                    print(obtener_nombre_y_dato("fuerza", lista_personajes[2]))
                case (4):
                    print(obtener_maximo("peso", lista_personajes))
                case (5):
                    print(obtener_minimo("peso", lista_personajes))
                case (6):
                    print(obtener_dato_cantidad("fuerza", 1, lista_personajes))
                case (7):
                    print(stark_imprimir_heroes(lista_personajes))
                case (8):
                    print(sumar_dato_heroe("altura", lista_personajes))
                case (9):
                    print(dividir(24, 4))
                case (10):
                    print(calcular_promedio("peso", lista_personajes))
                case (11):
                    print(mostrar_promedio_dato("fuerza", lista_personajes))
                case (12):
                    print(validar_entero("7"))
                case (13):
                    bandera = False

        else:
            print("Error al normalizar los datos, no puede continuar")

stark_marvel_app(lista_personajes)

#Desafío Resuelto
"""Esta funcion nos permite agrupar a los superhéroes por género, pasándole o una clave o el género por parámetro con la lista.
El parámetro elegido va a ser la clave y la lista nueva va a agruparlos. Esta va aretornar la lista nueva. """
def obtener_superheroes_por_genero(lista_personajes:list, genero:str):
    lista_heroes_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            lista_heroes_genero.append(superheroe)
    return lista_heroes_genero

""" Esta funcion agrupar o sacar la cantidad de superhéroes dependiendo la clave que le pasemos por parámetro. Si pasamos cantidad, nos va a devolver eso
si no, va a devolver la agrupacion """
def agrupar(clave: str, tipo: str):
    lista[valor] = []
    cantidad = {}
    lista = {}
    for superheroe in lista_personajes: 
        valor = superheroe[clave].capitalize()
        nombre = superheroe["nombre"]
        if valor in cantidad:
            cantidad[valor] = cantidad[valor] + 1
            lista[valor].append(superheroe)
        else:
            cantidad[valor] = 1
            lista[valor] = [nombre]  

    if tipo == "cantidad": 
        return cantidad
    
    elif tipo == "agrupar":
        return lista

def stark_marvel_app(lista_personajes:list):
    normalizar = True
    bandera = True

    while normalizar == True: 
        opcion = stark_menu_principal()
        while bandera == True:
            if opcion != 1:
                print("Hace falta normalizar los datos")
                opcion = stark_menu_principal()
            elif opcion == 1:
                normalizar_datos_stark(lista_personajes)
                bandera = False

        if opcion == 2:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'NB')
            stark_imprimir_heroes(heroe_por_genero)
            print(stark_imprimir_heroes(heroe_por_genero))

        elif opcion == 3:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'F')
            obtener_maximo(heroe_por_genero, "altura")
            print(obtener_maximo(heroe_por_genero, "altura"))

        elif opcion == 4:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'M')
            obtener_maximo(heroe_por_genero, "altura")
            print(obtener_maximo(heroe_por_genero, "altura"))

        elif opcion == 5:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'M')
            obtener_minimo(heroe_por_genero, "fuerza")
            print(obtener_minimo(heroe_por_genero, "fuerza"))

        elif opcion == 6:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'NB')
            obtener_minimo(heroe_por_genero, "fuerza")
            print(obtener_minimo(heroe_por_genero, "fuerza"))


        elif opcion == 7:
            heroe_por_genero = obtener_superheroes_por_genero(lista_personajes , 'NB')
            calcular_promedio(heroe_por_genero,"fuerza")
            print(mostrar_promedio_dato(heroe_por_genero,"fuerza"))


        elif opcion == 8:
            agrupar("color_ojos" , "cantidad")
            print("Color de ojos: \n{0}".format (agrupar("color_ojos" , "cantidad")))


        elif opcion == 9:
            agrupar("color_pelo" , "cantidad")
            print("Color de pelo: \n{0}".format (agrupar("color_pelo" , "cantidad")))

        elif opcion == 10:
            agrupar("color_ojos" , "agrupar")
            print("Color de ojos: \n{0}".format (agrupar("color_ojos" , "agrupar")))

        elif opcion == 11:
            agrupar("inteligencia" , "agrupar")
            print("Inteligencia: \n{0}".format (agrupar("inteligencia" , "agrupar")))

        elif opcion == 12:
            bandera = False

    print("Error al normalizar los datos, no puede continuar")



from data_stark import lista_personajes
stark_marvel_app(lista_personajes)

