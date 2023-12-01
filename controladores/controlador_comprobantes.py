from bd import obtenerConexion

def insertar_comprobante( fechaE, monto_total, tipo_comprobante, pedido_id, metodo_id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO comprobantes( fechaE, monto_total, tipo_comprobante, pedido_id, metodo_pago) VALUES (%s, %s, %s, %s, %s)",
            ( fechaE, monto_total, tipo_comprobante, pedido_id, metodo_id))
    conexion.commit()
    conexion.close()


def obtener_comprobantes():
    conexion = obtenerConexion()
    comprobantes = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT numero_boleta, fechaE, monto_total, tipo_comprobante, pedido_id, metodo_pago FROM comprobantes")
        comprobantes = cursor.fetchall()
    conexion.close()
    return comprobantes


def eliminar_comprobante(numero_boleta):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comprobantes WHERE numero_boleta = %s", (numero_boleta,))
    conexion.commit()
    conexion.close()


def obtener_comprobante_por_numero(numero_boleta):
    conexion = obtenerConexion()
    comprobante = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT numero_boleta, fechaE, monto_total, tipo_comprobante, pedido_id, metodo_pago FROM comprobantes WHERE numero_boleta = %s", (numero_boleta,))
        comprobante = cursor.fetchone()
    conexion.close()
    return comprobante


def actualizar_comprobante(fechaE, monto_total, tipo_comprobante, pedido_id, metodo_id, numero_boleta):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE comprobantes SET fechaE = %s, monto_total = %s, tipo_comprobante = %s, pedido_id = %s, metodo_pago = %s WHERE numero_boleta = %s",
            (fechaE, monto_total, tipo_comprobante, pedido_id, metodo_id, numero_boleta))
    conexion.commit()
    conexion.close()
