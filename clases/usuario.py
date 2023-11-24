class Usuario:
    id = 0
    nombres = ""
    apellidos = ""
    email = ""
    telefono = ""
    direccion = ""
    dni = ""
    username = ""
    password = ""
    token = ""
    tipo_usuario = ""
    estado = True

    def __init__(self, p_id,p_nombres,p_apellidos,p_email,p_telefono,p_direccion,p_dni,p_username, p_password, p_token,p_tipo_usuario,p_estado):
        self.id = p_id
        self.nombres = p_nombres
        self.apellidos = p_apellidos
        self.email = p_email
        self.telefono = p_telefono
        self.direccion = p_direccion
        self.dni = p_dni
        self.username = p_username
        self.password = p_password
        self.token = p_token
        self.tipo_usuario = p_tipo_usuario
        self.estado = p_estado


    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"]      = self.id
        dict_temp["nombres"] = self.nombres
        dict_temp["apellidos"] = self.apellidos
        dict_temp["email"] = self.email
        dict_temp["telefono"] = self.telefono
        dict_temp["direccion"] = self.direccion
        dict_temp["dni"] = self.dni
        dict_temp["username"] = self.username
        dict_temp["password"] = self.password
        dict_temp["token"] = self.token
        dict_temp["tipo_usuario"] = self.tipo_usuario
        dict_temp["estado"] = self.estado

        return dict_temp