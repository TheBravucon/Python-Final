from ui.base.button import Button
from ui.base.frame import Frame
from service.excel_service import crear_ticket

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}
bg = 'green'
title = 'Gestor de productos'
icon = 'icon.ico'
geometry = '1600x900'
config = {'bg': 'green'}


class VentanaCarrito:
    def __init__(self, product_service):
        self.__ventana = Frame(input_config=input_config, bg=bg, title=title, icon=icon, geometry=geometry,
                               config=config)
        self.product_service = product_service
        self.productos = self.obtener_productos()
        self.button = Button(self.__ventana, 'Generar ticket', lambda: crear_ticket(self.productos), [3, 0])

    def obtener_productos(self):
        return self.product_service.obtener_productos()
