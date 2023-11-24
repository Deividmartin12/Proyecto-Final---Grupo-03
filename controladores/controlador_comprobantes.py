from bd import obtenerConexion

def insertar_comprobante( fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO comprobante( fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id) VALUES (%s, %s, %s, %s, %s, %s)",
            ( fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id))
    conexion.commit()
    conexion.close()


def obtener_comprobantes():
    conexion = obtenerConexion()
    comprobantes = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT numero_boleta, fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id FROM comprobante")
        comprobantes = cursor.fetchall()
    conexion.close()
    return comprobantes


def eliminar_comprobante(numero_boleta):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comprobante WHERE numero_boleta = %s", (numero_boleta,))
    conexion.commit()
    conexion.close()


def obtener_comprobante_por_numero(numero_boleta):
    conexion = obtenerConexion()
    comprobante = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT numero_boleta, fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id FROM comprobante WHERE numero_boleta = %s", (numero_boleta,))
        comprobante = cursor.fetchone()
    conexion.close()
    return comprobante


def actualizar_comprobante(fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id, numero_boleta):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE comprobante SET fecha_hora_emision = %s, monto_total = %s, tipo_comprobante = %s, pedido_id = %s, metodo_id = %s WHERE numero_boleta = %s",
            (fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id, numero_boleta))
    conexion.commit()
    conexion.close()
