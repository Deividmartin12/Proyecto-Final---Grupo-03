from bd import obtenerConexion
from controladores import controlador_usuario

def insertar_pedidos(fecha_pedido, estado_pedido, usuario_id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pedido(fecha_pedido, estado_pedido, usuario_id) VALUES (%s, %s, %s)",
                       (fecha_pedido, estado_pedido, usuario_id))
    conexion.commit()
    conexion.close()


def obtener_pedidos():
    conexion = obtenerConexion()
    pedidos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT pedido_id, fecha_pedido, estado_pedido, usuario_id FROM pedido")
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos

def obtener_ultimo_idpedido():
    conexion = obtenerConexion()
    idpedido = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT coalesce(max(pedido_id),0)+1 as idpedido FROM pedido")
        idpedido = cursor.fetchone()
    conexion.close()
    return idpedido[0]

def obtener_clientes():
    conexion = obtenerConexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombres,apellidos, email, telefono, direccion, dni, username, password, token, tipo_usuario, estado FROM usuario")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def obtener_pedidos_formateado():
    conexion = obtenerConexion()
    pedidos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT ped.pedido_id, ped.fecha_pedido,CASE WHEN ped.estado_pedido = 'P' THEN 'Pendiente' WHEN ped.estado_pedido = 'E' THEN 'Enviado'  WHEN ped.estado_pedido = 'R' THEN 'Recibido' ELSE 'Desconocido' END AS estado_pedido, usu.nombres as nombre_cliente  FROM pedido as ped INNER JOIN usuario as usu ON ped.usuario_id = usu.id" )
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
            "SELECT pedido_id, fecha_pedido, estado_pedido, usuario_id FROM pedido WHERE pedido_id = %s", (id))
        pedido = cursor.fetchone()
    conexion.close()
    return pedido


def actualizar_pedido(fecha_pedido, estado_pedido, usuario_id, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE pedido SET fecha_pedido = %s, estado_pedido = %s, usuario_id = %s  WHERE pedido_id = %s",
                       (fecha_pedido, estado_pedido, usuario_id, id))
    conexion.commit()
    conexion.close()


def transaccion(productos):
    try:
        conexion = obtenerConexion()

        idpedido = obtener_ultimo_idpedido()
        total = 0

        user = controlador_usuario.obtener_usuario_por_username(productos["username"])
        id_user = user[0] 

        with conexion.cursor() as cursor:
            queryPedido = 'insert into pedido(pedido_id,usuario_id,fecha_pedido,estado_pedido) values(%s,%s,CURRENT_TIMESTAMP, %s)'
            cursor.execute(queryPedido,(idpedido,id_user,'R'))

        with conexion.cursor() as cursor:
            for data in productos['carrito']:
                idproducto = data['idproducto']
                precio_unitario = data["precio"]
                cantidad = data["cantidad"]

                total += precio_unitario * cantidad
                queryDetallePedido = 'insert into detalle_pedido(pedido_id,producto_id,cantidad,precio_unitario) values(%s,%s,%s,%s)'
                cursor.execute(queryDetallePedido,(idpedido,idproducto,cantidad,precio_unitario))

        with conexion.cursor() as cursor:
            queryComprobante = 'insert into comprobantes(pedido_id, fechaE,monto_total,tipo_comprobante, Metodo_pago) values(%s,CURRENT_TIMESTAMP,%s,%s,%s)'
            cursor.execute(queryComprobante,(idpedido,total,'B',productos['metodo_id']))

        conexion.commit()
        return True
    except Exception as e:
        print("Error: {}".format(e.__str__()))
        conexion.rollback()
        raise e
    finally:
        conexion.close()