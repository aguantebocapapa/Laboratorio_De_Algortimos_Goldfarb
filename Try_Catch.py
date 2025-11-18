def ejercicio1():
    saldo = 1000
    while 0 == 0:
        print("-- Oppenbanco TroleaJuanmer --")
        print("Usuario: UU093JS2")
        print(f"Saldo: {saldo}")
        print("Ingrese que desea hacer: ")
        print("1) Retirar saldo.")
        print("2) Ingresar saldo.")
        print("3) Cerrar Programa.")
        menu = int(input("--> "))
        if menu == 1:
            print(f"Saldo disponible: {saldo}")
            try:
                retirar = float(input("Ingrese cuanto saldo desea retirar: "))
                if retirar > saldo:
                    print(f"\n \nError 302. Solo retire un número menor a su saldo. \n")
                else:
                    print(f"\n \nOperación realizada con exito \n")
                    saldo = saldo - retirar
            except ValueError:
                print("")
                print(f"\n \nError 303. No puede retirar texto. \n")
        elif menu == 2:
            print(f"Saldo disponible: {saldo}")
            try:
                ingresar = float(input("Ingrese cuanto saldo desea ingresar: "))
                saldo = saldo + ingresar
                print(f"\n \n \n")
            except ValueError:
                print(f"\n \nError 304. No puede ingresar texto para sumar su saldo. \n")
        elif menu == 3:
            print("Cerrando programa...")
            break
        else:
            print(f"\n \nError 301. Esa opción no se encuentra disponible, intente otra vez. \n")

def ejercicio2 ():
    try:
        print("Calculadora de IMC ")
        altura = float(input("ingrese su altura en metros: "))
        peso = float(input("ingrese su peso en kg: "))
        indice = peso / (altura * altura)
        indice = indice * 10
        indice = indice // 1
        indice = indice // 10
        print(f"Su indice de masa corporal es: {indice}  ")
        if indice < 18.5:
            print("Usted tiene un bajo peso.")
        elif indice < 24.9:
            print("Usted tiene un peso saludable.")
        elif indice < 29.9:
            print("Usted tiene sobrepeso.")
        elif indice < 34.9:
            print("Usted tiene obesidad tipo-1")
        elif indice < 39.9:
            print("Usted tiene obesidad tipo-2")
        else:
            print("Usted tiene obesidad tipo-3")
    except TypeError:
        print("No puede calcular texto, chistocito.")

def ejercicio3():
    import random
    vocales = ["a", "e", "i", "o", "u"]
    while frase != "agusfortnite2008":
        frase = str(input("Ingrese una frase: "))
        frase_final = ""
        for letra in frase:
            if letra in vocales:
                letra = random.choice(vocales)
            frase_final = frase_final + letra


def ejercicio4():
    try:
        frase = str(input("Ingrese una frase: "))
        palabras = frase.split()
        for letra in palabras:
            print(letra[::-1])
    except ValueError:
        print("Osea ingrese una frase con texto, no con números.")

def ejercicio5():
    nombres = []
    while 0 == 0:
        print("-- Oppenbase de datos TroleaJuanmer --")
        print("Ingrese que desea hacer: ")
        print("1) Agregar nombre.")
        print("2) Revisar nombre.")
        print("3) Cerrar Programa.")
        menu = int(input("--> "))
        if menu == 1:
            try:
                nombre = str(input("Ingrese que nombre desea agregar: "))
                nombres.append(nombre)
                print(f"\n \n \n")
            except ValueError:
                print("")
                print(f"\n \nIngrese un nombre, no números. \n")
        elif menu == 2:
            try:
                buscar = int(input("Ingrese el número de índice del nombre que desea ver: "))
                print(f"\n \n{nombres[buscar]} \n")
            except (ValueError, IndexError):
                print(f"\n \nPor favor, no ingrese un número de índice mayor al que esta disponible y no ingrese cosas que no sean números.. \n")
        elif menu == 3:
            print("Cerrando programa...")
            break
        else:
            print(f"\n \nEsa opción no se encuentra disponible, intente otra vez. \n")

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
