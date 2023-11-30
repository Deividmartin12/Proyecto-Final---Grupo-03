class Pedido:
    id = 0
    fecha_pedido = ""
    estado_pedido = ""
    usuario_id = 0

    def __init__(self, p_id, p_fecha_pedido, p_estado_pedido, p_usuario_id):
        self.id = p_id
        self.fecha_pedido = p_fecha_pedido
        self.estado_pedido = p_estado_pedido
        self.usuario_id = p_usuario_id

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"] = self.id
        dict_temp["fecha_pedido"] = self.fecha_pedido
        dict_temp["estado_pedido"] = self.estado_pedido
        dict_temp["usuario_id"] = self.usuario_id
        return dict_temp