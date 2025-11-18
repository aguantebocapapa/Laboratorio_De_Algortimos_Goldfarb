
matriz_tateti = [
    ["00", "Y1", "Y2", "Y3"],
    ["X1", "🔵", "🔵", "🔵"],
    ["X2", "🔵", "🔵", "🔵"],
    ["X3", "🔵", "🔵", "🔵"]
]


def Imprimir_Matriz(matriz):
    for fila in matriz:
        print("\n-------------------")
        for elemento in fila:
            print(elemento, end=" | ")
        print() 


def Seleccionar_Casillero(jugador):
    try:
        x = int(input(f"\n({jugador}) Ingrese la coordenada X (1-3): "))
        y = int(input(f"({jugador}) Ingrese la coordenada Y (1-3): "))
        return [x, y]
    except ValueError:
        return None


def Comprobar_Espacio(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento == "🔵":
                return True
    return False


def Comprobar_Victoria(m):
    
    for i in range(1, 4):
        if m[i][1] != "🔵" and m[i][1] == m[i][2] == m[i][3]:
            return True
   
    for j in range(1, 4):
        if m[1][j] != "🔵" and m[1][j] == m[2][j] == m[3][j]:
            return True
    
    if m[1][1] != "🔵" and m[1][1] == m[2][2] == m[3][3]:
        return True
   
    if m[1][3] != "🔵" and m[1][3] == m[2][2] == m[3][1]:
        return True
    return False



print(f"\n❌⭕❌ Bienvenido al tateti ❌⭕❌")

while True:
    Imprimir_Matriz(matriz_tateti)

 
    X = Seleccionar_Casillero("❌")
    if X is None or X[0] not in [1, 2, 3] or X[1] not in [1, 2, 3]:
        print("Coordenadas inválidas. Pierdes un turno.")
    elif matriz_tateti[X[0]][X[1]] != "🔵":
        print("Casilla ocupada. Pierdes un turno.")
    else:
        matriz_tateti[X[0]][X[1]] = "❌"

    Imprimir_Matriz(matriz_tateti)

    if Comprobar_Victoria(matriz_tateti):
        Imprimir_Matriz(matriz_tateti)
        print("\nGanador la ❌")
        break
    if not Comprobar_Espacio(matriz_tateti):
        print("\nNo hay más espacio. Empate.")
        break

 
    O = Seleccionar_Casillero("⭕")
    if O is None or O[0] not in [1, 2, 3] or O[1] not in [1, 2, 3]:
        print("Coordenadas inválidas. Pierdes un turno.")
    elif matriz_tateti[O[0]][O[1]] != "🔵":
        print("Casilla ocupada. Pierdes un turno.")
    else:
        matriz_tateti[O[0]][O[1]] = "⭕"

    if Comprobar_Victoria(matriz_tateti):
        Imprimir_Matriz(matriz_tateti)
        print("\nGanador el ⭕")
        break
    if not Comprobar_Espacio(matriz_tateti):
        print("\nNo hay más espacio. Empate.")
        break
