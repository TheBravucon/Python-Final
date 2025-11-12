import tkinter as tk
from tkinter import messagebox

from db.queries import *
from ui.ventana_lista_productos import VentanaListaProductos
from ui.ventana_productos import VentanaProductos, get_nombre_producto, get_precio_producto, get_cantidad


class ProductService:
    def __init__(self, db):
        self.__db = db
        self.ventana_productos = None
        self.ventana_lista_productos = None
        self.editing = False

    def open_ventana_productos(self):
        self.ventana_productos = VentanaProductos(self)
        return self.ventana_productos

    def open_ventana_lista_productos(self):
        self.ventana_lista_productos = VentanaListaProductos(self)
        return self.ventana_lista_productos

    def crear_producto(self):
        name_product = self.ventana_productos.get_nombre_producto()
        amount_product = self.ventana_productos.get_precio_producto()
        price_product = self.ventana_productos.get_cantidad()

        if name_product == "" or amount_product == 0.0 or price_product == 0.0:
            print("Error: Todos los campos son obligatorios.")
            return

        if self.editing:
            id_producto = self.ventana_productos.get_id_producto().get()
            self.__db.execute(ACTUALIZAR_PRODUCTOS, (name_product, price_product, amount_product, id_producto))

        else:
            self.__db.execute(CREAR_PRODUCTOS, (name_product, price_product, amount_product))

        action = 'editado' if self.editing else 'creado'
        tk.messagebox.showinfo(title=f"Producto {action}", message=f"El producto fue {action} con exito")
        self.reset_form()

    def reset_form(self):
        self.ventana_productos.get_nombre_producto().set("")
        self.ventana_productos.get_precio_producto().set(0.0)
        self.ventana_productos.get_cantidad().set(0)
        self.editing = False

    def obtener_productos(self):
        self.__db.get_conexion()
        return self.__db.fetch_many(BUSCAR_TODOS_PRODUCTOS)
