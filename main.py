import tkinter as tk

from controllers.categoria_controller import CategoriaController
from views.menu_view import MenuView


root = tk.Tk()

categoria_controller = CategoriaController()

MenuView(
    root,
    categoria_controller
)

root.mainloop()