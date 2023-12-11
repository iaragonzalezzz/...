from data_stark import lista_personajes
# Gonzalez
# Iara

#Función Normalizar Datos:
"""Esta funcion nos permite normalizar los datos 'Fuerza', 'Peso' y 'Altura' ya que estos aparecen como tipo String, lo que hacemos es pasarlo a Int y Float, 
donde le paso una lista por parámetro y retorna valor True si los datos se normalizaron correctamente. 
En caso de que retorne False es porque la lista esta vacia, faltan datos, o porque ya se normalizo antes. """

def stark_normalizar_datos(lista_personajes: list):
    resultado = False
    if lista_personajes == []:
        print("ERROR. La lista se encuentra vacía")
        return False
    else:
        for personaje in lista_personajes:
            if type(personaje["altura"]) == float or type(personaje["peso"]) == float or type(personaje["fuerza"]) == int:
                print("ERROR, al normalizar los datos. Verificar que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
                return False
            else:
                personaje["altura"] = float(personaje["altura"])
                personaje["peso"] = float(personaje["peso"])
                personaje["fuerza"] = int(personaje["fuerza"])
                resultado = True
        if resultado == True:
            print("CORRECTO. Datos normalizados")
    return True

#Función Obtener Dato:
"""Esta funcion permite obtener un dato del diccionario. Este representa un solo heroe, y un str que representa el dato que queres obtener 
retorna el dato que pasaste por parametro, que es el estas buscando, si el diccionario esta vacío retorna False'''. """
def obtener_dato(heroe: dict , clave: str):
    if (heroe == {}):
        print("ERROR. La lista se encuentra vacía")
        return False
    dato_encontrado = heroe[clave]
    return dato_encontrado

#Función Obtener Nombre:
"""Esta funcion nos permite obtener el nombre del personaje en el diccionario. El parametro que recibe este
es un diccionario que representa a un solo héroe, es decir, va a retornar el nombre del superheroe, si el diccionario esta vacío va a retornar False. """
def obtener_nombre(heroe: dict):
    if (heroe == {}):
        print("ERROR. La lista se encuentra vacía")
        return False
    nombre = obtener_dato(heroe , "nombre")
    return "Nombre: {0}".format(nombre)

#Función Obtener Nombre Y Dato:
"""Esta funcion nos permite obtener el valor de la clave nombre. Este pasa la clave como el diccionario por 
parámetro, retornando el valor correcto o un False si el diccionario se encuentra vacío o las claves no existan. """

def obtener_nombre_y_dato(heroe: dict, clave: str):
    if (heroe == {}):
        print("ERROR. La lista se encuentra vacía")
        return False
    nombre = heroe["nombre"]
    dato = heroe[clave]

    return "Nombre: {0} | {1}: {2} ".format(nombre , clave , dato)

#Función Obtener Máximo:
"""Esta funcion nos permite obtener el valor del máximo de una clave. Este verifica que el valor sea un numero entero o un decimal, y
pasa la lista y la clave por parametro. En caso de que retorne False es porque la lista esta vacía o el valor que encontro no es ni int ni float.
En caso de que sea correcto, va a retornar el máximo junto con el nombre del superheroe. """
def obtener_maximo(lista_personajes: list, clave: str):
    if (lista_personajes == [] and type(clave) != float and type(clave) != int):
        print("ERROR. La lista se encuentra vacía o el valor que encontro no es ni int ni float")
        return False
    else:
        maximo = lista_personajes [0]
        for heroe in lista_personajes:
            if heroe[clave] > maximo [clave]:
                maximo = heroe
    return maximo ["nombre"], maximo [clave]

#Función Obtener Mínimo:
""" Esta funcion nos permite obtener el valor mínimo de una clave. ESte verifica que el valor sea un número entero o un decimal, y
pasa la lista y la clave por parametro. En caso de que retorne False es porque la lista esta vacía o el valor que encontro no es ni int ni float.
En caso de que sea correcto, va a retornar el máximo junto con el nombre del superheroe. """
def obtener_minimo(lista_personajes:list , clave:str):
    if lista_personajes == [] and type(clave) != float and type(clave) != int:
        return False
    else:
        minimo = lista_personajes [0]
        for heroe in lista_personajes:
            if heroe[clave] < minimo [clave]:
                    minimo = heroe

    return minimo["nombre"], minimo[clave]

#Función Obtener Dato y Cantidad (0 mínimo, 1 máximo):
""" Esta funcion nos permite obtener el valor minimo,o el valor maximo. (tambien uno exacto) de una clave mostrando al superheroe. Este
verifica que el valor sea un número entero o un decimal. Pasando la clave, el número del maximo = 1, minimo = 0, o al valor exacto que le pasamos, y la lista por parametro. 
Va retornar False cuando la lista esté vacía o el valor que se encontro no sea ni int ni float.
En caso de que sea correctamente, va retorna la lista nueva con los superheroes que cumplan con los valores pasados."""
def obtener_dato_cantidad(lista_personajes:list , numero:int , clave:str): 
    lista_dato_cantidad = []
    if numero == 0:
        numero_elegido = obtener_minimo(lista_personajes, clave)

    elif numero == 1:
        numero_elegido = obtener_maximo(lista_personajes, clave)

    for heroe in lista_personajes:
        if heroe[clave] == numero_elegido[1] :
            lista_dato_cantidad.append(heroe['nombre'])
            lista_dato_cantidad.append(heroe[clave])

    return lista_dato_cantidad

#Función Imprimir Héroes:
"""ESta funcion nos permite imprimir una lista completa que le pasemos por parametro. Va a retornar False si la lista se encuentra vacia."""
def stark_imprimir_heroes(lista_personajes:list):
    if lista_personajes == []:
        print("ERROR. La lista se encuentra vacía")
        return False
    else:
        return lista_personajes

#Función Sumar Dato de Héroe:
""" Esta funcion nos permite realizar la suma de los valores de una clave, que esta se pasa por parametro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, va retornar False. Si es correcto retorna el resultado de la suma como entero."""
def sumar_dato_heroe(lista_personajes:list , clave:str):
    suma = 0
    for heroe in lista_personajes:
        if (heroe == {}):
            print("ERROR. Diccionario se encuentra vacío")
            return False
        else:
                suma = suma + heroe[clave] 
    return suma


""" Esta funcion nos permite realizar una división entre dos números enteros que le pasamos por parámetro, retornando el resultado. Si el divisor que pasamos es cero, retorna False."""
def dividir(dividendo:int,divisor:int):
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
    return resultado

#Función Calcular Promedio:
""" Esta funcion nos permite calcular el promedio de todos los valores de una determinada clave, que esta se pasa por parámetro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, va retornar False. Si no, va a retornar el promedio. """
def calcular_promedio(lista_personajes:list , clave:str):
    suma = sumar_dato_heroe(lista_personajes , clave)
    divisor = len(lista_personajes)
    resultado = dividir(suma , divisor)
    return resultado

#Función Mostrar Dato Promedio:
""" ESta funcion nos permite calcular el promedio de todos los valores de una determinada clave,que esta se pasa por parámetro como la lista. Si el diccionario se encuntra vacio
o no sea del tipo diccionario, o que los valores no sean int o float, va a retornar False. Si no, va a retornar el promedio. """ 
def mostrar_promedio_dato(lista_personajes:list,clave:str):
    if (lista_personajes == []):
        print("ERROR. La lista se encuentra vacía")
        return False
    for heroe in lista_personajes:
        if type(heroe [clave]) == int or type(heroe[clave]) == float:
            return calcular_promedio(lista_personajes , clave)

def validar_entero(numero:str):
    return numero.isdigit()


def imprimir_menu():
    print('''
1- Normalizar datos 
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10. Listar todos los superhéroes agrupados por color de ojos.
11. Listar todos los superhéroes agrupados por tipo de inteligencia
12- Salir''')

def stark_menu_principal():
    opcion = input("Ingrese la opción (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):")
    if ((validar_entero(opcion) == True) and ((int(opcion) > 0) and (int(opcion) <= 13))):
        return int(opcion)
    else:
        return False
    

def obtener_superheroes_por_genero(lista_personajes:list , genero:str):
    superheroes_genero = []
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            superheroes_genero.append(superheroe)
    return superheroes_genero

def agrupar(clave: str, tipo: str):
    cantidad = {}
    listado = {}
    for heroe in lista_personajes: 
        valor = heroe[clave].capitalize()
        nombre = heroe["nombre"]
        if valor in cantidad:
            cantidad[valor] = cantidad[valor] + 1
            listado[valor].append(nombre) 
        else:
            cantidad[valor] = 1
            listado[valor] = [nombre]  
    if tipo == "cantidad": 
        return cantidad
    elif tipo == "agrupar":
        return listado

def stark_marvel_app(lista_personajes:list):
    bandera = True
    bandera_1 = True

    while bandera == True: 
        opcion = stark_menu_principal()
        while bandera_1 == True:
            if opcion != 1:
                print("ERROR. Tiene que normalizar los datos")
                opcion = stark_menu_principal()
            elif opcion == 1:
                stark_normalizar_datos(lista_personajes)
                bandera_1 = False
        if opcion == 2:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes ,"NB")
            stark_imprimir_heroes(heroe_genero)
            print(stark_imprimir_heroes(heroe_genero))

        elif opcion == 3:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes , "F")
            obtener_maximo(heroe_genero, "altura")
            print(obtener_maximo(heroe_genero, "altura"))

        elif opcion == 4:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes , "M")
            obtener_maximo(heroe_genero, "altura")
            print(obtener_maximo(heroe_genero, "altura"))

        elif opcion == 5:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes , "M")
            obtener_minimo(heroe_genero, "fuerza")
            print(obtener_minimo(heroe_genero, "fuerza"))

        elif opcion == 6:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes , "NB")
            obtener_minimo(heroe_genero, "fuerza")
            print(obtener_minimo(heroe_genero, "fuerza"))
        elif opcion == 7:
            heroe_genero = obtener_superheroes_por_genero(lista_personajes , "NB")
            calcular_promedio(heroe_genero,"fuerza")
            print(mostrar_promedio_dato(heroe_genero,"fuerza"))
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
            agrupar("inteligencia","agrupar")
            print("Inteligencia: \n{0}".format (agrupar("inteligencia" , "agrupar")))
        elif opcion == 12:
            bandera = False

stark_marvel_app(lista_personajes)

