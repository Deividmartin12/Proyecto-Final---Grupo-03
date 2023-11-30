class Mascota:
    mascota_id = 0
    nombre = ""
    estado = True

    def __init__(self, p_mascota_id, p_nombre, p_estado):
        self.mascota_id = p_mascota_id
        self.nombre = p_nombre
        self.estado = p_estado

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"]      = self.mascota_id
        dict_temp["nombre"]  = self.nombre
        dict_temp["estado"]  = self.estado
        return dict_temp