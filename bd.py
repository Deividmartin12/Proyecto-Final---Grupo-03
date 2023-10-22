import pymysql

def obtenerConexion():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='',
                           db='project_veterinaria')