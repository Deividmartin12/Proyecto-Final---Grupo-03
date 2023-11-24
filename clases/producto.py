class Producto:
    producto_id = 0
    nombre = ""
    descripcion = ""
    precio = 0.0
    stock = 0
    estado = True
    categoria_id = 0
    mascota_id = 0
    link_imagen = ""

    def __init__(self, p_producto_id,p_nombre,p_descripcion,p_precio,p_stock,p_estado,p_categoria_id,p_mascota_id,p_link_imagen):
        self.producto_id = p_producto_id
        self.nombre = p_nombre
        self.descripcion = p_descripcion
        self.precio = p_precio
        self.stock = p_stock
        self.estado = p_estado
        self.categoria_id = p_categoria_id
        self.mascota_id = p_mascota_id
        self.link_imagen = p_link_imagen

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["producto_id"] = self.producto_id
        dict_temp["nombre"] = self.nombre
        dict_temp["descripcion"] = self.descripcion
        dict_temp["precio"] = self.precio
        dict_temp["stock"] = self.stock
        dict_temp["estado"] = self.estado
        dict_temp["categoria_id"] = self.categoria_id
        dict_temp["mascota_id"] = self.mascota_id
        dict_temp["link_imagen"] = self.link_imagen

        return dict_temp