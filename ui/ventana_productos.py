from ui.base.button import *
from ui.base.frame import Frame
from ui.base.input import *


def get_nombre_producto():
    return VentanaProductos.nombre_producto


def get_precio_producto():
    return VentanaProductos.precio_producto


def get_cantidad():
    return VentanaProductos.cantidad

def initialize_variables():
    VentanaProductos.nombre_producto = tk.StringVar()
    VentanaProductos.precio_producto = tk.DoubleVar()
    VentanaProductos.cantidad = tk.IntVar()


class VentanaProductos:
    id_producto = None
    nombre_producto = None
    precio_producto = None
    cantidad = None

    def __init__(self, product_service):
        initialize_variables()
        self.__ventana = Frame()
        self.product_service = product_service
        self.input1 = Input(self.__ventana, 'Nombre de producto', [0, 0, 0, 1], [5, 5, 5, 5])
        self.input2 = Input(self.__ventana, 'Precio', [1, 0, 1, 1], [5, 5, 5, 5])
        self.input3 = Input(self.__ventana, 'Cantidad', [2, 0, 2, 1], [5, 5, 5, 5])
        self.button = Button(self.__ventana, 'Crear producto', self.product_service.crear_producto, [3, 0])

    def get_ventana(self):
        return self.__ventana

    def get_nombre_producto(self):
        return get_var_value()

    def get_precio_producto(self):
        return get_var_value()

    def get_cantidad(self):
        return get_var_value()
