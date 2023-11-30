class Categoria:
    id = 0
    nombre = ""
    descripcion = ""
    estado = True

    def __init__(self, p_id, p_nombre,p_descripcion,p_estado):
        self.id = p_id
        self.nombre = p_nombre
        self.descripcion = p_descripcion
        self.estado = p_estado


    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"]      = self.id
        dict_temp["nombre"]  = self.nombre
        dict_temp["descripcion"] = self.descripcion
        dict_temp["estado"] = self.estado
        return dict_temp