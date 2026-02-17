import sqlite3
import time, sys
from rich import print
from rich.panel import Panel
from rich.progress import track

def get_db():
    return sqlite3.connect("tabla_estudiantes_urp.db")

def mostrar_alumnos():
    conexion = get_db()
    cursor = conexion.cursor()

    print(
        Panel(
            "1.- Ver total de estudiantes\n"
            "2.- Estudiantes de género masculino\n"
            "3.- Estudiantes de género femenino\n"
            "4.- Estudiantes de otro género",
            title="BIENVENIDO"
        )
    )

    try:
        select = int(input("Introduzca una opción = "))
    except ValueError:
        print("Ingrese una opción válida!")
        return

    if select == 1:
        cursor.execute("SELECT * FROM Estudiantes_urp")
        data = cursor.fetchall()

        for _ in track(range(5), description="BUSCANDO DATOS..."):
            time.sleep(0.5)

        if not data:
            print("No hay alumnos.")
        else:
            for fila in data:
                print(fila)

    elif select == 2:
        cursor.execute("SELECT * FROM Estudiantes_urp WHERE Genero = ?", ("Hombre",))
        data = cursor.fetchall()

        for _ in track(range(5), description="BUSCANDO GENERO MASCULINO..."):
            time.sleep(0.5)

        for fila in data:
            print(fila)

    elif select == 3:
        cursor.execute("SELECT * FROM Estudiantes_urp WHERE Genero = ?", ("Mujer",))
        data = cursor.fetchall()

        for _ in track(range(5), description="BUSCANDO GENERO FEMENINO..."):
            time.sleep(0.5)

        for fila in data:
            print(fila)

    conexion.close()

    resp = input("¿Desea volver al menú? (si/no): ").lower()
    if resp != "si":
        sys.exit()

if __name__ == "__main__":
    while True:
        mostrar_alumnos()
