import tkinter as tk
from tkinter import messagebox


class CategoriaView:

    def __init__(self, root, controller):

        self.controller = controller

        self.janela = tk.Toplevel(root)
        self.janela.title("Categorias")
        self.janela.geometry("500x400")

        self.criar_interface()

    def criar_interface(self):

        tk.Label(
            self.janela,
            text="Categorias",
            font=("Arial", 18)
        ).pack(pady=20)

        tk.Button(
            self.janela,
            text="Cadastrar",
            width=20,
            command=self.cadastrar
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Listar",
            width=20,
            command=self.listar
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Buscar",
            width=20,
            command=self.buscar
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Editar",
            width=20,
            command=self.editar
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Excluir",
            width=20,
            command=self.excluir
        ).pack(pady=5)

    def cadastrar(self):

        janela = tk.Toplevel(self.janela)
        janela.title("Cadastrar Categoria")

        tk.Label(
            janela,
            text="Nome:"
        ).pack(pady=10)

        entrada = tk.Entry(janela)
        entrada.pack()

        def salvar():

            nome = entrada.get()

            resultado = self.controller.cadastrar(nome)

            if resultado:
                messagebox.showinfo(
                    "Sucesso",
                    "Categoria cadastrada!"
                )

                janela.destroy()

            else:
                messagebox.showerror(
                    "Erro",
                    "Não foi possível cadastrar."
                )

        tk.Button(
            janela,
            text="Salvar",
            command=salvar
        ).pack(pady=15)

    def listar(self):

        categorias = self.controller.listar()

        janela = tk.Toplevel(self.janela)
        janela.title("Categorias cadastradas")
        janela.geometry("400x300")

        lista = tk.Listbox(
            janela,
            width=50
        )

        lista.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        for categoria in categorias:

            lista.insert(
                tk.END,
                f"{categoria.id} - {categoria.nome}"
            )