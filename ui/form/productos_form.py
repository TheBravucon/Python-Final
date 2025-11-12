import tkinter as tk

from ui.base.input import Input


class ProductosForm:
    def __init__(self, ventana):
        self.nombre_producto = tk.StringVar(ventana)
        self.precio_producto = tk.DoubleVar(ventana)
        self.cantidad = tk.IntVar(ventana)
        self.nombre_producto_input = Input(ventana, 'Nombre', self.nombre_producto, [0, 0, 0, 1], [5, 5, 5, 5])
        self.precio_producto_input = Input(ventana, 'Precio', self.precio_producto, [1, 0, 1, 1], [5, 5, 5, 5])
        self.cantidad_producto_input = Input(ventana, 'Cantidad', self.cantidad, [2, 0, 2, 1], [5, 5, 5, 5])

    def get_nombre_producto(self):
        return self.nombre_producto

    def get_precio_producto(self):
        return self.precio_producto

    def get_cantidad(self):
        return self.cantidad
