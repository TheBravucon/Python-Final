import tkinter as tk

from ui.base.button import Button
from ui.base.frame import Frame

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}
bg = 'green'
title = 'Gestor de productos'
icon = 'icon.ico'
geometry = '1600x900'
config = {'bg': 'green'}


class VentanaPrincipal:
    def __init__(self, init_service):
        self.__popup: tk.Frame | None = None
        self.__ventana = Frame(input_config=input_config, bg=bg, title=title, icon=icon, geometry=geometry,
                               config=config)
        self.__service = init_service
        self.__crear_producto_button = Button(self.get_ventana(), 'Crear Producto', self.__service.open_products_window)
        self.__mostrar_productos_button = Button(self.get_ventana(), 'Mostrar todos los productos',
                                                 self.__service.open_all_products_window)
        self.__mostrar_carrito_button = Button(self.get_ventana(), 'Comprar productos', self.__service.open_carrito_window)

    def open_popup(self, popup):
        self.__popup = popup

    def close_popup(self):
        self.__popup.destroy()

    def get_ventana(self):
        return self.__ventana

    def ejecutar(self):
        self.__ventana.ejecutar()
