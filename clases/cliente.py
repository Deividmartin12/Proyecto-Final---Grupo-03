class Cliente:
    cliente_id = 0
    nombre = ""
    email = ""
    telefono = 0
    direccion = ""
    cliente_dni = ""
    password = ""
    token = ""


    def __init__(self, p_cliente_id,p_nombre,p_email,p_telefono,p_direccion,p_cliente_dni,p_password,p_token):
        self.cliente_id = p_cliente_id
        self.nombre = p_nombre
        self.email = p_email
        self.telefono = p_telefono
        self.direccion = p_direccion
        self.cliente_dni = p_cliente_dni
        self.password = p_password
        self.token = p_token

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["cliente_id"] = self.cliente_id
        dict_temp["nombre"] = self.nombre
        dict_temp["email"] = self.email
        dict_temp["telefono"] = self.telefono
        dict_temp["direccion"] = self.direccion
        dict_temp["cliente_dni"] = self.cliente_dni
        dict_temp["password"] = self.password
        dict_temp["token"] = self.token

        return dict_temp