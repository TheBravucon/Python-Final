from ui.base.frame import Frame
from ui.base.table import Table

COLUMNS = ['Producto', 'Precio', 'Cantidad']

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}
bg = 'green'
title = 'Gestor de productos'
icon = 'icon.ico'
geometry = '1600x900'
config = {'bg': 'green'}


class VentanaListaProductos:
    def __init__(self, product_service):
        self.__ventana = Frame(input_config=input_config, bg=bg, title=title, icon=icon, geometry=geometry,
                               config=config)
        self.__product_service = product_service
        self.__table = Table(self.__ventana, COLUMNS, self.obtener_productos(), self.editar_producto,
                             self.borrar_producto)

    def obtener_productos(self):
        return self.__product_service.obtener_productos()

    def editar_producto(self, id):
        self.__product_service.editar_producto(id)

    def borrar_producto(self, id):
        self.__product_service.borrar_producto(id)
