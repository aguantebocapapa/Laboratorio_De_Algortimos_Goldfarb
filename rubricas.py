

import mysql.connector
from mysql.connector import errorcode



cursor = None
cnx = None


Rubricas = []
Criterios = []
Tabla_Completa = []


def Conectar_SQL():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'escuela'
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


def Consultas(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()


def Actualizar_Tablas():
    global Rubricas, Criterios, Tabla_Completa
    Rubricas = Consultas('select * from Rubricas')
    Criterios = Consultas('select * from Criterios')
    Tabla_Completa = Consultas('select R.id_rubrica, R.nombre_rubrica, C.id_criterio, C.nombre_criterio, C.nota, C.nota_maxima from Rubricas R inner join Criterios C on R.id_rubrica = C.rubrica')
def Inserts_Rubricas():
    while True:
        try:
            nombre_rubrica = str(input("Ingrese la Rúbrica a calificar: "))
            break
        except ValueError:
            print("Error, ingrese solamente texto")
    sql = "insert into Rubricas (nombre_rubrica) values (%s);"
    cursor.execute(sql, (nombre_rubrica,))
    cnx.commit()
    Actualizar_Tablas()

def Inserts_Criterios():
    while True:
        try:
            nombre_criterio = str(input("Ingrese el Criterio a evaluar: "))
            rubrica = int(input("Ingrese el id de la Rúbrica que va a agregar el criterio: "))
            nota_maxima = int(input("Ingrese la nota máxima para este criterio: "))
            while True:
                nota = int(input("Ingrese la nota obtenida en este criterio: "))
                if nota > nota_maxima:
                    print("La nota debe ser menor o igual a la nota_maxima")
                else:
                    break
            break
        except ValueError:
            print("Error, ingrese valores válidos")
    sql = "insert into Criterios (nombre_criterio, nota, nota_maxima, rubrica) values (%s, %s, %s, %s)"
    cursor.execute(sql,(nombre_criterio, nota, nota_maxima, rubrica,))
    cnx.commit()
    Actualizar_Tablas()

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

def Buscar_Rubrica():
    while True:
        try:
            buscar_rubrica = int(input("Ingrese el id de la rúbrica buscada: ))
            break
        except ValueError:
            print("Error")
    Tabla_Nueva = [fila for fila in Tabla_Completa if fila["id_rubrica"] == buscar_rubrica]
    Imprimir_Tabla(Tabla_Nueva, "Rubrica buscada con sus Criterios)

def Main():
    Conectar_SQL()
    Actualizar_Tablas()
    print("Sistema de la OppenEscuela")
    while True:
        try:
            menu = int(input('''
                Ingrese que desea hacer:
                1. Crear una Rubrica
                2. Crear un Criterio
                3. Imprimir Rubricas
                4. Buscar Rúbrica
                0. Cerrar programa
                -> '''))
            if menu == 1:
                Inserts_Rubricas()
            elif menu == 2:
                if Rubricas[0] == None:
                    print("Primero debes crear una Rúbrica")
                else:
                    Inserts_Criterios()
            elif menu == 3:
                if Rubricas[0] == None:
                    print("Primero debes crear una Rúbrica")
                else:
                    Imprimir_Tabla(Rubricas, "Rubricas")
            elif menu == 4:
                Buscar_Rubrica()
            elif menu == 0:
                break
            else:
                print("Ingrese un número válido")
        except ValueError:
            print("Ingrese solo números")
Main()
