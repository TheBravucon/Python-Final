from ui.base.frame import Frame

input_config = {'padx': 5, 'pady': 5, 'bg': 'lightgray', 'font': ('Arial', 10)}
bg = 'green'
title = 'Gestor de productos'
icon = 'icon.ico'
geometry = '1600x900'
config = {'bg': 'green'}


class VentanaCreacion:
    def __init__(self):
        self.__ventana = Frame(input_config=input_config, bg=bg, title=title, icon=icon, geometry=geometry,
                               config=config)
