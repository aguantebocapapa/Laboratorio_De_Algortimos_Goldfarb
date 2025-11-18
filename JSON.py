import json

def Crear_JSON(nombre_archivo, diccionario):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(diccionario, archivo, indent=4, ensure_ascii=False)

#Ejercicio 1
informacion_personal = {
    "nombre": "Juan",
    "edad": 16,
    "ciudad": "Ciudad Incorrecta",
    "profesion": "Profesión Incorrecta"
}
nombre_archivo = "Ejercicio 1.json"
diccionario = informacion_personal
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 2
informacion_personal["ciudad"] = "San Martín"
informacion_personal["profesion"] = "Músico"
informacion_personal["telefono"] = 112233445566
informacion_personal["email"] = "juan123@gmail.com"
nombre_archivo = "Ejercicio 2.json"
diccionario = informacion_personal
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 3
calificaciones = {
    "matematica": 6,
    "lengua": 8,
    "ciencias": 5
}
print(calificaciones.get("matematica"))
nombre_archivo = "Ejercicio 3.json"
diccionario = calificaciones
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 4
promedio = calificaciones.get("matematica") + calificaciones.get("lengua") + calificaciones.get("ciencias")
promedio = promedio / 3
print(promedio)
nombre_archivo = "Ejercicio 4.json"
diccionario = calificaciones
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 5
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Paraguay": "Asunción",
    "Uruguay": "Montevideo"
}

pais_ingresado = input("Ingresá un país: ")
print("La capital es:", paises.get(pais_ingresado, "País no encontrado"))
nombre_archivo = "Ejercicio 5.json"
diccionario = paises
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 6
precios = {
    "pan": 800,
    "leche": 1200,
    "huevo": 1500,
    "queso": 2500
}

def costo_total(producto, cantidad):
    if producto in precios:
        return precios[producto] * cantidad
    else:
        return "Producto no encontrado"

print(costo_total("pan", 3))
nombre_archivo = "Ejercicio 6.json"
diccionario = precios
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 7
del informacion_personal["telefono"]
print(informacion_personal)
nombre_archivo = "Ejercicio 7.json"
diccionario = informacion_personal
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 8
def existe_clave(diccionario, clave):
    return clave in diccionario

print(existe_clave(informacion_personal, "email"))
print(existe_clave(informacion_personal, "telefono"))
nombre_archivo = "Ejercicio 8.json"
diccionario = informacion_personal
Crear_JSON(nombre_archivo, diccionario)

#Ejercicio 9
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 9, "d": 4, "e": 5}

dic1.update(dic2)
print(dic1)
nombre_archivo = "Ejercicio 9.json"
diccionario = dic1
Crear_JSON(nombre_archivo, diccionario)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
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
def Ejercicio_3(productos):
    nuevo_producto = {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
    productos.append(nuevo_producto)
    print(productos)
    return productos

def Ejercicio_4(productos):
    productos[0]["precio"] = 1000
    print(f"{productos[0]}")
    return productos

nombre_archivo = "Productos.json"
diccionario = productos
Crear_JSON(nombre_archivo, diccionario)
