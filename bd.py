import pymysql

def obtenerConexion():
    return pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='',
                           db='project_veterinaria')



#def obtenerConexion():
 #   return pymysql.connect(host='grupo1DAW.mysql.pythonanywhere-services.com',
  #                         user='grupo1DAW',
   #                        password='losjala2',
      #                     db='grupo1DAW$default')