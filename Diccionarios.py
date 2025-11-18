#Ejercicio 1
informacion_personal = {
    "nombre": "Juan",
    "edad": 16,
    "ciudad": "Ciudad Incorrecta",
    "profesion": "Profesión Incorrecta"
}


#Ejercicio 2
informacion_personal["ciudad"] = "San Martín"
informacion_personal["profesion"] = "Músico"
informacion_personal["telefono"] = 112233445566
informacion_personal["email"] = "juan123@gmail.com"


#Ejercicio 3
calificaciones = {
    "matematica": 6,
    "lengua": 8,
    "ciencias": 5
}
print(calificaciones.get("matematica"))


#Ejercicio 4
promedio = calificaciones.get("matematica") + calificaciones.get("lengua") + calificaciones.get("ciencias")
promedio = promedio / 3
print(promedio)


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


#Ejercicio 7
del informacion_personal["telefono"]
print(informacion_personal)


#Ejercicio 8
def existe_clave(diccionario, clave):
    return clave in diccionario

print(existe_clave(informacion_personal, "email"))
print(existe_clave(informacion_personal, "telefono"))


#Ejercicio 9
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 9, "d": 4, "e": 5}

dic1.update(dic2)
print(dic1)
