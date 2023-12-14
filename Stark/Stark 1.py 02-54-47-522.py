from data_stark import lista_personajes

#Nombre: Iara
#Apellido: Gonzalez

while True:


    print('''
   A) Imprimir por consola todos los datos de cada superhéroe
\n B) Mostrar la identidad y el peso del superhéroe con mayor fuerza 
\n C) Mostrar nombre e identidad del superhéroe más bajo 
\n D) Determinar el peso promedio de los superhéroes masculinos 
\n E) mostrar nombre y peso de los superhéroes los cuales su fuerza supere a la fuerza promedio de todas las 
superhéroes de género femenino 
\n F) Salir''' )

    opcion = input("Ingrese una opcion: ")

    if opcion == "A":
        for personaje in lista_personajes: 
            nombre = personaje["nombre"]
            identidad = personaje["identidad"]
            empresa = personaje["empresa"]
            altura = personaje["altura"]
            peso = personaje["peso"]
            genero = personaje["genero"]
            color_ojos = personaje["color_ojos"]
            color_pelo = personaje["color_pelo"]
            fuerza = personaje["fuerza"]
            inteligencia = personaje["inteligencia"]

            print(f"Superheroe: {nombre}\n, Identidad: {identidad}\n , Empresa: {empresa}\n , Altura: {altura}\n , Peso: {peso}\n , Genero: {genero}\n , Color de ojos: {color_ojos}\n , Color de ojos: {color_ojos}\n , Fuerza: {fuerza}\n , Inteligencia:{inteligencia}")

    elif opcion == "B":
        #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
        fuerza = lista_personajes[0]["fuerza"]
        mayor_fuerza = int(fuerza)
        identidad_mayor_fuerza = lista_personajes[0]["identidad"]
        peso_maximo = lista_personajes[0]["peso"]

        for personaje in lista_personajes:
            if int(personaje["fuerza"]) > mayor_fuerza:
                    mayor_fuerza = int(personaje["fuerza"])
                    identidad_mayor_fuerza = personaje["identidad"]
                    peso_maximo = personaje["peso"]

        print(f"La identidad del personaje es: {identidad_mayor_fuerza} Y su peso es: {peso_maximo}")


    elif opcion == "C":
        #. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
        altura = lista_personajes[0]["altura"]
        altura_minima = float(altura)
        nombre_minimo = lista_personajes[0] ["nombre"]
        identidad_minima = lista_personajes[0]["identidad"]

        for personaje in lista_personajes:
            if float(personaje["altura"]) < altura_minima:
                    altura_minima = float(personaje["altura"])
                    identidad_minima = personaje["identidad"]
                    nombre_minimo = personaje["nombre"]

        print(f"La identidad del superheroe es: {identidad_minima} Y su nombre es: {nombre_minimo}")


    elif opcion == "D":
        acumulador_peso_m = 0
        contador_m = 0

        for personajes in lista_personajes:
            genero = personajes["genero"]
            if(personajes["genero"] == "M"):
                peso_m = float(personajes["peso"])
                contador_m = contador_m + 1
                acumulador_peso_m = acumulador_peso_m + peso_m
        
        promedio_m = acumulador_peso_m / contador_m

        print(f"El promedio de peso de los masculinos es: {promedio_m}")

    elif opcion == "E":
        acumulador_f = 0
        contador_f = 0  

        for personajes in lista_personajes:
            if personajes ["genero"] == "F":
                contador_f = contador_f + 1
                fuerza_mujer = personajes ["fuerza"]
                fuerza_mujer = float(fuerza_mujer)
                acumulador_f = acumulador_f + fuerza_mujer
                
        if contador_f != 0:
            promedio_f = acumulador_f / contador_f

        else: 
            print("No hay se puede calcular el promedio")


        for personajes in lista_personajes:
            if int(personajes["fuerza"]) > promedio_f:
                print(f"El nombre es: {personajes['nombre']} y su peso es:  {personajes['peso']}")


    elif opcion == "F":
        print("Saliste del menu")
        break
