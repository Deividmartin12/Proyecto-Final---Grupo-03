from bd import obtenerConexion


def insertar_mascota(nombre):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO mascota(nombre,estado) VALUES (%s,%s)",
                       (nombre,True))
    conexion.commit()
    conexion.close()


def obtener_mascotas():
    conexion = obtenerConexion()
    mascotas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT mascota_id, nombre,estado FROM mascota")
        mascotas = cursor.fetchall()
    conexion.close()
    return mascotas

def obtener_mascotas_vigentes():
    conexion = obtenerConexion()
    mascotas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT mascota_id, nombre,estado FROM mascota where estado = true")
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
            "SELECT mascota_id,nombre,estado FROM mascota WHERE mascota_id = %s", (id,))
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

def actualizar_estado(estado, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE mascota SET estado = %s WHERE mascota_id = %s",
                       (estado, id))
    conexion.commit()
    conexion.close()

def actualizar_estadoInterfaz(estado, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE mascota SET estado = %s WHERE mascota_id = %s",
                       (estado, id))
        cursor.execute("UPDATE producto SET estado = %s WHERE mascota_id = %s and categoria_id in (select categoria_id from categoria where estado = %s)",
        (estado,id,estado))
    conexion.commit()
    conexion.close()