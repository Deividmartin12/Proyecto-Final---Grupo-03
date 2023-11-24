class Comprobante:
    numero_boleta = 0
    fecha_hora_emision = ""
    monto_total = 0.0
    tipo_comprobante = ""
    pedido_id = 0
    metodo_id = 0

    def __init__(self, numero_boleta, fecha_hora_emision, monto_total, tipo_comprobante, pedido_id, metodo_id):
        self.numero_boleta = numero_boleta
        self.fecha_hora_emision = fecha_hora_emision
        self.monto_total = monto_total
        self.tipo_comprobante = tipo_comprobante
        self.pedido_id = pedido_id
        self.metodo_id = metodo_id

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["numero_boleta"] = self.numero_boleta
        dict_temp["fecha_hora_emision"] = self.fecha_hora_emision
        dict_temp["monto_total"] = self.monto_total
        dict_temp["tipo_comprobante"] = self.tipo_comprobante
        dict_temp["pedido_id"] = self.pedido_id
        dict_temp["metodo_id"] = self.metodo_id
        return dict_temp
