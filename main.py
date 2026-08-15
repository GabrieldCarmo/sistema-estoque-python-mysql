import tkinter as tk

from controllers.categoria_controller import CategoriaController
from controllers.produto_controller import ProdutoController
from views.menu_view import MenuView


root = tk.Tk()

produto_controller = ProdutoController()
categoria_controller = CategoriaController()

MenuView(
    root,
    categoria_controller,
    produto_controller
)

root.mainloop()