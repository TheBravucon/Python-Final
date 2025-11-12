from tkinter import Label
from typing import Callable

from ui.base.button import Button

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}


class Table:
    def __init__(self, ventana, columns, data, editar: Callable[[int], None], borrar: Callable[[int], None]):
        self.__ventana = ventana
        self.__columns = columns
        self.__data = data
        self.__editar = editar
        self.__borrar = borrar

        self.validar_datos()
        self.mostrar_columnas()
        self.mostrar_datos()

    def validar_datos(self):
        if len(self.__data) > 0 and len(self.__data[0]) - 1 != len(self.__columns):
            raise Exception("La cantidad de columnas de la tabla difiere de la cantidad de columnas en los datos")

    def mostrar_columnas(self):
        i = 0
        for column in self.__columns:
            label = Label(self.__ventana.get_ventana(), text=column, **input_config, bd=2, relief='raised', width=30)
            label.grid(row=0, column=i, sticky='ew')
            i += 1

    def mostrar_datos(self):
        for i in range(0, len(self.__data)):
            for j in range(len(self.__columns)):
                column_label = Label(self.__ventana.get_ventana(), text=self.__data[i][j + 1], **input_config, bd=2,
                                     relief='raised', width=30)
                column_label.grid(row=i + 1, column=j, sticky='ew')

            id = int(self.__data[i][0])
            boton_editar = Button(self.__ventana, text='Editar', command=lambda id=id: self.__editar(id),
                                  grid=[i + 1, len(self.__columns) + 1])
            boton_borrar = Button(self.__ventana, text='Borrar', command=lambda id=id: self.__borrar(id),
                                  grid=[i + 1, len(self.__columns) + 2])
