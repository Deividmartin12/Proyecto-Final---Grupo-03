from bd import obtenerConexion

def insertar_metodo_pago(nombre, descripcion):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO metodo_pago(nombre, descripcion, estado) VALUES (%s, %s, %s)",
            (nombre, descripcion, True)
        )
    conexion.commit()
    conexion.close()


def obtener_metodos_pago():
    conexion = obtenerConexion()
    metodos_pago = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT metodo_id, nombre, descripcion, estado FROM metodo_pago")
        metodos_pago = cursor.fetchall()
    conexion.close()
    return metodos_pago

def eliminar_metodo_pago(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM metodo_pago WHERE metodo_id = %s", (id))
    conexion.commit()
    conexion.close()

def obtener_metodo_pago_por_id(id):
    conexion = obtenerConexion()
    metodo_pago = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT metodo_id, nombre, descripcion, estado FROM metodo_pago WHERE metodo_id = %s", (id))
        metodo_pago = cursor.fetchone()
    conexion.close()
    return metodo_pago

def actualizar_metodo_pago(nombre, descripcion, estado, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE metodo_pago SET nombre = %s, descripcion = %s, estado = %s WHERE metodo_id = %s",
            (nombre, descripcion, estado, id)
        )
    conexion.commit()
    conexion.close()

def darbaja_metodo(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE metodo_pago SET estado = false WHERE producto_id = %s",
                       (id))
    conexion.commit()
    conexion.close()