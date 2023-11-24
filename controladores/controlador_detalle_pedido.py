from bd import obtenerConexion
import controladores.controlador_producto as controlador_producto
import controladores.controlador_pedidos as controlador_pedido

def insertar_det_pedido(pedido_id,producto_id,cantidad,precio_unitario):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_pedido(pedido_id,producto_id,cantidad,precio_unitario) VALUES (%s, %s, %s, %s)",
                       (pedido_id,producto_id,cantidad,precio_unitario))
    conexion.commit()
    conexion.close()

def obtener_det_pedido_por_id(pedido,producto):
    conexion= obtenerConexion()
    det_ped = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select pedido_id, producto_id, cantidad, precio_unitario where pedido_id= %s and producto_id=%s", (pedido,producto))
        det_ped = cursor.fetchone()
    conexion.close()
    return det_ped

def obtener_det_pedido():
    conexion = obtenerConexion()
    det_peds=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT pedido_id, producto_id, cantidad, precio_unitario from detalle_pedido")
        det_peds= cursor.fetchall()
    conexion.close()
    return det_peds




def actualizar_det_pedido(pedido_id, producto_id, nueva_cantidad, nuevo_precio_unitario):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE detalle_pedido SET cantidad=%s, precio_unitario=%s WHERE pedido_id=%s AND producto_id=%s",
            (nueva_cantidad, nuevo_precio_unitario, pedido_id, producto_id)
        )
    conexion.commit()
    conexion.close()


def eliminar_det_pedido(pedido_id, producto_id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM detalle_pedido WHERE pedido_id=%s AND producto_id=%s",
            (pedido_id, producto_id)
        )
    conexion.commit()
    conexion.close()



