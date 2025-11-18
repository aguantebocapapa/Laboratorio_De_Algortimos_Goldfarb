import random

matriz_tesoro = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

matriz_guia = [
    ['?¿', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10' ],
    [1, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [2, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [3, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [4, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [5, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [6, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [7, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [8, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [9, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
    [10, '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵', '🔵'],
]

#Crear coordenadas de bombas
def Seleccionar_Bomba():
    bomba_coordenadas = []
    fila_bomba = random.randint(0, 9)
    columna_bomba = random.randint(0, 9)
    bomba_coordenadas.append(fila_bomba)
    bomba_coordenadas.append(columna_bomba)
    return bomba_coordenadas

#Crear bombas
bomba1 = Seleccionar_Bomba()
bomba2 = Seleccionar_Bomba()
bomba3 = Seleccionar_Bomba()

#Verificar que sean diferentes
while bomba1 == bomba2 or bomba1 == bomba3 or bomba2 == bomba3:
    bomba1 = Seleccionar_Bomba()
    bomba2 = Seleccionar_Bomba()
    bomba3 = Seleccionar_Bomba()

#Posicionar bombas
matriz_tesoro [bomba1[0]] [bomba1[1]] = 1
matriz_tesoro [bomba2[0]] [bomba2[1]] = 1
matriz_tesoro [bomba3[0]] [bomba3[1]] = 1

#Variable juego
def Ejecutar_Juego():
    intentos = 5
    bombas_encontradas = 0
    while intentos > 0:
        try:
            for fila in matriz_guia:
                print("\n------------------------------------------------------")
                for elemento in fila:
                    print(elemento, end= " | ")
            print(f"\nIntentos disponibles : {intentos}")
            coordenada_x = int(input("Ingrese la coordenada X donde crees que esta la bomba (1 - 10): "))
            coordenada_y = int(input("Ingrese la coordenada Y donde crees que esta la bomba (1 - 10): "))   
            try:
                if matriz_tesoro [coordenada_x] [coordenada_y]:
                    print("Felicidades, haz encontrado una bomba 👏👏")
                    intentos += 10
                    print("Intentos restaurados. \nTienes 5 intentos otra vez.")
                    bombas_encontradas += 1
                    matriz_guia [coordenada_x] [coordenada_y] = '✅'
                else:
                    print("No encontraste una bomba.")
                    matriz_guia [coordenada_x] [coordenada_y] = '❌'
            except IndexError:
                print("Por favor ingrese un número del 1 al 10 \n Poner algo indebido te va a quitar un intento extra.")
                intentos -= 1
        except ValueError:
            print("Por favor ingrese un número, pierdes un intento extra por bobo")
            intentos -= 1
        if bombas_encontradas == 3:
            print("Haz encontrado las 3 bombas.")
            break
        intentos -= 1
        if intentos == 0:
            print("JAJAJA PERDISTE NUB")
            break

#Menu interactivo
while 0 == 0:
    print("Bienvenido al buscador de tesoros 💰💎")
    try:
        menu = int(input(f"Ingrese que desea hacer: \n1. Jugar \n2. Salir \n"))
        if menu == 1:
            Ejecutar_Juego()
            break
        elif menu == 2:
            break
        else:
            print("Ingrese 1 o 2. Ni mas, ni menos")
    except ValueError:
        print("Por favor ingrese 1 o 2, no se haga el payaso")
