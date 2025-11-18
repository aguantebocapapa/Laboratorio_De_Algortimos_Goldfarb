Matriz_Listas = [[]]

def Crear_Lista(Matriz_Listas):
    lista_nueva = []
    Matriz_Listas.append(lista_nueva)
    print("Se creó una nueva lista.")
    return Matriz_Listas

def Agregar_Numero(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea agregar el número \nFilas disponibles: {len(Matriz_Listas)}\n"))
        num = int(input("Ingrese el número que desea agregar: "))
        Matriz_Listas[numFila].append(num)
        print("Número agregado correctamente.")
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

def Busqueda_Secuencial(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea usar para la búsqueda \nFilas disponibles: {len(Matriz_Listas)}\n"))
        num = int(input("Ingrese qué número desea buscar: "))
        for i in range(len(Matriz_Listas[numFila])):
            if Matriz_Listas[numFila][i] == num:
                print(f"Número encontrado en la posición {i}")
                return i
        print("Número no encontrado.")
        return -1
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

def Busqueda_Binaria(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea usar para la búsqueda \nFilas disponibles: {len(Matriz_Listas)}\n"))
        if Matriz_Listas[numFila] == sorted(Matriz_Listas[numFila]):
            num = int(input("Ingrese qué número desea buscar: "))
            izquierda = 0
            derecha = len(Matriz_Listas[numFila]) - 1
            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                if Matriz_Listas[numFila][medio] == num:
                    print(f"Número encontrado en la posición {medio}")
                    return medio
                elif Matriz_Listas[numFila][medio] < num:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1
            print("Número no encontrado.")
            return -1
        else:
            print("No puede buscar en esta lista, está desordenada.")
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

def Ordenamiento_Insercion(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea ordenar \nFilas disponibles: {len(Matriz_Listas)}\n"))
        for i in range(1, len(Matriz_Listas[numFila])):
            key = Matriz_Listas[numFila][i]
            j = i - 1
            while j >= 0 and key < Matriz_Listas[numFila][j]:
                Matriz_Listas[numFila][j + 1] = Matriz_Listas[numFila][j]
                j -= 1
            Matriz_Listas[numFila][j + 1] = key
        print("Lista ordenada por Inserción:", Matriz_Listas[numFila])
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

def Ordenamiento_Burbuja(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea ordenar \nFilas disponibles: {len(Matriz_Listas)}\n"))
        n = len(Matriz_Listas[numFila])
        for i in range(n - 1):
            Hay_Cambio = False
            for j in range(0, n - i - 1):
                if Matriz_Listas[numFila][j] > Matriz_Listas[numFila][j + 1]:
                    Matriz_Listas[numFila][j], Matriz_Listas[numFila][j + 1] = Matriz_Listas[numFila][j + 1], Matriz_Listas[numFila][j]
                    Hay_Cambio = True
            if not Hay_Cambio:
                break
        print("Lista ordenada por Burbuja:", Matriz_Listas[numFila])
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

def Ordenamiento_Seleccion(Matriz_Listas):
    try:
        numFila = int(input(f"Ingrese a qué fila de la matriz desea ordenar \nFilas disponibles: {len(Matriz_Listas)}\n"))
        n = len(Matriz_Listas[numFila])
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if Matriz_Listas[numFila][j] < Matriz_Listas[numFila][minimo]:
                    minimo = j
            Matriz_Listas[numFila][i], Matriz_Listas[numFila][minimo] = Matriz_Listas[numFila][minimo], Matriz_Listas[numFila][i]
        print("Lista ordenada por Selección:", Matriz_Listas[numFila])
    except (IndexError, ValueError):
        print("Error: fila inválida o dato no numérico.")

# --- Menú principal ---
while True:
    try:
        menu = int(input(
            "\nBienvenido al sistema de ordenación de números. Ingrese qué desea hacer: \n"
            "1 Crear una nueva lista\n"
            "2 Agregar un número a una lista\n"
            "3 Buscar un número secuencialmente\n"
            "4 Buscar un número de forma binaria\n"
            "5 Ordenar una fila por método de inserción\n"
            "6 Ordenar una fila por el método burbuja\n"
            "7 Ordenar una fila por el método de selección\n"
            "8 Salir\n"
        ))

        if menu == 1:
            Crear_Lista(Matriz_Listas)
        elif menu == 2:
            Agregar_Numero(Matriz_Listas)
        elif menu == 3:
            Busqueda_Secuencial(Matriz_Listas)
        elif menu == 4:
            Busqueda_Binaria(Matriz_Listas)
        elif menu == 5:
            Ordenamiento_Insercion(Matriz_Listas)
        elif menu == 6:
            Ordenamiento_Burbuja(Matriz_Listas)
        elif menu == 7:
            Ordenamiento_Seleccion(Matriz_Listas)
        elif menu == 8:
            print("Cerrando Programa...")
            break
        else:
            print("Ingrese un número del 1 al 8")

    except ValueError:
        print("Error: debe ingresar un número entre 1 y 8.")
