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

while 0 == 0:
    print("--- Este es el menú de ejecución ---")
    ejercicio = int(input("Ingrese el ejercicio desea corregir (ingrese 0 para terminar): "))
    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    elif ejercicio == 0:
        print("Finalizando programa...")
        break
    else:
        print("Debe ingresar un ejercicio del 1 al 3")
