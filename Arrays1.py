def ejercicio1():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    print("Recorrido de la matriz:")
    for fila in matriz:
        
        print(f"\n-----------")
        for elemento in fila:
            print(elemento, end=" | ")

def ejercicio2():
    suma_total = 0
    matriz = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]

    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    print(suma_total)

def ejercicio3():
    matriz = [
        ["1", "H", "4", "2"],
        ["F", "+", "L", "Kira"],
        ["Maxi", "Ema", "Ferra", "7"],
        ["Veneco", "0", "a", "A"]]
    i = 0
    try:
        fila = int(input("Ingrese que fila desea revisar: ")) - 1
        columna = int(input("Ingrese que columna desea revisar: ")) - 1
        for elemento in matriz[fila]:
            if i == columna:
                print(elemento)
            i += 1
    except IndexError:
        print("Pon por favor, una fila y columna del 1 al 4")

def ejercicio4():
    matriz = [
        [1, 2, 3, 4],
        [91218, 7, 45, 5],
        [36, 42, 21, 213],
        [543, 648, 325, 768]]
    mayor = 0
    
    for fila in matriz:
        for elemento in fila:
            if elemento > mayor:
                mayor = elemento
    print(f"El elemento mas grande de la matriz es: {mayor}")

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
