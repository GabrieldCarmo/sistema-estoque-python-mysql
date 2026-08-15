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

        # Titulo

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

        # Buttons

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
            command=self.mostrar_cadastro
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Buscar",
            command=self.mostrar_busca
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            botoes,
            text="Excluir",
            command=self.mostrar_exclusao
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar
        ).pack(
            side="left",
            padx=10
        )

        # Formulario

        self.formulario = ctk.CTkFrame(
            self.frame
        )

        self.formulario.pack(
            fill="x",
            padx=40,
            pady=20
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
            pady=(0, 30)
        )

        self.lista.configure(
            state="disabled"
        )

        self.listar()

    # Formulario

    def limpar_formulario(self):

        for widget in self.formulario.winfo_children():
            widget.destroy()

    # Cadastrar

    def mostrar_cadastro(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Cadastrar Categoria",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        entrada = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nome da categoria"
        )

        entrada.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

        entrada.focus()

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        def salvar():

            nome = entrada.get().strip()

            if not nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o nome da categoria."
                )

                return

            try:

                resultado = self.controller.cadastrar(nome)

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Categoria cadastrada com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

                else:

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível cadastrar a categoria."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível cadastrar a categoria.\n\n{erro}"
                )

        ctk.CTkButton(
            botoes,
            text="Salvar",
            width=120,
            command=salvar
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            width=120,
            fg_color="gray",
            command=self.limpar_formulario
        ).pack(
            side="left"
        )

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

                self.lista.insert(
                    "end",
                    "ID        NOME\n"
                )

                self.lista.insert(
                    "end",
                    "-" * 50 + "\n"
                )

                for categoria in categorias:

                    self.lista.insert(
                        "end",
                        f"{categoria.id:<10}"
                        f"{categoria.nome}\n"
                    )

            self.lista.configure(
                state="disabled"
            )

        except Exception as erro:

            self.lista.configure(
                state="disabled"
            )

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar as categorias.\n\n{erro}"
            )

    # Buscar

    def mostrar_busca(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Buscar Categoria",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        entrada = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="ID da categoria"
        )

        entrada.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

        entrada.focus()

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        def realizar_busca():

            try:

                id_categoria = int(
                    entrada.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            try:

                categoria = self.controller.buscar(
                    id_categoria
                )

                if categoria:

                    self.mostrar_resultado_busca(
                        categoria
                    )

                else:

                    messagebox.showwarning(
                        "Não encontrada",
                        "Não existe uma categoria com esse ID."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível realizar a busca.\n\n{erro}"
                )

        ctk.CTkButton(
            botoes,
            text="Buscar",
            width=120,
            command=realizar_busca
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            width=120,
            fg_color="gray",
            command=self.limpar_formulario
        ).pack(
            side="left"
        )

    # Resultado
    

    def mostrar_resultado_busca(self, categoria):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Categoria encontrada",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"ID: {categoria.id}",
            font=("Arial", 14)
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"Nome: {categoria.nome}",
            font=("Arial", 14)
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkButton(
            self.formulario,
            text="Fechar",
            width=120,
            command=self.limpar_formulario
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

    # Excluir
    
    def mostrar_exclusao(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Excluir Categoria",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        entrada = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="ID da categoria"
        )

        entrada.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

        entrada.focus()

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        def realizar_exclusao():

            try:

                id_categoria = int(
                    entrada.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            try:

                categoria = self.controller.buscar(
                    id_categoria
                )

                if not categoria:

                    messagebox.showwarning(
                        "Não encontrada",
                        "Não existe uma categoria com esse ID."
                    )

                    return

                confirmar = messagebox.askyesno(
                    "Confirmar exclusão",
                    f"Tem certeza que deseja excluir:\n\n"
                    f"ID: {categoria.id}\n"
                    f"Nome: {categoria.nome}?"
                )

                if not confirmar:
                    return

                resultado = self.controller.excluir(
                    id_categoria
                )

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Categoria excluída com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

                else:

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível excluir a categoria."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível excluir a categoria.\n\n{erro}"
                )

        ctk.CTkButton(
            botoes,
            text="Excluir",
            width=120,
            fg_color="#c62828",
            hover_color="#8e0000",
            command=realizar_exclusao
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            width=120,
            fg_color="gray",
            command=self.limpar_formulario
        ).pack(
            side="left"
        )

    # Editar

    def mostrar_edicao(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Editar Categoria",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        entrada_id = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="ID da categoria"
        )

        entrada_id.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        entrada_nome = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Novo nome"
        )

        entrada_nome.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        def realizar_edicao():

            try:

                id_categoria = int(
                    entrada_id.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            novo_nome = entrada_nome.get().strip()

            if not novo_nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o novo nome da categoria."
                )

                return

            try:

                categoria = self.controller.buscar(
                    id_categoria
                )

                if not categoria:

                    messagebox.showwarning(
                        "Não encontrada",
                        "Não existe uma categoria com esse ID."
                    )

                    return

                # A edição será implementada no Controller
                resultado = self.controller.editar(
                    id_categoria,
                    novo_nome
                )

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Categoria atualizada com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

                else:

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível atualizar a categoria."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível editar a categoria.\n\n{erro}"
                )

        ctk.CTkButton(
            botoes,
            text="Salvar",
            width=120,
            command=realizar_edicao
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            width=120,
            fg_color="gray",
            command=self.limpar_formulario
        ).pack(
            side="left"
        )