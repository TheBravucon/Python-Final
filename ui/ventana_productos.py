from ui.base.button import *
from ui.base.frame import Frame
from ui.form.productos_form import ProductosForm

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}
bg = 'green'
title = 'Gestor de productos'
icon = 'icon.ico'
geometry = '1600x900'
config = {'bg': 'green'}


class VentanaProductos:
    def __init__(self, product_service):
        self.__ventana = Frame(input_config=input_config, bg=bg, title=title, icon=icon, geometry=geometry,
                               config=config)
        self.product_service = product_service
        self.form = ProductosForm(self.__ventana.get_ventana())
        self.button = Button(self.__ventana, 'Crear producto', self.product_service.crear_producto, [3, 0])

    def get_nombre_producto(self):
        return self.form.get_nombre_producto()

    def get_precio_producto(self):
        return self.form.get_precio_producto()

    def get_cantidad(self):
        return self.form.get_cantidad()
