def ejercicio1():
    lista = ["manzana", "banana", "cereza"]
    print(lista)
    print(lista[1])
    return lista

def ejercicio2():
    lista = ["perro", "gato", "elefante"]
    lista.append("jirafa")
    gato = "gato"
    lista.remove(gato)
    print(lista)
    return lista

def ejercicio3():
    ValorTotal = 0
    lista1 = [5, 1, 8]
    lista2 = [3, 9, 2]
    for i in lista1:
        ValorTotal = ValorTotal + i
    for i in lista2:
        ValorTotal = ValorTotal + i
    print(ValorTotal)
    return ValorTotal

def ejercicio4():
    lista1 = [5, 1, 8]
    lista2 = [3, 9, 2]
    lista_combinada = []
    for i in lista1:
        lista_combinada.append(i)
    for i in lista2:
        lista_combinada.append(i)
    print(lista_combinada)

def ejercicio5():
    import random
    lista = ["Pepe", "Juana", "Santiago", "Ignacio", "Federico", "Gabriel", "Sofia"]
    notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Lista_Alumno = []
    agregar = random.choice(lista)
    Lista_Alumno.append(agregar)
    agregar = random.choice(notas)
    Lista_Alumno.append(agregar)
    return Lista_Alumno

def ejercicio6():
    Alumno1 = ejercicio5()
    Alumno2 = ejercicio5()
    Alumno3 = ejercicio5()
    Notas_Curso = []
    Notas_Curso.append(Alumno1[1])
    Notas_Curso.append(Alumno2[1])
    Notas_Curso.append(Alumno3[1])
    promedio = 0
    for i in Notas_Curso:
        promedio = promedio + i
    print(f"{Alumno1}, {Alumno2}, {Alumno3}")
    return promedio

def ejercicio7():
    while 0 == 0:
        print("--- Menú promedios escuela ---")
        menu = int(input("Seleccione una opción: \n1 - Generar cursos nuevos (3) \n2 - Cerrar programa \n"))
        if menu == 1:
            Curso1 = ejercicio6()
            Curso2 = ejercicio6()
            Curso3 = ejercicio6()
            promediosEscuela = Curso1 + Curso2 + Curso3
            promediosEscuela = promediosEscuela/3
            if promediosEscuela >= 6:
                print("La escuela tiene buen promedio.")
            else:
                print("La escuela tiene mal promedio.")
        elif menu == 2:
            print("Cerrando programa...")
            break

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
    elif ejercicio == 5:
        ejercicio5()
    elif ejercicio == 6:
        ejercicio6()
    elif ejercicio == 7:
        ejercicio7()
    elif ejercicio == 0:
        print("Finalizando programa...")
        break
    else:
        print("Debe ingresar un ejercicio del 1 al 7")
