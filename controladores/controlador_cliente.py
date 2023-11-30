from bd import obtenerConexion





def eliminar_cliente(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id))
    conexion.commit()
    conexion.close()



def actualizar_token(entrada,token):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET token = %s WHERE username = %s OR dni = %s",
                       (token,entrada,entrada))
    conexion.commit()
    conexion.close()




def obtener_clientes():
    conexion = obtenerConexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario where tipo_usuario=2")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def actualizar_cliente(id,nombres,apellidos,email,telefono,direccion,dni,estado):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombres = %s,apellidos = %s,email = %s,telefono = %s,direccion = %s,dni = %s,estado=%s WHERE id = %s",
                       (nombres,apellidos,email,telefono,direccion,dni,estado,id))
    conexion.commit()
    conexion.close()



def obtener_cliente_por_username(username):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_cliente_por_dni(dni):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario,estado FROM usuario WHERE dni = %s", (dni,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario