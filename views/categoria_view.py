import customtkinter as ctk
from tkinter import messagebox


class CategoriaView:

    def __init__(self, parent, controller):

        self.controller = controller

        self.frame = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.criar_interface()

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self.frame,
            text="Categorias",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )

        # Botões

        botoes = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        botoes.pack(
            fill="x",
            padx=40
        )

        ctk.CTkButton(
            botoes,
            text="Cadastrar",
            command=self.cadastrar
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Buscar",
            command=self.buscar
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            botoes,
            text="Excluir",
            command=self.excluir
        ).pack(
            side="left",
            padx=10
        )

        # Lista

        self.lista = ctk.CTkTextbox(
            self.frame,
            font=("Arial", 14)
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        self.lista.configure(
            state="disabled"
        )

        self.listar()

    # Cadastrar

    def cadastrar(self):

        janela = ctk.CTkToplevel(self.frame)

        janela.title("Cadastrar Categoria")
        janela.geometry("400x250")
        janela.resizable(False, False)

        ctk.CTkLabel(
            janela,
            text="Nova Categoria",
            font=("Arial", 22, "bold")
        ).pack(pady=(30, 20))

        entrada = ctk.CTkEntry(
            janela,
            width=300,
            placeholder_text="Nome da categoria"
        )

        entrada.pack(pady=10)

        entrada.focus()

        def salvar():

            nome = entrada.get().strip()

            if not nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o nome da categoria.",
                    parent=janela
                )

                return

            try:

                resultado = self.controller.cadastrar(nome)

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Categoria cadastrada com sucesso!",
                        parent=janela
                    )

                    janela.destroy()
                    self.listar()

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível cadastrar.\n\n{erro}",
                    parent=janela
                )

        ctk.CTkButton(
            janela,
            text="Salvar",
            width=300,
            height=40,
            command=salvar
        ).pack(pady=20)

    # Listar

    def listar(self):

        try:

            categorias = self.controller.listar()

            self.lista.configure(
                state="normal"
            )

            self.lista.delete(
                "1.0",
                "end"
            )

            if not categorias:

                self.lista.insert(
                    "end",
                    "Nenhuma categoria cadastrada."
                )

            else:

                for categoria in categorias:

                    self.lista.insert(
                        "end",
                        f"ID: {categoria.id}    |    "
                        f"Nome: {categoria.nome}\n"
                    )

            self.lista.configure(
                state="disabled"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar as categorias.\n\n{erro}",
                parent=self.frame
            )

    # Buscar

    def buscar(self):

        janela = ctk.CTkToplevel(self.frame)

        janela.title("Buscar Categoria")
        janela.geometry("400x230")
        janela.resizable(False, False)

        ctk.CTkLabel(
            janela,
            text="Buscar Categoria",
            font=("Arial", 22, "bold")
        ).pack(pady=(30, 20))

        entrada = ctk.CTkEntry(
            janela,
            width=300,
            placeholder_text="ID da categoria"
        )

        entrada.pack(pady=10)

        def realizar_busca():

            try:

                id_categoria = int(
                    entrada.get()
                )

                categoria = self.controller.buscar(
                    id_categoria
                )

                if categoria:

                    messagebox.showinfo(
                        "Categoria encontrada",
                        f"ID: {categoria.id}\n"
                        f"Nome: {categoria.nome}",
                        parent=janela
                    )

                else:

                    messagebox.showwarning(
                        "Não encontrada",
                        "Categoria não encontrada.",
                        parent=janela
                    )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido.",
                    parent=janela
                )

        ctk.CTkButton(
            janela,
            text="Buscar",
            width=300,
            command=realizar_busca
        ).pack(pady=20)

    # Editar

    def editar(self):

        messagebox.showinfo(
            "Em desenvolvimento",
            "A função de editar ainda será implementada.",
            parent=self.frame
        )

    # Excluir

    def excluir(self):

        messagebox.showinfo(
            "Em desenvolvimento",
            "A função de excluir ainda será implementada.",
            parent=self.frame
        )