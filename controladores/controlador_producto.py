from bd import obtenerConexion


def insertar_producto(nombre, descripcion, precio, stock, categoria_id, mascota_id, link_imagen):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto(nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                       (nombre, descripcion, precio, stock, True, categoria_id, mascota_id, link_imagen))
    conexion.commit()
    conexion.close()


def obtener_categoria_por_id(id):
    conexion = obtenerConexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT categoria_id,nombre,descripcion FROM categoria WHERE categoria_id = %s", (id,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria


def obtener_categorias():
    conexion = obtenerConexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT categoria_id,nombre,descripcion FROM categoria")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias


def obtener_categorias_vigentes():
    conexion = obtenerConexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT categoria_id,nombre,descripcion FROM categoria where estado = true")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias


def obtener_productos():
    conexion = obtenerConexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT producto_id,nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen FROM producto")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def obtener_productos_formateado():
    conexion = obtenerConexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT pro.producto_id, pro.nombre, pro.descripcion, pro.precio, pro.stock,
            CASE
            WHEN pro.estado is true THEN 'Vigente'
            ELSE 'No vigente'
            END AS estado
            , cat.nombre AS categoria, mas.nombre AS mascota, link_imagen FROM producto as pro
            INNER JOIN categoria AS cat ON cat.categoria_id = pro.categoria_id
            INNER JOIN mascota AS mas ON mas.mascota_id = pro.mascota_id
            WHERE pro.estado is true""")
    productos = cursor.fetchall()
    conexion.close()
    return productos


def obtener_productos_no_vigentes_formateado():
    conexion = obtenerConexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT pro.producto_id, pro.nombre, pro.descripcion, pro.precio, pro.stock,
            CASE
            WHEN pro.estado is true THEN 'Vigente'
            ELSE 'No vigente'
            END AS estado
            , cat.nombre AS categoria, mas.nombre AS mascota, link_imagen FROM producto as pro
            INNER JOIN categoria AS cat ON cat.categoria_id = pro.categoria_id
            INNER JOIN mascota AS mas ON mas.mascota_id = pro.mascota_id
            WHERE pro.estado is false""")
    productos = cursor.fetchall()
    conexion.close()
    return productos


def obtener_productos_vigentes_formateado():
    conexion = obtenerConexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT pro.producto_id, pro.nombre, pro.descripcion, pro.precio, pro.stock,
                CASE
                WHEN pro.estado is true THEN 'Vigente'
                ELSE 'No vigente'
                END AS estado
                , cat.nombre AS categoria, mas.nombre AS mascota, link_imagen FROM producto as pro
                INNER JOIN categoria AS cat ON cat.categoria_id = pro.categoria_id
                INNER JOIN mascota AS mas ON mas.mascota_id = pro.mascota_id WHERE pro.estado = true""")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE producto_id = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtenerConexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT producto_id,nombre,descripcion,precio,stock,estado,categoria_id,mascota_id,link_imagen FROM producto WHERE producto_id = %s", (id))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_producto(nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, link_imagen, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s,descripcion = %s,precio = %s,stock = %s,estado = %s,categoria_id = %s,mascota_id = %s, link_imagen = %s  WHERE producto_id = %s",
                       (nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, link_imagen, id))
    conexion.commit()
    conexion.close()


def actualizar_producto_sinImagen(nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s,descripcion = %s,precio = %s,stock = %s,estado = %s,categoria_id = %s,mascota_id = %s  WHERE producto_id = %s",
                       (nombre, descripcion, precio, stock, estado, categoria_id, mascota_id, id))
    conexion.commit()
    conexion.close()


def actualizar_imagen_producto(link_imagen, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET link_imagen = %s  WHERE producto_id = %s",
                       (link_imagen, id))
    conexion.commit()
    conexion.close()


def actualizar_estado(estado, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET estado = %s WHERE producto_id = %s",
                       (estado, id))
    conexion.commit()
    conexion.close()

def darbaja_producto(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET estado = NOT estado WHERE producto_id = %s",
                       (id))
    conexion.commit()
    conexion.close()
