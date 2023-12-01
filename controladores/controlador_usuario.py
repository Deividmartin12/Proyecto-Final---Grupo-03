'''from bd import obtenerConexion


def registrar_usuario(username,password):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(username,password) VALUES (%s,%s)",
                       (username,password))
    conexion.commit()
    conexion.close()

def obtener_usuarios():
    conexion = obtenerConexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,username,password,token FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def obtener_usuario_por_username(username):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,username,password,token FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_id(id):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,username,password,token FROM usuario WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def eliminar_usuario(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def actualizar_usuario(username,password, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET username = %s,password = %s WHERE id = %s",
                       (username,password, id))
    conexion.commit()
    conexion.close()

def actualizar_token(username,token):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET token = %s WHERE username = %s",
                       (token,username))
    conexion.commit()
    conexion.close()'''


from bd import obtenerConexion


def registrar_usuario_cliente(nombres,apellidos,email,telefono,direccion,dni,username,password):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombres,apellidos,email,telefono,direccion,dni,username,password,tipo_usuario,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (nombres,apellidos,email,telefono,direccion,dni,username,password,2,True))
    conexion.commit()
    conexion.close()

def registrar_usuario_empleado(nombres,apellidos,email,telefono,direccion,dni,username,password):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombres,apellidos,email,telefono,direccion,dni,username,password,tipo_usuario,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (nombres,apellidos,email,telefono,direccion,dni,username,password,1,True))
    conexion.commit()
    conexion.close()



def obtener_administrador(nombre_busqueda=None):
    conexion = obtenerConexion()
    usuarios = []
    with conexion.cursor() as cursor:
        if nombre_busqueda:
            # Si se proporciona un nombre, filtrar por él
            cursor.execute("SELECT id, nombres, apellidos, email, telefono, direccion, dni, username, password, token, tipo_usuario, estado FROM usuario WHERE tipo_usuario=1 AND nombres LIKE %s", ('%' + nombre_busqueda + '%',))
        else:
            # Sin búsqueda por nombre, obtener todos los clientes
            cursor.execute("SELECT id, nombres, apellidos, email, telefono, direccion, dni, username, password, token, tipo_usuario, estado FROM usuario WHERE tipo_usuario=1")
            
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios




def obtener_usuario_por_username(username):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_dni(dni):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE dni = %s", (dni,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_id(id):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE id = %s", (id))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_dni_username(entrada):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE dni = %s OR username = %s", (entrada,entrada))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def eliminar_usuario(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id))
    conexion.commit()
    conexion.close()

def actualizar_usuario_cliente(id,nombres,apellidos,email,telefono,direccion,username,dni,estado):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombres = %s,apellidos = %s,email = %s,telefono = %s,direccion = %s,username=%s,dni = %s,estado=%s WHERE id = %s",
                       (nombres,apellidos,email,telefono,direccion,username,dni,estado,id))
    conexion.commit()
    conexion.close()

def actualizar_usuario_empleado(nombres,apellidos,email,telefono,direccion,dni,username,password,id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombres = %s,apellidos = %s,email = %s,telefono = %s,direccion = %s,dni = %s,username = %s,password = %s,tipo_usuario =%s WHERE id = %s",
                       (nombres,apellidos,email,telefono,direccion,dni,username,password,1,id))
    conexion.commit()
    conexion.close()


def cambiar_permisos(id):
    conexion = obtenerConexion()
    
    with conexion.cursor() as cursor:
        # Obtener el tipo_usuario actual
        cursor.execute("SELECT tipo_usuario FROM usuario WHERE id = %s", (id,))
        tipo_usuario_actual = cursor.fetchone()[0]

        # Cambiar el tipo_usuario
        nuevo_tipo_usuario = 2 if tipo_usuario_actual == 1 else 1
        cursor.execute("UPDATE usuario SET tipo_usuario = %s WHERE id = %s", (nuevo_tipo_usuario, id))

    conexion.commit()
    conexion.close()

def actualizar_token(entrada,token):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET token = %s WHERE username = %s OR dni = %s",
                       (token,entrada,entrada))
    conexion.commit()
    conexion.close()