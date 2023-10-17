from flask import Flask, render_template, request, redirect, flash, jsonify
from markupsafe import escape
import controladores.controlador_metodoP as controlador_metodoP
import math
from flask import url_for
from flask import make_response
import hashlib
import random

app = Flask(__name__)

#----APIS----

@app.route("/api_guardar_metodo_pago")

#----NORMAL----
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/login_empleado", methods=["GET", "POST"])
def login_empleado():
    return render_template('login_empleado.html')

@app.route("/registro_usuario")
def registro_usuario():
    return render_template('registro.html')

@app.route("/producto")
def producto():
    return render_template('producto.html')

@app.route("/carrito")
def carrito():
    return render_template('carrito.html')

@app.route("/categoria")
def  categoria():
    return render_template('categorias.html')

#metodo pago
@app.route("/agregar_metodo_pago")
def formulario_agregar_metodo_pago():
    return render_template("agregar_metodo_pago.html")

@app.route("/metodos_pago")
def metodos_pago():
    metodos_pago = controlador_metodoP.obtener_metodos_pago()
    return render_template("metodos_pago.html", metodos_pago=metodos_pago)

@app.route("/guardar_metodo_pago", methods=["POST"])
def guardar_metodo_pago():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    controlador_metodoP.insertar_metodo_pago(nombre, descripcion)
    return redirect("/metodos_pago")

@app.route("/eliminar_metodo_pago", methods=["POST"])
def eliminar_metodo_pago():
    controlador_metodoP.eliminar_metodo_pago(request.form["id"])
    return redirect("/metodos_pago")

@app.route("/formulario_editar_metodo_pago/<int:id>")
def editar_metodo_pago(id):
    metodo_pago = controlador_metodoP.obtener_metodo_pago_por_id(id)
    return render_template("editar_metodo_pago.html", metodo_pago=metodo_pago)

@app.route("/actualizar_metodo_pago", methods=["POST"])
def actualizar_metodo_pago():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    controlador_metodoP.actualizar_metodo_pago(nombre, descripcion, id)
    return redirect("/metodos_pago")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)