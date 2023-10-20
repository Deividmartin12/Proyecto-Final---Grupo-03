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


@app.route("/metodos_pago")
def metodos_pago():
    return render_template("metodos_pago.html")

@app.route("/control_admin", methods=["GET", "POST"])
def control_admin():
    return render_template("maestra_admin.html")

@app.route("/admin_det_ped")
def admin_det_ped():
    return render_template("admin_det_ped.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)