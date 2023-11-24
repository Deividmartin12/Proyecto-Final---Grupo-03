from flask import Flask, render_template, request, redirect, flash, jsonify,json,url_for,make_response
from markupsafe import escape
import controladores.controlador_metodoP as controlador_metodoP
import math
import hashlib
import random
import controladores.controlador_categorias as controlador_categorias
import controladores.controlador_mascota as controlador_mascota
import controladores.controlador_producto as controlador_producto
import controladores.controlador_usuario as controlador_usuario
import controladores.controlador_pedidos as controlador_pedido
import controladores.controlador_cliente as controlador_cliente
import controladores.controlador_comprobantes as controlador_comprobante
import controladores.controlador_metodoP as controlador_metodos_pago

import clases.metodopago as clase_metodo_pago
import clases.usuario as clase_usuario
import clases.producto as clase_producto
import clases.mascota as clase_mascota
import clases.categoria as clase_categoria
import clases.cliente as clase_cliente
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)

##### SEGURIDAD - INICIO ###################################

def authenticate(username, password):
    usuario = controlador_usuario.obtener_usuario_por_username(username)

    if usuario and (usuario[8] == password):
        objUsuario = clase_usuario.Usuario(usuario[0], usuario[1], usuario[2], usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11])
        return objUsuario


def identity(payload):
    user_id = payload['identity']

    usuario = controlador_usuario.obtener_usuario_por_id(user_id)
    objUsuario = clase_usuario.Usuario(usuario[0], usuario[1], usuario[2], usuario[3],usuario[4],usuario[5],usuario[6],usuario[7],usuario[8],usuario[9],usuario[10],usuario[11])

    if usuario:
        return objUsuario


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)
##### SEGURIDAD - FIN ######################################


'''@app.route("/login")
def login():
    return render_template("login_empleado.html")'''

@app.route("/login",methods=["GET", "POST"])
def login():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")

        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            return render_template("index_admin.html",esSesionIniciada=True)

        elif token == usuario[9] and usuario[10] == 2 and usuario[11]==True:
            return render_template("usuario.html",esSesionIniciada=True,usuario=usuario)

        return render_template("login.html")
    except:
        return render_template("login.html")

############### LOGIN ###############

@app.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    resp.set_cookie('token', '', expires=0)
    return resp

@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    username = request.form["username"]
    password = request.form["password"]
    usuario = controlador_usuario.obtener_usuario_por_username(username)

    if usuario == None:
        return render_template("login.html")
    else:
        # Encriptar password ingresado por usuario
        h = hashlib.new('sha256')
        h.update(bytes(password,encoding='utf-8'))
        encpassword = h.hexdigest()
        if encpassword == usuario[8]:
            # Obteniendo token
            t = hashlib.new('sha256')
            entale = random.randint(1,1024)
            strEntale = str(entale)
            t.update(bytes(strEntale,encoding='utf-8'))
            token = t.hexdigest()
            # Acá se debe controlar con cookies
            if usuario[10] == 1:
                resp = make_response(redirect("/index_admin"))
                resp.set_cookie('username', username)
                resp.set_cookie('token', token)
                controlador_usuario.actualizar_token(username, token)
                return resp
            elif usuario[10] == 2:
                resp = make_response(redirect("/usuario"))
                resp.set_cookie('username', username)
                resp.set_cookie('token', token)
                controlador_usuario.actualizar_token(username, token)
                return resp

        return render_template("login.html")




############### FIN LOGIN ###############


############# APIS #########################################
#########Comprobantes########

@app.route("/api_comprobantes", methods=["GET"])
@jwt_required()
def api_obtener_comprobantes():
    respuesta = dict()
    listadiccs = []
    comprobantes = controlador_comprobante.obtener_comprobantes()
    for comprobante in comprobantes:
        objComprobante = clase_comprobante.Comprobante(comprobante[0], comprobante[1], comprobante[2], comprobante[3], comprobante[4])
        listadiccs.append(objComprobante.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de comprobantes correcto"
    return jsonify(respuesta)


@app.route("/api_agregar_comprobante", methods=["POST"])
@jwt_required()
def api_guardar_comprobante():
    respuesta = dict()
    listadiccs = []

    fechaE = request.json["fechaE"]
    monto = request.json["monto"]
    tipoC = request.json["tipoC"]
    pedidoId = request.json["pedidoId"]
    metodoPId = request.json["metodoPId"]
    controlador_comprobantes.insertar_comprobante(fechaE, monto, tipoC, pedidoId, metodoPId)
    respuesta["data"] = listadiccs
    respuesta["code"] = 3
    respuesta["message"] = "Agregado correcto"
    return jsonify(respuesta)

@app.route("/api_editar_comprobante", methods=["POST"])
@jwt_required()
def api_actualizar_comprobante():
    respuesta = dict()
    listadiccs = []
    id = request.json["id"]
    fechaE = request.json["fechaE"]
    monto = request.json["monto"]
    tipoC = request.json["tipoC"]
    pedidoId = request.json["pedidoId"]
    metodoPId = request.json["metodoPId"]
    controlador_comprobantes.actualizar_comprobante(id, fechaE, monto, tipoC, pedidoId, metodoPId)
    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizado correcto"
    return jsonify(respuesta)

#########MetodosPago########
@app.route("/api_metodos_pago", methods=["GET"])
@jwt_required()
def api_obtener_metodos_pago():
    respuesta = dict()
    listadiccs = []
    metodos_pago = controlador_metodos_pago.obtener_metodos_pago()
    for metodo_pago in metodos_pago:
        objMetodoPago = clase_metodo_pago.MetodoPago(metodo_pago[0], metodo_pago[1], metodo_pago[2], metodo_pago[3])
        listadiccs.append(objMetodoPago.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de métodos de pago correcto"
    return jsonify(respuesta)


@app.route("/api_actualizar_metodo_pago", methods=["POST"])
@jwt_required()
def api_actualizar_metodo_pago():
    respuesta = dict()
    listadiccs = []
    id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_metodos_pago.actualizar_metodo_pago(nombre, descripcion, id)
    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizado correcto"
    return jsonify(respuesta)

@app.route("/api_guardar_metodo_pago", methods=["POST"])
@jwt_required()
def api_guardar_metodo_pago():
    respuesta = dict()
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_metodos_pago.insertar_metodo_pago(nombre, descripcion)
    respuesta["code"] = 3
    respuesta["message"] = "Guardado correcto"
    return jsonify(respuesta)


#########Categorias########
@app.route("/api_guardar_categoria", methods=["POST"])
@jwt_required()
def api_guardar_categoria():
    respuesta = dict()
    listadiccs = []
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_categorias.insertar_categoria(nombre, descripcion)
    respuesta["data"] = listadiccs
    respuesta["code"] = 3
    respuesta["message"] = "Guardado correcto"
    return jsonify(respuesta)

@app.route("/api_actualizar_categoria", methods=["POST"])
@jwt_required()
def api_actualizar_categoria():
    respuesta = dict()
    listadiccs = []
    id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_categorias.actualizar_categoria(nombre, descripcion, id)
    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizado correcto"
    return jsonify(respuesta)

@app.route("/api_categorias", methods=["GET"])
@jwt_required()
def api_obtener_categorias():
    respuesta = dict()
    listadiccs = []
    categorias = controlador_categorias.obtener_categorias()
    for categoria in categorias:
        objCategoria = clase_categoria.Categoria(categoria[0], categoria[1], categoria[2], categoria[3])
        listadiccs.append(objCategoria.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de categorías correcto"
    return jsonify(respuesta)


#########Mascotas########

@app.route("/api_mascotas", methods=["GET"])
@jwt_required()
def api_obtener_mascotas():
    respuesta = dict()
    listadiccs = []
    mascotas = controlador_mascota.obtener_mascotas()
    for mascota in mascotas:
        objMascota = clase_mascota.Mascota(mascota[0],mascota[1])
        listadiccs.append(objMascota.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de datos correcto"
    return jsonify(respuesta)
@app.route("/api_insertar_mascota", methods=["POST"])
@jwt_required()
def api_insertar_mascota():
    respuesta = dict()
    listadiccs = []
    nombre = request.json["nombre"]
    controlador_mascota.insertar_mascota(nombre)
    respuesta["data"] = listadiccs
    respuesta["code"] = 3
    respuesta["message"] = "Guardado correcto"
    return jsonify(respuesta)
@app.route("/api_actualizar_mascota", methods=["POST"])

@jwt_required()
def api_actualizar_mascota():
    respuesta = dict()
    listadiccs = []
    mascota_id = request.json["id"]
    nombre = request.json["nombre"]
    controlador_mascota.actualizar_mascota(nombre, mascota_id)
    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizado correcto"
    return jsonify(respuesta)

#########Productos########

@app.route("/api_productos", methods=["GET"])
@jwt_required()
def api_productos():
    respuesta = dict()
    listadiccs = []
    productos = controlador_producto.obtener_productos()
    for producto in productos:
        objProducto = clase_producto.Producto(producto[0],producto[1],producto[2],producto[3],producto[4],producto[5],producto[6],producto[7],producto[8])
        listadiccs.append(objProducto.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de datos correcto"
    return jsonify(respuesta)

@app.route("/api_actualizar_producto", methods=["POST"])
@jwt_required()
def api_actualizar_producto():
    respuesta = dict()
    listadiccs = []
    producto_id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    stock = request.json["stock"]
    estado = request.json["estado"]
    categoria_id = request.json["categoria_id"]
    mascota_id = request.json["mascota_id"]
    link_imagen = request.json["imagen"]
    controlador_producto.actualizar_producto(nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, link_imagen, producto_id)
    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizadion Correcta"
    return jsonify(respuesta)

@app.route("/api_insertar_producto", methods=["POST"])
@jwt_required()
def api_insertar_producto():
    respuesta = dict()
    listadiccs = []
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    stock = request.json["stock"]
    estado = request.json["estado"]
    categoria_id = request.json["categoria_id"]
    mascota_id = request.json["mascota_id"]
    link_imagen = request.json["imagen"]
    controlador_producto.insertar_producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen)
    respuesta["data"] = listadiccs
    respuesta["code"] = 3
    respuesta["message"] = "Guardado Correcto"
    return jsonify(respuesta)

#########Usuarios########
@app.route("/api_guardar_usuario", methods=["POST"])
@jwt_required()
def api_guardar_usuario():
    respuesta = dict()
    listadiccs = []
    nombres = request.json["nombres"]
    apellidos = request.json["apellidos"]
    email = request.json["email"]
    telefono = request.json["telefono"]
    direccion = request.json["direccion"]
    dni = request.json["dni"]
    username = request.json["username"]
    password = request.json["password"]
    tipo_usuario = request.json["tipo_usuario"]

    controlador_usuarios.registrar_usuario_cliente(
        nombres=nombres,
        apellidos=apellidos,
        email=email,
        telefono=telefono,
        direccion=direccion,
        dni=dni,
        username=username,
        password=password,
        tipo_usuario=tipo_usuario
    )

    respuesta["data"] = listadiccs
    respuesta["code"] = 3
    respuesta["message"] = "Guardado Correcto"
    return jsonify(respuesta)

@app.route("/api_actualizar_usuario", methods=["POST"])
@jwt_required()
def api_actualizar_usuario():
    respuesta = dict()
    listadiccs = []
    id = request.json["id"]
    nombres = request.json["nombres"]
    apellidos = request.json["apellidos"]
    email = request.json["email"]
    telefono = request.json["telefono"]
    direccion = request.json["direccion"]
    dni = request.json["dni"]
    username = request.json["username"]
    password = request.json["password"]
    tipo_usuario = request.json["tipo_usuario"]
    estado = request.json["estado"]

    controlador_usuarios.actualizar_usuario_cliente(
        nombres=nombres,
        apellidos=apellidos,
        email=email,
        telefono=telefono,
        direccion=direccion,
        dni=dni,
        username=username,
        password=password,
        tipo_usuario=tipo_usuario,
        estado=estado,
        id=id
    )

    respuesta["data"] = listadiccs
    respuesta["code"] = 2
    respuesta["message"] = "Actualizadion Correcta"
    return jsonify(respuesta)

@app.route("/api_usuarios", methods=["GET"])
@jwt_required()
def api_obtener_usuarios():
    respuesta = dict()
    listadiccs = []
    usuarios = controlador_usuario.obtener_usuarios()
    for usuario in usuarios:
        objUsuario = clase_usuario.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], usuario[8], usuario[9], usuario[10], usuario[11])
        listadiccs.append(objUsuario.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de usuarios correcto"
    return jsonify(respuesta)

##########Clientes##########
@app.route("/api_clientes", methods=["GET"])
#@jwt_required()
def api_clientes():
    respuesta = dict()
    listadiccs = []
    clientes = controlador_cliente.obtener_clientes()
    for cliente in clientes:
        objCliente = clase_cliente.Cliente(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6],cliente[7])
        listadiccs.append(objCliente.obtenerObjetoSerializable())
    respuesta["data"] = listadiccs
    respuesta["code"] = 1
    respuesta["message"] = "Listado de datos correcto"
    return jsonify(respuesta)
############# APIS #########################################






#----NORMAL----

@app.route("/")



@app.route("/index")
def index():
    return render_template('index.html')

#@app.route("/login", methods=["GET", "POST"])
#def login():
#    return render_template('login.html')


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

@app.route("/usuario")
def  usuario():
    username = request.cookies.get('username')
    token = request.cookies.get('token')
    usuario = controlador_usuario.obtener_usuario_por_username(username)
    if username is None:
        return render_template("login.html")
    if token == usuario[9] and usuario[10] == 2 and usuario[11]==True:
        return render_template("usuario.html",esSesionIniciada=True,usuario=usuario)
    return render_template("login.html")


@app.route("/control_admin", methods=["GET", "POST"])
def control_admin():
    return render_template("maestra_admin.html")

@app.route("/admin_det_ped")
def admin_det_ped():
    return render_template("admin_det_ped.html")

@app.route("/Blog")
def Blog():
    return render_template('Blog.html')

@app.route("/Sobre_Nosotros")
def Sobre_Nosotros():
    return render_template('Sobre_Nosotros.html')

##################### Cornejo ##########################
@app.route("/pago")
def pago():
    return render_template("pago.html")

@app.route("/misOrdenes")
def mis_ordenes():
    return render_template("misOrdenes.html")




#####################     MASCOTA     ############################
@app.route("/mascotas")
def formulario_mascotas():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            mascotas = controlador_mascota.obtener_mascotas()
            return render_template("mascotas.html", mascotas=mascotas)
        return render_template("login.html")
    except:
        return render_template("login.html")


@app.route("/agregar_mascota")
def formulario_registrar_mascota():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            return render_template('registrar_mascota.html')
        return render_template("login.html")
    except:
        return render_template("login.html")

@app.route("/insertar_mascota", methods=["POST"])
def metodo_insertar_mascota():
    nombre = request.form["nombre"]
    controlador_mascota.insertar_mascota(nombre)
    return redirect("/mascotas")

@app.route("/editar_mascota/<int:id>")
def formulario_editar_mascota(id):
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            mascota = controlador_mascota.obtener_mascota_por_id(id)
            return render_template("editar_mascota.html",mascota=mascota)
        return render_template("login.html")
    except:
        return render_template("login.html")


@app.route("/actualizar_mascota",methods=["POST"])
def metodo_actualizar_mascota():
    mascota_id = request.form["id"]
    nombre = request.form["nombre"]
    if request.form["estado"]=='SI':
        estado = True
    else:
        estado = False
    controlador_mascota.actualizar_mascota(nombre,mascota_id)
    controlador_mascota.actualizar_estado(estado,mascota_id)
    return redirect("/mascotas")

@app.route("/eliminar_mascota",methods=["POST"])
def metodo_eliminar_mascota():
    mascota_id = request.form["id"]
    controlador_mascota.eliminar_mascota(mascota_id)
    return redirect("/mascotas")
#####################     MASCOTA     ############################
#####################     METODO PAGO     ############################
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
#####################     METODO PAGO     ############################
#####################     CATEGORIAS    ############################
@app.route("/agregar_categoria")
def formulario_agregar_categoria():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            return render_template("agregar_categoria.html")
        return render_template("login.html")
    except:
        return render_template("login.html")


@app.route("/categoriasAdmin")
def categoriasAdmin():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            categorias = controlador_categorias.obtener_categorias()
            return render_template("categoriasAdmin.html", categorias=categorias)
        return render_template("login.html")
    except:
        return render_template("login.html")

@app.route("/guardar_categoria", methods=["POST"])
def guardar_categoria():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    controlador_categorias.insertar_categoria(nombre, descripcion)
    return redirect("/categoriasAdmin")

@app.route("/direccion_pago")
def direccion_pago():
    return render_template("direccion_pago.html")

@app.route("/eliminar_categoria", methods=["POST"])
def eliminar_categoria():
    controlador_categorias.eliminar_categoria(request.form["id"])
    return redirect("/categoriasAdmin")

@app.route("/formulario_editar_categoria/<int:id>")
def editar_categoria(id):
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            # Obtener la categoría por ID
            categoria = controlador_categorias.obtener_categoria_por_id(id)
            return render_template("editar_categoria.html", categoria=categoria)
        return render_template("login.html")
    except:
        return render_template("login.html")


@app.route("/actualizar_categoria", methods=["POST"])
def actualizar_categoria():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    if request.form["estado"]=='SI':
        estado = True
    else:
        estado = False
    controlador_categorias.actualizar_categoria(nombre, descripcion, id)
    controlador_categorias.actualizar_estado(estado,id)
    return redirect("/categoriasAdmin")
#####################     CATEGORIAS     ############################

#####################     PRODUCTO     ############################
@app.route("/catalogo_productos")
def catalogo_productos():
    categorias = controlador_producto.obtener_categorias()
    mascotas = controlador_mascota.obtener_mascotas()
    return render_template("catalogo_productos.html",categorias=categorias, mascotas=mascotas)

@app.route("/datos_producto/<int:id>")
def datos_producto(id):
    producto = controlador_producto.obtener_producto_por_id(id)
    return render_template("datos_producto.html",producto=producto)

@app.route("/productos")
def formulario_productos():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            productos = controlador_producto.obtener_productos_formateado()
            return render_template("productos.html", productos=productos)
        return render_template("login.html")
    except:
        return render_template("login.html")

@app.route("/agregar_producto")
def formulario_registrar_producto():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            categorias = controlador_producto.obtener_categorias()
            mascotas = controlador_mascota.obtener_mascotas()
            return render_template('registrar_producto.html', categorias=categorias, mascotas=mascotas)
        return render_template("login.html")
    except:
        return render_template("login.html")

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
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            producto = controlador_producto.obtener_producto_por_id(id)
            categorias = controlador_producto.obtener_categorias()
            mascotas = controlador_mascota.obtener_mascotas()
            return render_template("editar_producto.html",producto=producto, categorias=categorias, mascotas=mascotas)
        return render_template("login.html")
    except:
        return render_template("login.html")

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
    #controlador_producto.actualizar_producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen,producto_id)
    if link_imagen is None:
        controlador_producto.actualizar_imagen_producto(link_imagen, producto_id)
    controlador_producto.actualizar_producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,producto_id)
    return redirect("/productos")

@app.route("/eliminar_producto",methods=["POST"])
def metodo_eliminar_producto():
    producto_id = request.form["id"]
    controlador_producto.eliminar_producto(producto_id)
    return redirect("/productos")

@app.route("/lista_productos")
def lista_productos():
    respuesta = []
    productos = controlador_producto.obtener_productos_vigentes_formateado()
    for producto in productos:
        dict_producto = dict()
        dict_producto["id"] = producto[0]
        dict_producto["nombre"] = producto[1]
        dict_producto["descripcion"] = producto[2]
        dict_producto["precio"] = producto[3]
        dict_producto["stock"] = producto[4]
        dict_producto["estado"] = producto[5]
        dict_producto["categoria"] = producto[6]
        dict_producto["mascota"] = producto[7]
        dict_producto["imagen"] = producto[8]

        respuesta.append(dict_producto)

    return respuesta
#####################     PRODUCTO     ############################
#####################     CLIENTE    ############################

@app.route("/procesar_login_cliente", methods=["POST"])
def procesar_login_cliente():
    cliente_dni = request.form["cliente_dni"]
    password = request.form["password"]
    cliente = controlador_usuario.obtener_usuario_por_dni(cliente_dni)

    if cliente == None:
        return render_template("login.html")
    else:
        # Encriptar password ingresado por usuario
        h = hashlib.new('sha256')
        h.update(bytes(password,encoding='utf-8'))
        encpassword = h.hexdigest()
        if encpassword == cliente[8]:
            # Obteniendo token
            t = hashlib.new('sha256')
            entale = random.randint(1,1024)
            strEntale = str(entale)
            t.update(bytes(strEntale,encoding='utf-8'))
            token = t.hexdigest()
            # Acá se debe controlar con cookies
            resp = make_response(redirect("/usuario"))
            resp.set_cookie('cliente_dni', cliente_dni)
            resp.set_cookie('token', token)
            controlador_usuario.actualizar_token(cliente_dni, token)
            return resp

        return render_template("login.html")


@app.route("/clientes")
def formulario_clientes():
    clientes = controlador_cliente.obtener_clientes()
    return render_template("clientes.html", clientes=clientes)

@app.route("/agregar_cliente")
def formulario_registrar_cliente():
    return render_template('registrar_cliente.html')

@app.route("/registro_cliente", methods=["POST"])
def metodo_registro_cliente():
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    dni = request.form["dni"]
    username = request.form["username"]
    password = request.form["password"]

    h = hashlib.new('sha256')
    h.update(bytes(password,encoding='utf-8'))
    encpassword = h.hexdigest()

    controlador_usuario.registrar_usuario_cliente(nombres,apellidos,email,telefono,direccion,dni,username,encpassword)
    return redirect("/login")


@app.route("/insertar_cliente", methods=["POST"])
def metodo_insertar_cliente():
    nombre = request.form["nombre"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    cliente_dni = request.form["cliente_dni"]
    password = request.form["password"]

    controlador_cliente.insertar_cliente(nombre,email,telefono,direccion,cliente_dni,password)
    return redirect("/clientes")

@app.route("/editar_cliente/<int:id>")
def formulario_editar_cliente(id):
    cliente = controlador_cliente.obtener_cliente_por_id(id)
    return render_template("editar_cliente.html",cliente=cliente)

@app.route("/actualizar_cliente",methods=["POST"])
def metodo_actualizar_cliente():
    cliente_id = request.form["id"]
    nombre = request.form["nombre"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    cliente_dni = request.form["cliente_dni"]
    password = request.form["password"]
    controlador_cliente.actualizar_cliente(nombre,email,telefono,direccion,cliente_dni,password,cliente_id)
    return redirect("/clientes")

@app.route("/eliminar_cliente",methods=["POST"])
def metodo_eliminar_cliente():
    cliente_id = request.form["id"]
    controlador_cliente.eliminar_cliente(cliente_id)
    return redirect("/clientes")

@app.route("/lista_clientes")
def lista_clientes():
    respuesta = []
    clientes = controlador_cliente.obtener_clientes()
    for cliente in clientes:
        dict_cliente = dict()
        dict_cliente["id"] = cliente[0]
        dict_cliente["nombre"] = cliente[1]
        dict_cliente["email"] = cliente[2]
        dict_cliente["telefono"] = cliente[3]
        dict_cliente["direccion"] = cliente[4]
        dict_cliente["cliente_dni"] = cliente[5]
        dict_cliente["password"] = cliente[6]


        respuesta.append(dict_cliente)

    return respuesta




###################### PEDIDOS #################################

@app.route("/pedidos")
def formulario_pedidos():
    pedidos = controlador_pedido.obtener_pedidos_formateado()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/agregar_pedido")
def formulario_registrar_pedido():
    clientes = controlador_pedido.obtener_clientes()
    return render_template('registrar_pedido.html', clientes=clientes)

@app.route("/insertar_pedido", methods=["POST"])
def metodo_insertar_pedido():
    fecha_pedido = request.form["fecha_pedido"]
    estado_pedido = request.form["estado_pedido"]
    cliente_id = request.form["cliente_id"]
    controlador_pedido.insertar_pedidos(fecha_pedido, estado_pedido, cliente_id)
    return redirect("/pedidos")

@app.route("/editar_pedido/<int:id>")
def formulario_editar_pedido(id):
    pedido = controlador_pedido.obtener_pedido_por_id(id)
    clientes = controlador_pedido.obtener_clientes()
    return render_template("editar_pedido.html", pedido=pedido, clientes=clientes)

@app.route("/actualizar_pedido", methods=["POST"])
def metodo_actualizar_pedido():
     pedido_id = request.form["id"]
     fecha_pedido = request.form["fecha_pedido"]
     estado_pedido = request.form["estado_pedido"]
     cliente_id = request.form["cliente_id"]
     controlador_pedido.actualizar_pedido(fecha_pedido, estado_pedido, cliente_id, pedido_id)
     return redirect("/pedidos")

@app.route("/eliminar_pedido", methods=["POST"])
def metodo_eliminar_pedido():
    pedido_id = request.form["id"]
    controlador_pedido.eliminar_pedido(pedido_id)
    return redirect("/pedidos")


###################### VENTA #################################

@app.route("/venta")
def formulario_venta():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[11]==True:
            metodos = controlador_metodoP.obtener_metodos_pago()
            return render_template("venta.html",cliente=usuario,metodos=metodos)
        return render_template("login.html")
    except:
        return render_template("login.html")

@app.route("/metodo_venta", methods=["POST"])
def metodo_venta():
    #controlador_pedido.transaccion(datos)
    carrito = json.loads(request.body.decode())

    return jsonify(carrito)



#####################     INTERFAZ ADMIN     ############################
@app.route("/index_admin")
def interfaz_admin():
    try:
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login.html")
        if token == usuario[9] and usuario[10] == 1 and usuario[11]==True:
            return render_template("index_admin.html",esSesionIniciada=True)
        return render_template("login.html")
    except:
        return render_template("login.html")
#####################     INTERFAZ ADMIN     ############################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)