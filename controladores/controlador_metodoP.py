from bd import obtener_conexion

def insertar_metodo_pago(nombre, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO metodo_pago(nombre, descripcion) VALUES (%s, %s)",
            (nombre, descripcion)
        )
    conexion.commit()
    conexion.close()

def obtener_metodos_pago():
    conexion = obtener_conexion()
    metodos_pago = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT metodo_id, nombre, descripcion FROM metodo_pago")
        metodos_pago = cursor.fetchall()
    conexion.close()
    return metodos_pago

def eliminar_metodo_pago(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM metodo_pago WHERE metodo_id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_metodo_pago_por_id(id):
    conexion = obtener_conexion()
    metodo_pago = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT metodo_id, nombre, descripcion FROM metodo_pago WHERE metodo_id = %s", (id,))
        metodo_pago = cursor.fetchone()
    conexion.close()
    return metodo_pago

def actualizar_metodo_pago(nombre, descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE metodo_pago SET nombre = %s, descripcion = %s WHERE metodo_id = %s",
            (nombre, descripcion, id)
        )
    conexion.commit()
    conexion.close()
