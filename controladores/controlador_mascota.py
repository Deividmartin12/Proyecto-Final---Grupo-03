from bd import obtenerConexion


def insertar_mascota(nombre):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO mascota(nombre) VALUES (%s)",
                       (nombre))
    conexion.commit()
    conexion.close()


def obtener_mascotas():
    conexion = obtenerConexion()
    mascotas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT mascota_id, nombre FROM mascota")
        mascotas = cursor.fetchall()
    conexion.close()
    return mascotas


def eliminar_mascota(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM mascota WHERE mascota_id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_mascota_por_id(id):
    conexion = obtenerConexion()
    mascota = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT mascota_id,nombre FROM mascota WHERE mascota_id = %s", (id,))
        mascota = cursor.fetchone()
    conexion.close()
    return mascota


def actualizar_mascota(nombre, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE mascota SET nombre = %s WHERE mascota_id = %s",
                       (nombre, id))
    conexion.commit()
    conexion.close()