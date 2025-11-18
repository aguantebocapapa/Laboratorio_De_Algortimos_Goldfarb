productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
]

estudiantes = [
    {"nombre": "Ana", "edad": 21, "calificacion": 90},
    {"nombre": "Luis", "edad": 22, "calificacion": 95},
    {"nombre": "Marta", "edad": 20, "calificacion": 85}
]

libros = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
]

def Ejercicio_1(productos):
    for i in productos:
        print(f"Nombre: {i["nombre"]}")

def Ejercicio_2(productos):
    precio = 0
    for i in productos:
        precio += i["precio"]
    print(f"El precio total de todos los productos : {precio}")

def Ejercicio_3(productos):
    nuevo_producto = {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    productos.append(nuevo_producto)
    print(productos)

def Ejercicio_4(productos):
    productos[0]["precio"] = 1000
    print(f"{productos[0]}")

def Ejercicio_5(estudiantes):
    nota_alta = 0
    for i in estudiantes:
        if i["calificacion"] > nota_alta:
            nota_alta = i["calificacion"]
            estudiante = i
    print(estudiante)

def Ejercicio_6(estudiantes):
    lista_nombres = []
    for i in estudiantes:
        lista_nombres.append(i["nombre"])
    print(lista_nombres)

def Ejercicio_7(libros):
    libro_eliminado = libros.pop(1)
    libros.append(libro_eliminado)
    print(libros)

def Ejercicio_8(libros):
    for i in libros:
        i["disponible"] = True
    print(libros)

menu = int(input("Ingresa que ejercicio vas a revisar: "))
if menu == 1:   
    Ejercicio_1(productos)
elif menu == 2:
    Ejercicio_2(productos)
elif menu == 3:
    Ejercicio_3(productos)
elif menu == 4:
    Ejercicio_4(productos)
elif menu == 5:
    Ejercicio_5(estudiantes)
elif menu == 6:
    Ejercicio_6(estudiantes)
elif menu == 7:
    Ejercicio_7(libros)
elif menu == 8:
    Ejercicio_8(libros)
