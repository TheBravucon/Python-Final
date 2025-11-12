from tkinter import Label


class Table:
    def __init__(self, ventana, columns):
        self.__ventana = ventana
        i = 0
        for column in columns:
            label = Label(self.__ventana, text=column, bd=2, relief='raised', width=30)
            label.grid(row=0, column=i, sticky='ew')
            i += 1