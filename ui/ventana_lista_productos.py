from ui.base.frame import Frame
from ui.base.table import Table

COLUMNS = ['Producto', 'Precio', 'Cantidad', 'La concha de tu madre']


class VentanaListaProductos:
    def __init__(self, product_service):
        self.__ventana = Frame()
        self.__product_service = product_service
        self.__table = Table(self.__ventana.get_ventana(), COLUMNS)

    def get_ventana(self):
        return self.__ventana
