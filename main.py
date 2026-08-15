import customtkinter as ctk

from controllers.categoria_controller import CategoriaController
from views.menu_view import MenuView


root = ctk.CTk()

categoria_controller = CategoriaController()

MenuView(
    root,
    categoria_controller
)

root.mainloop()