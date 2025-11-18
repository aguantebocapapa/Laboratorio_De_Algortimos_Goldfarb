def ejercicio1():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    try:
        resultado = num1 / num2
        print(f"El resultado de la división entre {num1} y {num2} es {resultado}")
    except ZeroDivisionError:
        print("Por favor no intente dividir por cero.")

def ejercicio2():
    try:
        edad = int(input("Por favor ingrese su edad: "))
        print(f"{edad} años de aportes quizas.")
    except ValueError:
        print("De verdad tenés esa edad?")
        print("Pone un número entero por favor.")

def ejercicio3():
    lista = ["Ana", "Pedro", "Sofía"]
    try:
        indice = int(input("Ingrese un número de indice para leer un nombre de la lista: "))
        print(lista[indice])
    except IndexError:
        print("Osea, la lista no es muy grande viste, pone un número entre 0 y 2 no seas bruto.")

def ejercicio4():
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        suma = num1 + num2
        print(f"El resultado entre la suma entre {num1} y {num2} es {suma}")
    except (ValueError, TypeError):
        print("Por favor debe sumar 2 NÚMEROS ENTEROS.")

def ejercicio5():
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        resultado = num1 / num2
        print(f"El resultado entre la división entre {num1} y {num2} es {resultado}")
    except (ZeroDivisionError, ValueError, TypeError):
        print("Osea intente que sean 2 números enteros para dividir,")
    finally:
        print("Fin del programa de cálculo.")

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
    elif ejercicio == 0:
        print("Finalizando programa...")
        break
