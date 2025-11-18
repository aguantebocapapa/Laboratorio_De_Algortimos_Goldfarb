def ejercicio1():
    matriz = [
        [12, 23, 432, 6],
        [674, 35, 532, 7],
        [4, 100, 204, 302],
        [173, 786, 123, 321]]
    fila1 = 0
    fila2 = 0
    fila3 = 0
    fila4 = 0
    col1 = 0
    col2 = 0
    col3 = 0
    col4 = 0
    for i in matriz[0]:
        fila1 += i
    for i in matriz[1]:
        fila2 += i
    for i in matriz[2]:
        fila3 += i
    for i in matriz[3]:
        fila4 += i
    for fila in matriz:
        i = 0
        for elemento in fila:
            if i == 0:
                col1 += elemento
            elif i == 1:
                col2 += elemento
            elif i == 2:
                col3 += elemento
            elif i == 3:
                col4 += elemento
            i += 1
    print(f"Fila 1: {fila1}, Fila 2: {fila2}, Fila 3: {fila3}, Fila 4: {fila4} \nColumna 1: {col1}, Columna 2: {col2}, Columna 3: {col3}, Columna 4: {col4}")


def ejercicio2():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    matriz_cambiada = [
        [],
        [],
        [],
        []
    ]
    for fila in matriz:
        i = 0
        for elemento in fila:
            if i == 0:
                matriz_cambiada[0].append(elemento)
            elif i == 1:
                matriz_cambiada[1].append(elemento)
            elif i == 2:
                matriz_cambiada[2].append(elemento)
            elif i == 3:
                matriz_cambiada[3].append(elemento)
            i += 1


    for fila in matriz_cambiada:
        print("\n-----------------")
        for elemento in fila:
            print(elemento, end=" | ")


def ejercicio3():
    matriz = [
        [1, 5, 3, 5],
        [8, 5, 9, 2],
        [4, 5, 6, 7]
    ]
    numero = int(input("Ingrese un número para buscarlo en la matriz: "))
    veces_repetido = 0
    for fila in matriz:
        for elemento in fila:
            if elemento == numero:
                veces_repetido += 1
    print(f"el numero {numero} aparece {veces_repetido} veces en la matriz.")

def ejercicio4():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    promedio = 0
    for fila in matriz:
        for elemento in fila:
            promedio += elemento
    promedio = promedio / 16
    matriz_cambiada = [
        [],
        [],
        [],
        []
    ]
    i = 0
    for fila in matriz:
        for elemento in fila:
            if i == 0:
                if elemento < promedio:
                    elemento = promedio
                matriz_cambiada[0].append(elemento)
            elif i == 1:
                if elemento < promedio:
                    elemento = promedio
                matriz_cambiada[1].append(elemento)
            elif i == 2:
                if elemento < promedio:
                    elemento = promedio
                matriz_cambiada[2].append(elemento)
            elif i == 3:
                if elemento < promedio:
                    elemento = promedio
                matriz_cambiada[3].append(elemento)
        i += 1
    for fila in matriz_cambiada:
        print("\n-----------------")
        for elemento in fila:
            print(elemento, end=" | ")
            
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
