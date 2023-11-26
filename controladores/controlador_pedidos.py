from bd import obtenerConexion
import controladores.controlador_producto as controlador_producto

def insertar_pedidos(fecha_pedido, estado_pedido, cliente_id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pedido(fecha_pedido, estado_pedido, cliente_id) VALUES (%s, %s, %s)",
                       (fecha_pedido, estado_pedido, cliente_id))
    conexion.commit()
    conexion.close()


def obtener_pedidos():
    conexion = obtenerConexion()
    pedidos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT pedido_id, fecha_pedido, estado_pedido, cliente_id FROM pedido")
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos


def obtener_clientes():
    conexion = obtenerConexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cliente_id, nombre, email, telefono, direccion, cliente_dni FROM cliente")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def obtener_pedidos_formateado():
    conexion = obtenerConexion()
    pedidos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT ped.pedido_id, ped.fecha_pedido,
            CASE
            WHEN ped.estado_pedido = 'P' THEN 'Pendiente'
            WHEN ped.estado_pedido = 'E' THEN 'Enviado'
            WHEN ped.estado_pedido = 'R' THEN 'Recibido'
            ELSE 'Desconocido'
            END AS estado_pedido,
            cli.nombre as nombre_cliente
            FROM pedido as ped
            INNER JOIN cliente as cli
            ON ped.cliente_id = cli.cliente_id"""
        )
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos


def eliminar_pedido(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pedido WHERE pedido_id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_pedido_por_id(id):
    conexion = obtenerConexion()
    pedido = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT pedido_id, fecha_pedido, estado_pedido, cliente_id FROM pedido WHERE pedido_id = %s", (id,))
        pedido = cursor.fetchone()
    conexion.close()
    return pedido


def actualizar_pedido(fecha_pedido, estado_pedido, cliente_id, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE pedido SET fecha_pedido = %s, estado_pedido = %s, cliente_id = %s  WHERE pedido_id = %s",
                       (fecha_pedido, estado_pedido, cliente_id, id))
    conexion.commit()
    conexion.close()


def transaccion(datos):
    try:
        conexion = obtenerConexion()
        cursor = conexion.cursor()

        conexion.start_transaction()

        estado_pedido = datos["estado_pedido"]
        cliente_id = datos["cliente_id"]
        cursor.execute("INSERT pedido(fecha_pedido, estado_pedido, cliente_id) VALUES (CURRENT_DATE, %s, %s)",
                       (estado_pedido, cliente_id))

        monto_total = 0
        for detalle in datos["detalle_pedido"]:
            producto_id = detalle["producto_id"]
            cantidad = detalle["cantidad"]
            prod = controlador_producto.obtener_producto_por_id(producto_id)
            if cantidad>prod[4]:
                precio_unitario = detalle["precio_unitario"]
                monto_total += precio_unitario
                cursor.execute("INSERT detalle_pedido(pedido_id,producto_id,cantidad,precio_unitario) VALUES (%s,%s,%s,%s)",
                           (pedido_id,producto_id,cantidad,precio_unitario))
            else:
                conexion.rollback()
                return False

        tipo_comprobante = datos["tipo_comprobante"]
        metodo_id = datos["metodo_id"]
        cursor.execute("INSERT comprobantes(fecha_hora_emision,monto_total,tipo_comprobante,pedido_id,metodo_id) VALUES (CURRENT_TIMESTAMP,%s,%s,%s,%s)",
                       (monto_total,tipo_comprobante,pedido_id,metodo_id))

        conexion.commit()
        return True

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        conexion.rollback()
        return False

    finally:
        cursor.close()
        conexion.close()

def transaccion(productos):

    try:

        conexion = obtenerConexion()
        cursor = conexion.cursor()

        conexion.begin()
        for data in productos:
            precio = data["precio"]
            cantidad = data["cantidad"]
            pass

    except Exception as e:
        print("Error: {}".format(e.__str__()))
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()
    


