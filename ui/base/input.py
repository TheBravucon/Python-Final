import tkinter as tk
from typing import List


class Input:
    def __init__(self, frame: tk.Frame, text: str, text_variable, grid: List[int], padding: List[int]):
        if len(grid) != 4:
            raise Exception("Grid debe tener 4 valores")
        if len(padding) != 4:
            raise Exception("Padding debe tener 4 valores")

        self.__ventana = frame
        self.__label = tk.Label(self.__ventana, text=text)
        self.__label.grid(row=grid[0], column=grid[1], padx=padding[0], pady=padding[1])
        self.__entry = tk.Entry(self.__ventana, textvariable=text_variable)
        self.__entry.grid(row=grid[2], column=grid[3], padx=padding[2], pady=padding[3])
