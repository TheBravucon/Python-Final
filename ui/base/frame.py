import tkinter as tk

class Frame:
    def __init__(self):
        self.__font = 'Arial'
        self.__input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': (self.__font, 10)}
        self.__root_bg = 'green'
        self.__ventana = tk.Tk()
        self.__ventana.title('Gestor de productos')
        self.__ventana.geometry('1600x900')
        self.__ventana.iconbitmap('icon.ico')
        self.__ventana.config(bg=self.__root_bg)
        self.__frame = tk.Frame(self.__ventana, bg='White')

    def get_ventana(self):
        return self.__ventana

    def ejecutar(self):
        self.__ventana.mainloop()