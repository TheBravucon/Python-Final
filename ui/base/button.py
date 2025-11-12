import tkinter as tk
from typing import Callable

from ui.base.frame import Frame


class Button:
    def __init__(self, frame: Frame, label: str, command: Callable, grid: list[int] = None) -> None:
        self.ventana = frame.get_ventana()
        self.button = tk.Button(self.ventana, text=label, command=command)
        if not callable(command):
            raise Exception("Command must be a function")
        if grid is None:
            self.button.pack(fill="x", expand=False)
            return

        if len(grid) != 2:
            raise Exception("Grid must have 2 values")
        self.button.grid(row=grid[0], column=grid[1])
