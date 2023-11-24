class MetodoPago:
    metodo_id = 0
    nombre = ""
    descripcion = ""
    estado = True

    def __init__(self, metodo_id, nombre, descripcion, estado):
        self.metodo_id = metodo_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["metodo_id"] = self.metodo_id
        dict_temp["nombre"] = self.nombre
        dict_temp["descripcion"] = self.descripcion
        dict_temp["estado"] = self.estado
        return dict_temp

