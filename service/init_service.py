from db.db import db
from service.product_service import ProductService
from ui.ventana_principal import VentanaPrincipal


class InitService:
    def __init__(self):
        self.__ventana_principal = VentanaPrincipal(self)
        self.__product_service = ProductService(db)
        self.__ventana_principal.ejecutar()

    def get_ventana_principal(self):
        return self.__ventana_principal

    def open_products_window(self):
        self.__ventana_principal.open_popup(self.__product_service.open_ventana_productos())

    def open_all_products_window(self):
        self.__ventana_principal.open_popup(self.__product_service.open_ventana_lista_productos())

    def open_carrito_window(self):
        self.__ventana_principal.open_popup(self.__product_service.open_ventana_carrito())
