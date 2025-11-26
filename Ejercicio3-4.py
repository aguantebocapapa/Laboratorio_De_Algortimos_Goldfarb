import os
import mysql.connector
from mysql.connector import errorcode
import json

cursor = None
cnx = None

Tabla_Pokemon = []
Lista_Select = []
Lista_paraSelect = [1, 2, 3, 4, 5, 6]
Tabla_Especial = []
pedido_consulta = None
id_buscar = None
campo_buscar = None
valor_nuevo = None
Campos_Validos = ['nombre', 'numero_pokedex', 'tipo1', 'tipo2', 'categoria']

def Conectar_SQL():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'pokemon'
        )
        cursor = cnx.cursor(dictionary=True)
        print("Conexión establecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrectos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()

def Crear_Tablas():
    global Tabla_Pokemon, Tabla_Especial
    Tabla_Pokemon = InnerJoin(
        "select p.id_pokemon, p.nombre, p.numero_pokedex, t.nombre_tipo as tipo1, t2.nombre_tipo as tipo2 , c.nombre_categoria as categoria " \
        "from pokemones p " \
        "inner join tipos t on p.tipo1 = t.id_tipo " \
        "inner join tipos t2 on p.tipo2 = t2.id_tipo " \
        "inner join categorias c on p.categoria = c.id_categoria;"
    )

    if pedido_consulta != None:
        Tabla_Especial = InnerJoin(
            f"select {pedido_consulta} from pokemones;"
        )

# 1. Imprimir tabla ordenada
def Imprimir_Tabla(tabla, titulo):
    if not tabla:
        print(f"{titulo} N/a")
        return
    encabezados = list(tabla[0].keys())
    ancho_columnas = []
    for llave in encabezados:
        max_ancho = max(len(str(fila[llave])) for fila in tabla)
        max_ancho = max(max_ancho, len(llave))
        ancho_columnas.append(max_ancho)

    def Formatear_Fila(fila):
        return " | ".join(str(fila[llave]).ljust(ancho_columnas[i]) for i, llave in enumerate(encabezados))

    print(f"\n-- {titulo} --")
    print(Formatear_Fila({llave: llave for llave in encabezados}))
    print("-" * (sum(ancho_columnas) + 3 * (len(encabezados)-1)))
    for fila in tabla:
        print(Formatear_Fila(fila))

def Imprimir_Pokemon():
    Imprimir_Tabla(Tabla_Pokemon, "Pokemones")

def Generar_Json(nombre_archivo, tabla):
    ruta = f"archivos/{nombre_archivo}.json"
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(tabla, archivo, indent=4, ensure_ascii=False)
    print(f"El Reporte {nombre_archivo} fue creado con éxito")
    return ruta

# 2. Crear Json
def Json_Pokemon():
    Generar_Json("Pokemones", Tabla_Pokemon)

# 3. Crear Select
def Crear_Select():
    global pedido_consulta
    print("Escribe los datos que quieres de la consulta:")
    print("id_pokemon, nombre, numero_pokedex, tipo1, tipo2, categoria")
    print("Ejemplo: select id_pokemon, nombre, numero_pokedex")
    pedido_consulta = str(input("select "))
    Crear_Tablas()

# 4. Actualizar valores
def Actualizar_Valor(id, valorguardar):
    actualizacion = f"update Pokemones set {campo_buscar} = %s where id_pokemon = %s"
    valores = (valorguardar, id)
    cursor.execute(actualizacion, valores)
    cnx.commit()

def Pedir_Valores_Actualizar():
    global id_buscar, campo_buscar, valor_nuevo
    id_buscar = int(input("Ingrese el id del pokemon a cambiar: "))
    while True:
        campo_buscar = str(input("Ingrese el campo que deseas cambiar (nombre, numero_pokedex, tipo1, tipo2, categoria): "))      
        if campo_buscar not in Campos_Validos:
            print("Ingrese un campo coherente")
        else:
            break
    valor_nuevo = input("Ingrese el nuevo valor: ")

# 5. Insert a elección
def Crear_Insert():
    while True:
        try:
            submenu = int(input(
                "Ingrese que tabla quiere hacer un insert:"
                "\n1. Nuevo Tipo"
                "\n2. Nueva Categoria"
                "\n3. Nuevo Pokemon"
                "\n0. Cerrar"
                ))
            if submenu == 1:
                while True:
                    try:
                        nombre_tipo = str(input("Ingrese el nuevo tipo: "))
                        break 
                    except ValueError:
                        print("Ingrese texto")
                sql = "insert into tipos (nombre_tipo) values (%s);"
                cursor.execute(sql, (nombre_tipo))
                Crear_Tablas()
            elif submenu == 2:
                while True:
                    try:
                        nombre_categoria = str(input("Ingrese la nueva categoria: "))
                        break 
                    except ValueError:
                        print("Ingrese texto")
                sql = "insert into categorias (nombre_categoria) values (%s);"
                cursor.execute(sql, (nombre_categoria))
                Crear_Tablas()
            elif submenu == 3:
                while True:
                    try:
                        nombre = str(input("Ingrese el nuevo tipo: "))
                        numero_pokedex = int(input("Ingrese el número de pokedex: "))
                        tipo1 = int(input("Ingrese su tipo 1: "))
                        tipo2 = int(input("Ingrese su tipo 2: "))
                        categoria = int(input("Ingrese su categoria: "))
                        break 
                    except ValueError:
                        print("Ingrese valores correctos")
                sql = "insert into pokemones (nombre, numero_pokedex, tipo1, tipo2, categoria) values (%s, %s, %s, %s, %s);"
                cursor.execute(sql,(nombre, numero_pokedex, tipo1, tipo2, categoria))
                Crear_Tablas()
            elif submenu == 0:
                break
            else:
                print("Ingrese un valor válido")
        except ValueError:
            print("Error")

def main ():
    Conectar_SQL()
    Crear_Tablas()
    while True:
        menu = int(input(
            "Trabajo 3.4 Base de Datos bla bla bla"
            "\n1. Imprimir la tabla de pokemones"
            "\n2. Crear un json de la tabla de pokemones"
            "\n3. Hacer tu propio select"
            "\n4. Actualizar un valor"
            "\n5. Hacer un insert nuevo"
            "\n0. Cerrar"
            "\n-> "
        ))
        if menu == 1:
            Imprimir_Pokemon()
        elif menu == 2:
            while True:
                try:
                    Json_Pokemon()
                    break
                except FileNotFoundError:
                            os.makedirs("archivos")
        elif menu == 3:
            while True:
                try:
                    Crear_Select()
                    break
                except mysql.connector.errors.ProgrammingError:
                    print("Ingrese los campos correctamente.")
        elif menu == 4:
            while True:
                try:
                    Pedir_Valores_Actualizar()
                    Actualizar_Valor(id_buscar, valor_nuevo)
                    break
                except mysql.connector.errors.ProgrammingError:
                    print("Ingrese los datos correctamente.")
        elif menu == 5:
            Crear_Insert()
        elif menu == 0:
            print("Cerrando Programa")
            break

main()
