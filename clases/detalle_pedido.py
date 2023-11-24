class DetallePedido:
    pedido_id = 0
    producto_id = 0
    cantidad = 0
    precio_unitario = 0.0

    def __init__(self, p_pedido_id, p_producto_id, p_cantidad, p_precio_unitario):
        self.pedido_id = p_pedido_id
        self.producto_id = p_producto_id
        self.cantidad = p_cantidad
        self.precio_unitario = p_precio_unitario

    def obtener_objeto_serializable(self):
        dict_temp = dict()
        dict_temp["pedido_id"] = self.pedido_id
        dict_temp["producto_id"] = self.producto_id
        dict_temp["cantidad"] = self.cantidad
        dict_temp["precio_unitario"] = self.precio_unitario
        return dict_temp
