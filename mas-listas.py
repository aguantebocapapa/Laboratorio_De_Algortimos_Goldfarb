import random

def ejercicio1():
    nombres = []
    largo = 0
    nombrelargo = ""
    for i in range(10, 0, -1):
        nombre = str(input(f"Ingrese {i} nombres para agregar a la lista: "))
        nombres.append(nombre)
    for i in nombres:
        if len(i) > largo:
            largo = len(i)
            nombrelargo = i
    print(f"El nombre mas largo es: {nombrelargo}, tiene {largo} caracteres.")
    return nombres

def ejercicio2():
    vocales = "aeiou"
    nombresv = ejercicio1()
    cantVocales = 0
    for nombre in nombresv:
        for letra in nombre:
            if letra in vocales:
                cantVocales = cantVocales + 1
    print(f"Entre todos los nombres hay {cantVocales} vocales")

def ejercicio3():
    numeros = []
    nuevos_numeros = []
    while 0 == 0:
        numero = int(input("Ingrese un número (0 para terminar el bucle): "))
        if numero != 0:
            numeros.append(numero)
        else:
            break
    factor = int(input("Elige un factor para multiplicar todos los números: "))
    for i in numeros:
        numero = i * factor
        nuevos_numeros.append(numero)
    print(nuevos_numeros)

def dar_carta():
    # Valores posibles
    numeros_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    palos_posibles = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    carta = []
    
    # Distribución de valores
    numero = random.choice(numeros_posibles)
    palo = random.choice(palos_posibles)
    carta.append(numero)
    carta.append(palo)
    return carta

def definir_mano():
    Carta1 = dar_carta()
    Carta2 = dar_carta()
    Carta3 = dar_carta()
    Carta4 = dar_carta()
    Carta5 = dar_carta()
    Carta6 = dar_carta()
    Carta7 = dar_carta()
    Carta8 = dar_carta()
    mano = [Carta1, Carta2, Carta3, Carta4, Carta5, Carta6, Carta7, Carta8]
    return mano

def ejercicio4():
    Mano = definir_mano()
    while 0 == 0:         
        print(f"Mano actual: {Mano}")
        menu_avanzado = int(input(f"--- ♤ Menu Mano ♤ --- \n1 - Modificar Mano \n2 - Cerrar programa \n"))
        if menu_avanzado == 1:
            while 0 == 0:
                cambiar = int(input("Ingrese que carta desea cambiar: "))
                if cambiar > len(Mano):
                    print("Debe ingresar un número del 1 al 8 para cambiar una de las cartas de la lista")
                else:
                    cambiar = cambiar-1
                    Mano[cambiar] = dar_carta()
                    break
        elif menu_avanzado == 2:
            print("Cerrando programa...")
            break
        else:
            print("Opción no disponible.")

while 0 == 0:
    print("--- Este es el menú de ejecución ---")
    ejercicio = int(input("Ingrese el ejercicio desea corregir (ingrese 0 para terminar): "))
    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    elif ejercicio == 4:
        ejercicio4()
    elif ejercicio == 0:
        print("Finalizando programa...")
        break
    else:

        print("Debe ingresar un ejercicio del 1 al 4")
