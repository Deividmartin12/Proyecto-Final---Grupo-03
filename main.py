from flask import Flask, render_template, request, redirect, flash, jsonify,json
from markupsafe import escape
import controladores.controlador_metodoP as controlador_metodoP
import math
from flask import url_for
from flask import make_response
import hashlib
import random
import controladores.controlador_categorias as controlador_categorias
import controladores.controlador_mascota as controlador_mascota
import controladores.controlador_producto as controlador_producto
import controladores.controlador_cliente as controlador_cliente

app = Flask(__name__)

#########Comprobantes########
@app.route("/api_comprobantes", methods=["GET"])
def api_comprobantes():
    comprobantes = controlador_comprobantes.obtener_comprobantes()
    return jsonify({'Mensaje': 'Comprobantes obtenidos correctamente', 'Codigo': '1', 'Comprobantes': comprobantes})

@app.route("/api_agregar_comprobante", methods=["POST"])
def api_guardar_comprobante():
    try:
        fechaE = request.json["fechaE"]
        monto = request.json["monto"]
        tipoC = request.json["tipoC"]
        pedidoId = request.json["pedidoId"]
        metodoPId = request.json["metodoPId"]
        controlador_comprobantes.insertar_comprobante(fechaE, monto, tipoC, pedidoId, metodoPId)
        return jsonify({'Mensaje': 'Registro correcto', 'Codigo': '1'})
    except Exception as e:
        return jsonify({'Mensaje': 'Error interno del servidor', 'Codigo': '500', 'Error': str(e)}), 500

@app.route("/api_editar_comprobante", methods=["POST"])
def api_actualizar_comprobante():
    id = request.json["id"]
    fechaE = request.json["fechaE"]
    monto = request.json["monto"]
    tipoC = request.json["tipoC"]
    pedidoId = request.json["pedidoId"]
    metodoPId = request.json["metodoPId"]
    controlador_comprobantes.actualizar_comprobante(id, fechaE, monto, tipoC, pedidoId, metodoPId)
    return jsonify({'Mensaje': 'Actualización correcta', 'Codigo': '1'})

#########MetodosPago########
@app.route("/api_metodos_pago", methods=["GET"])
def api_metodos_pago():
    metodos_pago = controlador_metodoP.obtener_metodos_pago()
    return jsonify({'Mensaje': 'Métodos de pago obtenidos correctamente', 'Codigo': '1', 'Metodos_pago': metodos_pago})

@app.route("/api_actualizar_metodo_pago", methods=["POST"])
def api_actualizar_metodo_pago():
    id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_metodoP.actualizar_metodo_pago(nombre, descripcion, id)
    return jsonify({'Mensaje': 'Actualización correcta', 'Codigo': '1'})

@app.route("/api_guardar_metodo_pago", methods=["POST"])
def api_guardar_metodo_pago():
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_metodoP.insertar_metodo_pago(nombre, descripcion)
    return jsonify({'Mensaje': 'Registro correcto', 'Codigo': '1'})


#########Categorias########
@app.route("/api_guardar_categoria", methods=["POST"])
def api_guardar_categoria():
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_categorias.insertar_categoria(nombre, descripcion)
    return jsonify({'Mensaje': 'Registro correcto', 'Codigo': '1'})

@app.route("/api_actualizar_categoria", methods=["POST"])
def api_actualizar_categoria():
    id = request.json["id"]
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    controlador_categorias.actualizar_categoria(nombre, descripcion, id)
    return jsonify({'Mensaje': 'Actualización correcta', 'Codigo': '1'})

@app.route("/api_categorias", methods=["GET"])
def api_categorias():
    categorias = controlador_categorias.obtener_categorias()
    return jsonify({'Mensaje': 'Categorías obtenidas correctamente', 'Codigo': '1', 'Categorias': categorias})

#########Mascotas########

@app.route("/api_mascotas", methods=["GET"])
def api_obtener_mascotas():
    mascotas = controlador_mascota.obtener_mascotas()
    return jsonify({'Mensaje': 'Mascotas obtenidas correctamente', 'Codigo': '1', 'Mascotas': mascotas})
@app.route("/api_insertar_mascota", methods=["POST"])
def api_insertar_mascota():
    nombre = request.json["nombre"]
    controlador_mascota.insertar_mascota(nombre)
    return jsonify({'Mensaje': 'Inserción correcta', 'Codigo': '1'})
@app.route("/api_actualizar_mascota", methods=["POST"])
def api_actualizar_mascota():
    mascota_id = request.json["id"]
    nombre = request.json["nombre"]
    controlador_mascota.actualizar_mascota(nombre, mascota_id)
    return jsonify({'Mensaje': 'Actualización correcta', 'Codigo': '1'})

#########Productos########

@app.route("/api_productos", methods=["GET"])
def api_productos():
    productos = controlador_producto.obtener_productos()
    return jsonify({'Mensaje': 'Productos obtenidos correctamente', 'Codigo': '1', 'Productos': productos})

@app.route("/api_actualizar_producto", methods=["POST"])
def api_actualizar_producto():
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
    return jsonify({'Mensaje': 'Actualización correcta', 'Codigo': '1'})

@app.route("/api_insertar_producto", methods=["POST"])
def api_insertar_producto():
    nombre = request.json["nombre"]
    descripcion = request.json["descripcion"]
    precio = request.json["precio"]
    stock = request.json["stock"]
    estado = request.json["estado"]
    categoria_id = request.json["categoria_id"]
    mascota_id = request.json["mascota_id"]
    link_imagen = request.json["imagen"]
    controlador_producto.insertar_producto(nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, link_imagen)
    return jsonify({'Mensaje': 'Inserción correcta', 'Codigo': '1'})
############# WEB #########################################








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

@app.route("/usuario")
def  usuario():
    return render_template('usuario.html')


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
    return render_template("agregar_categoria.html")

@app.route("/categoriasAdmin")
def categoriasAdmin():
    categorias = controlador_categorias.obtener_categorias()
    return render_template("categoriasAdmin.html", categorias=categorias)

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
    # Obtener la categoría por ID
    categoria = controlador_categorias.obtener_categoria_por_id(id)
    return render_template("editar_categoria.html", categoria=categoria)

@app.route("/actualizar_categoria", methods=["POST"])
def actualizar_categoria():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    controlador_categorias.actualizar_categoria(nombre, descripcion, id)
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


@app.route("/clientes")
def formulario_clientes():
    clientes = controlador_cliente.obtener_clientes()
    return render_template("clientes.html", clientes=clientes)

@app.route("/agregar_cliente")
def formulario_registrar_cliente():
    return render_template('registrar_cliente.html')

@app.route("/registro_cliente", methods=["POST"])
def metodo_registro_cliente():
    nombre = request.form["nombre"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    cliente_dni = request.form["cliente_dni"]
    password = request.form["password"]

    controlador_cliente.insertar_cliente(nombre,email,telefono,direccion,cliente_dni,password)
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

#####################     INTERFAZ ADMIN     ############################
@app.route("/index_admin")
def interfaz_admin():
    return render_template("index_admin.html")
#####################     INTERFAZ ADMIN     ############################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)