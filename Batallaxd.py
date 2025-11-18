import random

matriz_barco = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

matriz_guia = [
    ['?¿', '01' , '02', '03' , '04' , '05'],
    ['01', '🔵', '🔵', '🔵', '🔵', '🔵'],
    ['02', '🔵', '🔵', '🔵', '🔵', '🔵'],
    ['03', '🔵', '🔵', '🔵', '🔵', '🔵'],
    ['04', '🔵', '🔵', '🔵', '🔵', '🔵'],
    ['05', '🔵', '🔵', '🔵', '🔵', '🔵']
]

#Crear coordenadas de bombas
def Seleccionar_Barco():
    barco_coordenadas = []
    fila_barco = random.randint(0, 4)
    columna_barco = random.randint(0, 4)
    barco_coordenadas = [fila_barco, columna_barco]
    return barco_coordenadas

#Crear bombas
barco1 = Seleccionar_Barco()
barco2 = Seleccionar_Barco()
barco3 = Seleccionar_Barco()

#Verificar que sean diferentes
while barco1 == barco2 or barco1 == barco3 or barco2 == barco3:
    barco1 = Seleccionar_Barco()
    barco2 = Seleccionar_Barco()
    barco3 = Seleccionar_Barco()

#Posicionar bombas
matriz_barco [barco1[0]] [barco1[1]] = 1
matriz_barco [barco2[0]] [barco2[1]] = 1
matriz_barco [barco3[0]] [barco3[1]] = 1

#Variable juego
def Ejecutar_Juego():
    barcos_encontrados = 0
    while True:
        try:
            for fila in matriz_guia:
                print("\n-----------------------------")
                for elemento in fila:
                    print(elemento, end= " | ")
            coordenada_x = int(input("Ingrese la coordenada X donde crees que esta el barco (1 - 5): "))
            coordenada_y = int(input("Ingrese la coordenada Y donde crees que esta el barco (1 - 5): "))   
            try:
                if matriz_barco [coordenada_x] [coordenada_y]:
                    print("Felicidades, Le diste a un barco 👏👏")
                    barcos_encontrados += 1
                    matriz_guia [coordenada_x] [coordenada_y] = '✅'
                else:
                    print("\n\nLe diste al agua.")
                    matriz_guia [coordenada_x] [coordenada_y] = '❌'
            except IndexError:
                print("Por favor ingrese un número del 1 al 5.")
        except ValueError:
            print("Por favor ingrese un número.")
        if barcos_encontrados == 3:
            print("Haz encontrado los 3 barcos.")
            break
#Menu interactivo
while 0 == 0:
    print("Bienvenido a Batalla Naval ⚓🚢")
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
