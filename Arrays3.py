def ejercicio1():
    matriz = [
        [1, 2, 3, 1],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [1, 14, 15, 1]
    ]
    suma = 0
    suma += matriz[0] [0] + matriz [0] [-1]
    suma += matriz[-1] [0] + matriz [-1] [-1]
    print(suma)
    
def ejercicio2():
    matriz = [
        [4, 752, 1],
        [5, 751, 2],
        [3, 749, 753]
    ]

    suma_primaria = matriz[0] [0] + matriz[1] [1] + matriz [2] [2]
    suma_secundaria = matriz[0] [2] + matriz[1] [1] + matriz [2] [0]
    print(f"El resultado de la suma primaria es: {suma_primaria} \nEl resultado de la suma secundaria es: {suma_secundaria}")

def ejercicio3():
    indice = int(input("Ingrese de cuanto quiere que sea la matriz de identidad: "))
    matriz = []
    for i in range(indice):
        fila = []
        for x in range(indice):
            if i == x:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    for fila in matriz:
        print("\n------------------------")
        for elemento in fila:
            print(elemento, end= " | ")
    print("\n-----------------------")

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
