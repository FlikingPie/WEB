from flask import Flask, render_template, request

#Flask --> crea la app web
#render_template -->permite usar archivos html
#request--> sirve para recibir datos enviados desde formularios html

app = Flask(__name__) # Crear la applicación (App) __name__ le dice a Flask dónde está el archivo principal


#Esta funcion se encarga de mostrar el formulario html
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"]) # /enviar es la ruta que conecta python y html : <form method="POST" action="/enviar" onsubmit="return validar()">
#methods indica QUÉ TIPO de solicitud acepta esa ruta.
#| Método   | Para qué se usa  |
#| -------- | ---------------- |
#| **GET**  | Pedir una página |
#| **POST** | Enviar datos     | NUESTRO CASO, es decir, solo acepta
#| PUT      | Actualizar datos |
#| DELETE   | Borrar datos     |

def enviar():
    nombre = request.form.get("nombre") # del formulario, recibe "nombre"
    dni = request.form.get("dni")
    pais = request.form.get("pais")
    educacion = request.form.getlist("educacion") # de la lista, recibe "educacion"
    comentario = request.form.get("comentarios")

    with open("Formulario.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre},{dni},{pais},{' | '.join(educacion)},{comentario}\n")

    return "Datos guardados correctamente"

if __name__ == "__main__":
    app.run(debug=True) #permite ver los cambios (debug=True)
