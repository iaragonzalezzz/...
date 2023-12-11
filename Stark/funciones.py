from data_stark import lista_personajes
#Nombre: Iara
#Apellido: Gonzalez


def encontrar_superheroes_NB (key , value):
    lista_NB = []
    for personajes in lista_personajes:
        if personajes[key] == value:
            lista_NB.append(personajes["nombre"])
    return lista_NB


def encontrar_maximos(key , value):
    maximo = 0
    for personajes in lista_personajes:
        personajes["altura"] = float(personajes["altura"])
        if personajes[key] == value and maximo < personajes["altura"]:
            maximo = personajes["altura"]
            nombre = personajes["nombre"]
    return nombre


def encontrar_minimos(key , value):
    minimo = 99999999999999999999
    for personaje in lista_personajes:
        personaje["fuerza"] = float(personaje["fuerza"])
        if personaje[key] == value and minimo > personaje["fuerza"]:
            minimo = personaje["fuerza"]
            nombre = personaje["nombre"]
    return nombre


def encontrar_promedio (key , value):
    contador_NB = 0
    acumulador_NB = 0
    for personajes in lista_personajes:    
        if personajes[key] == value:
            personajes["fuerza"] = float(personajes["fuerza"])
            contador_NB = contador_NB + 1
            acumulador_NB = acumulador_NB + personajes["fuerza"]
    promedio_NB = acumulador_NB / contador_NB
    return promedio_NB

def determinar_tipos (key , tipo):
    cantidad = {}
    listado = {}
    for heroe in lista_personajes: 
        valor = heroe[key].capitalize()
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

