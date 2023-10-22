from flask import Flask, render_template, request, redirect, flash, jsonify
from markupsafe import escape
import math
from flask import url_for
from flask import make_response
import hashlib
import random

import controlador_mascota
import controlador_producto

app = Flask(__name__)

#----APIS----

#soicaballero

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

#####################     MASCOTA     ############################
@app.route("/mascotas")
def formulario_mascotas():
    mascotas = controlador_mascota.obtener_mascotas()
    return render_template("mascotas.html", mascotas=mascotas)

@app.route("/agregar_mascota")
def formulario_registrar_mascota():
    return render_template('registrar_mascota.html')

@app.route("/insertar_mascota", methods=["POST"])
def metodo_insertar_mascota():
    nombre = request.form["nombre"]
    controlador_mascota.insertar_mascota(nombre)
    return redirect("/mascotas")

@app.route("/editar_mascota/<int:id>")
def formulario_editar_mascota(id):
    mascota = controlador_mascota.obtener_mascota_por_id(id)
    return render_template("editar_mascota.html",mascota=mascota)

@app.route("/actualizar_mascota",methods=["POST"])
def metodo_actualizar_mascota():
    mascota_id = request.form["id"]
    nombre = request.form["nombre"]
    controlador_mascota.actualizar_mascota(nombre,mascota_id)
    return redirect("/mascotas")

@app.route("/eliminar_mascota",methods=["POST"])
def metodo_eliminar_mascota():
    mascota_id = request.form["id"]
    controlador_mascota.eliminar_mascota(mascota_id)
    return redirect("/mascotas")
#####################     MASCOTA     ############################


#####################     PRODUCTO     ############################
@app.route("/productos")
def formulario_productos():
    productos = controlador_producto.obtener_productos_formateado()
    return render_template("productos.html", productos=productos)

@app.route("/agregar_producto")
def formulario_registrar_producto():
    categorias = controlador_producto.obtener_categorias()
    mascotas = controlador_mascota.obtener_mascotas()
    return render_template('registrar_producto.html', categorias=categorias, mascotas=mascotas)

@app.route("/insertar_producto", methods=["POST"])
def metodo_insertar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    if request.form["estado"]=='SI':
        estado = True
    else:
        estado = False
    categoria_id = request.form["categoria_id"]
    mascota_id = request.form["mascota_id"]
    link_imagen = request.form["imagen"]
    controlador_producto.insertar_producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen)
    return redirect("/productos")

@app.route("/editar_producto/<int:id>")
def formulario_editar_producto(id):
    producto = controlador_producto.obtener_producto_por_id(id)
    categorias = controlador_producto.obtener_categorias()
    mascotas = controlador_mascota.obtener_mascotas()
    return render_template("editar_producto.html",producto=producto, categorias=categorias, mascotas=mascotas)

@app.route("/actualizar_producto",methods=["POST"])
def metodo_actualizar_producto():
    producto_id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    if request.form["estado"]=='SI':
        estado = True
    else:
        estado = False
    categoria_id = request.form["categoria_id"]
    mascota_id = request.form["mascota_id"]
    link_imagen = request.form["imagen"]
    controlador_producto.actualizar_producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen,producto_id)
    return redirect("/productos")

@app.route("/eliminar_producto",methods=["POST"])
def metodo_eliminar_producto():
    producto_id = request.form["id"]
    controlador_producto.eliminar_producto(producto_id)
    return redirect("/productos")
#####################     PRODUCTO     ############################


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)