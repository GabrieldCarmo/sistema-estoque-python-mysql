import customtkinter as ctk
from tkinter import messagebox


class ProdutoView:

    def __init__(
        self,
        parent,
        controller,
        categoria_controller
    ):

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

        # Guarda as categorias para transformar
        # "Eletrônicos" -> ID 1, por exemplo.
        self.categorias = []

        self.criar_interface()

    def criar_interface(self):

        # =========================
        # TÍTULO
        # =========================

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

        # =========================
        # BOTÕES
        # =========================

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
            text="Editar",
            command=self.mostrar_edicao
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

        # =========================
        # FORMULÁRIO
        # =========================

        self.formulario = ctk.CTkFrame(
            self.frame
        )

        self.formulario.pack(
            fill="x",
            padx=40,
            pady=20
        )

        # =========================
        # LISTA
        # =========================

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
    # LIMPAR FORMULÁRIO
    # ==================================================

    def limpar_formulario(self):

        for widget in self.formulario.winfo_children():
            widget.destroy()

    # ==================================================
    # CARREGAR CATEGORIAS
    # ==================================================

    def carregar_categorias(self):

        self.categorias = self.categoria_controller.listar()

        nomes = [
            categoria.nome
            for categoria in self.categorias
        ]

        return nomes

    # ==================================================
    # ENCONTRAR ID DA CATEGORIA
    # ==================================================

    def encontrar_categoria_id(self, nome):

        for categoria in self.categorias:

            if categoria.nome == nome:
                return categoria.id

        return None

    # ==================================================
    # CADASTRAR
    # ==================================================

    def mostrar_cadastro(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Cadastrar Produto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        # Nome

        entrada_nome = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nome do produto"
        )

        entrada_nome.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        # Preço

        entrada_preco = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Preço"
        )

        entrada_preco.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        # Quantidade

        entrada_quantidade = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Quantidade"
        )

        entrada_quantidade.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        # Categoria

        nomes_categorias = self.carregar_categorias()

        if not nomes_categorias:

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

        categoria_selecionada = ctk.StringVar(
            value="Selecione uma categoria"
        )

        combo_categoria = ctk.CTkComboBox(
            self.formulario,
            width=350,
            variable=categoria_selecionada,
            values=nomes_categorias
        )

        combo_categoria.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        # =========================
        # BOTÕES
        # =========================

        botoes = ctk.CTkFrame(
            self.formulario,
            fg_color="transparent"
        )

        botoes.pack(
            anchor="w",
            padx=20,
            pady=(10, 15)
        )

        def salvar():

            nome = entrada_nome.get().strip()
            preco_texto = entrada_preco.get().strip()
            quantidade_texto = entrada_quantidade.get().strip()
            categoria_nome = categoria_selecionada.get()

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

            categoria_id = self.encontrar_categoria_id(
                categoria_nome
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

                else:

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível cadastrar o produto."
                    )

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
    # LISTAR
    # ==================================================

    def listar(self):

        try:

            produtos = self.controller.listar()

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
                    "Nenhum produto cadastrado."
                )

            else:

                self.lista.insert(
                    "end",
                    "ID        NOME                         "
                    "PREÇO       QTD       CATEGORIA\n"
                )

                self.lista.insert(
                    "end",
                    "-" * 90 + "\n"
                )

                for produto in produtos:

                    self.lista.insert(
                        "end",
                        f"{produto.id:<10}"
                        f"{produto.nome:<30}"
                        f"R$ {produto.preco:<10}"
                        f"{produto.quantidade:<10}"
                        f"{produto.categoria_id}\n"
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
                f"Não foi possível carregar os produtos.\n\n{erro}"
            )

    # ==================================================
    # BUSCAR
    # ==================================================

    def mostrar_busca(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Buscar Produto",
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
            placeholder_text="ID do produto"
        )

        entrada.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

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

                id_produto = int(
                    entrada.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            try:

                produto = self.controller.buscar(
                    id_produto
                )

                if produto:

                    self.mostrar_resultado_busca(
                        produto
                    )

                else:

                    messagebox.showwarning(
                        "Não encontrado",
                        "Produto não encontrado."
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

    # ==================================================
    # RESULTADO BUSCA
    # ==================================================

    def mostrar_resultado_busca(self, produto):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Produto encontrado",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"ID: {produto.id}"
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"Nome: {produto.nome}"
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"Preço: R$ {produto.preco}"
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"Quantidade: {produto.quantidade}"
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

        ctk.CTkLabel(
            self.formulario,
            text=f"Categoria ID: {produto.categoria_id}"
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

    # ==================================================
    # EDITAR
    # ==================================================

    def mostrar_edicao(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Editar Produto",
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
            placeholder_text="ID do produto"
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

        entrada_preco = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Novo preço"
        )

        entrada_preco.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        entrada_quantidade = ctk.CTkEntry(
            self.formulario,
            width=350,
            placeholder_text="Nova quantidade"
        )

        entrada_quantidade.pack(
            padx=20,
            pady=5,
            anchor="w"
        )

        nomes_categorias = self.carregar_categorias()

        categoria_selecionada = ctk.StringVar()

        combo_categoria = ctk.CTkComboBox(
            self.formulario,
            width=350,
            variable=categoria_selecionada,
            values=nomes_categorias
        )

        combo_categoria.pack(
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

            categoria_id = self.encontrar_categoria_id(
                categoria_selecionada.get()
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

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível atualizar o produto."
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

    # ==================================================
    # EXCLUIR
    # ==================================================

    def mostrar_exclusao(self):

        self.limpar_formulario()

        titulo = ctk.CTkLabel(
            self.formulario,
            text="Excluir Produto",
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
            placeholder_text="ID do produto"
        )

        entrada.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

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

                id_produto = int(
                    entrada.get().strip()
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um ID válido."
                )

                return

            try:

                produto = self.controller.buscar(
                    id_produto
                )

                if not produto:

                    messagebox.showwarning(
                        "Não encontrado",
                        "Produto não encontrado."
                    )

                    return

                confirmar = messagebox.askyesno(
                    "Confirmar exclusão",
                    f"Tem certeza que deseja excluir:\n\n"
                    f"ID: {produto.id}\n"
                    f"Nome: {produto.nome}?"
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

                    messagebox.showerror(
                        "Erro",
                        "Não foi possível excluir o produto."
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