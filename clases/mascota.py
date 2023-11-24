class Mascota:
    mascota_id = 0
    nombre = ""

    def __init__(self, p_mascota_id, p_nombre):
        self.mascota_id = p_mascota_id
        self.nombre = p_nombre


    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"]      = self.mascota_id
        dict_temp["nombre"]  = self.nombre
        return dict_temp