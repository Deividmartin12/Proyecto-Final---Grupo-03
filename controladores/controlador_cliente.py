from bd import obtenerConexion


def insertar_cliente(nombre, email, telefono, direccion, cliente_dni, password):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(nombre, email, telefono, direccion, cliente_dni, password) VALUES (%s, %s, %s, %s, %s, %s)",
                       (nombre, email, telefono, direccion, cliente_dni, password))
    conexion.commit()
    conexion.close()


def obtener_clientes():
    conexion = obtenerConexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cliente_id, nombre, email, telefono, direccion, cliente_dni, password, token FROM cliente")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def eliminar_cliente(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE cliente_id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(id):
    conexion = obtenerConexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT cliente_id, nombre, email, telefono, direccion, cliente_dni, password, token FROM cliente WHERE cliente_id = %s", (id,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente

def obtener_cliente_por_dni(dni):
    conexion = obtenerConexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT cliente_id, nombre, email, telefono, direccion, cliente_dni, password, token FROM cliente WHERE cliente_dni = %s", (dni,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente


def actualizar_cliente(nombre, email, telefono, direccion, cliente_dni, password, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET nombre = %s, email = %s, telefono = %s, direccion = %s, cliente_dni = %s, password = %s WHERE cliente_id = %s",
                       (nombre, email, telefono, direccion, cliente_dni, password, id))
    conexion.commit()
    conexion.close()



def actualizar_token(cliente_dni,token):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET token = %s WHERE cliente_dni = %s",
                       (token,cliente_dni))
    conexion.commit()
    conexion.close()