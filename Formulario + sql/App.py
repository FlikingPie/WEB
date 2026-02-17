from flask import Flask, render_template, request
import sqlite3,os

"NO se puede utilizar RICH Y FLASK EN UN MISMO ARCHIVO"

#print(os.mkdir("static"))
#print(os.mkdir("templates"))



app = Flask(__name__)

def get_db():
    return sqlite3.connect("tabla_estudiantes_urp.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    global cursor
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    genero = request.form.get("genero")
    carrera = request.form.get("carrera")
    cursos = request.form.getlist("curso")

    cursos_str = ", ".join(cursos)

    conexion = get_db()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO Estudiantes_urp
        (Nombre, Apellido, Genero, Carrera, Favorito)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellido, genero, carrera, cursos_str))

    conexion.commit()
    conexion.close()

    return "Datos guardados correctamente ✅"


if __name__ == "__main__":
    app.run(debug=True)

