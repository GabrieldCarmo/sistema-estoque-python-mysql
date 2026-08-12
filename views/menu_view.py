import tkinter as tk
from views.categoria_view import CategoriaView


class MenuView:

    def __init__(self, root, categoria_controller):
        self.root = root
        self.categoria_controller = categoria_controller

        self.root.title("Sistema de Estoque")
        self.root.geometry("500x400")

        self.criar_interface()

    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="Sistema de Estoque",
            font=("Arial", 20)
        )
        titulo.pack(pady=30)

        botao_categoria = tk.Button(
            self.root,
            text="Categorias",
            width=20,
            command=self.abrir_categorias
        )
        botao_categoria.pack(pady=10)

        botao_produto = tk.Button(
            self.root,
            text="Produtos",
            width=20
        )
        botao_produto.pack(pady=10)

        botao_sair = tk.Button(
            self.root,
            text="Sair",
            width=20,
            command=self.root.destroy
        )
        botao_sair.pack(pady=10)

    def abrir_categorias(self):
        CategoriaView(
            self.root,
            self.categoria_controller
        )