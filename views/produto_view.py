import customtkinter as ctk
from tkinter import messagebox


class ProdutoView:

    def __init__(self, parent, controller, categoria_controller):

        self.controller = controller
        self.categoria_controller = categoria_controller

        self.frame = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.categorias = []

        self.criar_interface()

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self.frame,
            text="Produtos",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )

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
            text="Editar",
            command=self.editar
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

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar
        ).pack(
            side="left",
            padx=10
        )

        # Área onde os formulários aparecem

        self.formulario = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
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

    # ==================================================
    # UTILITÁRIOS
    # ==================================================

    def limpar_formulario(self):

        for widget in self.formulario.winfo_children():
            widget.destroy()

    def carregar_categorias(self):

        self.categorias = self.categoria_controller.listar()

        return [
            categoria.nome
            for categoria in self.categorias
        ]

    def obter_categoria_id(self, nome):

        for categoria in self.categorias:

            if categoria.nome == nome:
                return categoria.id

        return None

    def atualizar_lista(self, produtos):

        self.lista.configure(
            state="normal"
        )

        self.lista.delete(
            "1.0",
            "end"
        )

        if not produtos:

            self.lista.insert(
                "end",
                "Nenhum produto encontrado."
            )

        else:

            for produto in produtos:

                self.lista.insert(
                    "end",
                    f"ID: {produto.id}\n"
                    f"Nome: {produto.nome}\n"
                    f"Preço: R$ {produto.preco:.2f}\n"
                    f"Quantidade: {produto.quantidade}\n"
                    f"Categoria ID: {produto.categoria_id}\n"
                    f"{'-' * 50}\n"
                )

        self.lista.configure(
            state="disabled"
        )

    # ==================================================
    # LISTAR
    # ==================================================

    def listar(self):

        try:

            produtos = self.controller.listar()

            self.atualizar_lista(produtos)

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar os produtos.\n\n{erro}"
            )

    # ==================================================
    # CADASTRAR
    # ==================================================

    def cadastrar(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Cadastrar Produto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        entrada_nome = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nome do produto"
        )

        entrada_nome.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        entrada_preco = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Preço"
        )

        entrada_preco.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        entrada_quantidade = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Quantidade"
        )

        entrada_quantidade.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        categorias = self.carregar_categorias()

        if not categorias:

            ctk.CTkLabel(
                self.formulario,
                text="Nenhuma categoria cadastrada.",
                text_color="orange"
            ).pack(
                anchor="w",
                padx=20,
                pady=10
            )

            return

        categoria_var = ctk.StringVar(
            value="Selecione uma categoria"
        )

        combo_categoria = ctk.CTkComboBox(
            self.formulario,
            width=350,
            values=categorias,
            variable=categoria_var
        )

        combo_categoria.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        def salvar():

            nome = entrada_nome.get().strip()
            preco_texto = entrada_preco.get().strip()
            quantidade_texto = entrada_quantidade.get().strip()

            if not nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o nome do produto."
                )

                return

            try:

                preco = float(
                    preco_texto.replace(",", ".")
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Informe um preço válido."
                )

                return

            try:

                quantidade = int(
                    quantidade_texto
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Informe uma quantidade válida."
                )

                return

            categoria_id = self.obter_categoria_id(
                categoria_var.get()
            )

            if categoria_id is None:

                messagebox.showwarning(
                    "Atenção",
                    "Selecione uma categoria."
                )

                return

            try:

                resultado = self.controller.cadastrar(
                    nome,
                    preco,
                    quantidade,
                    categoria_id
                )

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Produto cadastrado com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível cadastrar o produto.\n\n{erro}"
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

    # ==================================================
    # BUSCAR POR NOME
    # ==================================================

    def buscar(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Buscar Produto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        entrada = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nome do produto"
        )

        entrada.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        def realizar_busca():

            nome = entrada.get().strip()

            if not nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o nome do produto."
                )

                return

            try:

                produtos = self.controller.buscar(nome)

                self.atualizar_lista(produtos)

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

    # ==================================================
    # EDITAR
    # ==================================================

    def editar(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Editar Produto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        entrada_id = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="ID do produto"
        )

        entrada_id.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        entrada_nome = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nome"
        )

        entrada_nome.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        entrada_preco = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Preço"
        )

        entrada_preco.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        entrada_quantidade = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Quantidade"
        )

        entrada_quantidade.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        categorias = self.carregar_categorias()

        categoria_var = ctk.StringVar(
            value="Selecione uma categoria"
        )

        combo_categoria = ctk.CTkComboBox(
            self.formulario,
            width=350,
            values=categorias,
            variable=categoria_var
        )

        combo_categoria.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        def salvar():

            try:

                id_produto = int(
                    entrada_id.get().strip()
                )

                preco = float(
                    entrada_preco.get()
                    .strip()
                    .replace(",", ".")
                )

                quantidade = int(
                    entrada_quantidade.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Confira os valores informados."
                )

                return

            nome = entrada_nome.get().strip()

            if not nome:

                messagebox.showwarning(
                    "Atenção",
                    "Informe o nome do produto."
                )

                return

            categoria_id = self.obter_categoria_id(
                categoria_var.get()
            )

            if categoria_id is None:

                messagebox.showwarning(
                    "Atenção",
                    "Selecione uma categoria."
                )

                return

            try:

                resultado = self.controller.editar(
                    id_produto,
                    nome,
                    preco,
                    quantidade,
                    categoria_id
                )

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Produto atualizado com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

                else:

                    messagebox.showwarning(
                        "Atenção",
                        "Produto não encontrado."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível editar o produto.\n\n{erro}"
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

    # ==================================================
    # EXCLUIR
    # ==================================================

    def excluir(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Excluir Produto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        entrada_id = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="ID do produto"
        )

        entrada_id.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        def realizar_exclusao():

            try:

                id_produto = int(
                    entrada_id.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            try:

                produto = self.controller.buscar_por_id(
                    id_produto
                )

                if produto is None:

                    messagebox.showwarning(
                        "Não encontrado",
                        "Produto não encontrado."
                    )

                    return

                confirmar = messagebox.askyesno(
                    "Confirmar exclusão",
                    f"Tem certeza que deseja excluir?\n\n"
                    f"ID: {produto.id}\n"
                    f"Nome: {produto.nome}"
                )

                if not confirmar:
                    return

                resultado = self.controller.excluir(
                    id_produto
                )

                if resultado:

                    messagebox.showinfo(
                        "Sucesso",
                        "Produto excluído com sucesso!"
                    )

                    self.limpar_formulario()
                    self.listar()

                else:

                    messagebox.showwarning(
                        "Atenção",
                        "Produto não encontrado."
                    )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível excluir o produto.\n\n{erro}"
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