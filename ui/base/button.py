import tkinter as tk
from typing import Callable

from ui.base.frame import Frame


class Button:
    def __init__(self, frame: Frame, text: str, command: Callable, grid: list[int] = None) -> None:
        self.ventana = frame.get_ventana()
        self.button = tk.Button(self.ventana, text=text, command=command, bg='lightgray', font=('Arial', 10), bd=2,
                                relief='raised', width=30, padx=5, pady=2)
        if not callable(command):
            raise Exception("Command must be a function")
        if grid is None:
            self.button.pack(fill="x", expand=False)
            return

        if len(grid) != 2:
            raise Exception("Grid must have 2 values")
        self.button.grid(row=grid[0], column=grid[1])
