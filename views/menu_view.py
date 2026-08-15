import customtkinter as ctk
from views.categoria_view import CategoriaView
from views.produto_view import ProdutoView


class MenuView:

    def __init__(self, root, categoria_controller, produto_controller):
        self.root = root
        self.categoria_controller = categoria_controller
        self.produto_controller = produto_controller

        self.configurar_janela()
        self.criar_interface()

    def configurar_janela(self):

        self.root.title("Sistema de Estoque")
        self.root.geometry("1000x600")
        self.root.minsize(900, 550)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def criar_interface(self):

        # Sidebar

        self.sidebar = ctk.CTkFrame(
            self.root,
            width=210,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="ESTOQUE",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=(40, 40))

        self.criar_botao_menu(
            "Dashboard",
            self.abrir_dashboard
        )

        self.criar_botao_menu(
            "Categorias",
            self.abrir_categorias
        )

        self.criar_botao_menu(
            "Produtos",
            self.abrir_produtos
        )

        self.criar_botao_menu(
            "Estoque",
            self.abrir_estoque
        )

        self.criar_botao_menu(
            "Movimentações",
            self.abrir_movimentacoes
        )

        self.criar_botao_menu(
            "Relatórios",
            self.abrir_relatorios
        )

        botao_sair = ctk.CTkButton(
            self.sidebar,
            text="Sair",
            height=40,
            fg_color="transparent",
            border_width=1,
            command=self.root.destroy
        )

        botao_sair.pack(
            side="bottom",
            padx=20,
            pady=30,
            fill="x"
        )

        # Conteúdo

        self.conteudo = ctk.CTkFrame(
            self.root,
            corner_radius=0
        )

        self.conteudo.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.abrir_dashboard()

    def criar_botao_menu(self, texto, comando):

        botao = ctk.CTkButton(
            self.sidebar,
            text=texto,
            height=40,
            command=comando
        )

        botao.pack(
            padx=20,
            pady=6,
            fill="x"
        )

    def limpar_conteudo(self):

        for widget in self.conteudo.winfo_children():
            widget.destroy()

    # Dashboard

    def abrir_dashboard(self):

        self.limpar_conteudo()

        titulo = ctk.CTkLabel(
            self.conteudo,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=40,
            pady=(40, 5)
        )

        subtitulo = ctk.CTkLabel(
            self.conteudo,
            text="Visão geral do seu estoque",
            font=("Arial", 15)
        )

        subtitulo.pack(
            anchor="w",
            padx=40
        )

        cards = ctk.CTkFrame(
            self.conteudo,
            fg_color="transparent"
        )

        cards.pack(
            fill="x",
            padx=30,
            pady=40
        )
        
        quantidade_categorias = self.categoria_controller.contar()
        
        self.criar_card(
            cards,
            "Produtos",
            "0",
            0
        )

        self.criar_card(
            cards,
            "Categorias",
            quantidade_categorias,
            1
        )

        self.criar_card(
            cards,
            "Estoque baixo",
            "0",
            2
        )

    def criar_card(self, parent, titulo, valor, coluna):

        card = ctk.CTkFrame(
            parent,
            height=120
        )

        card.grid(
            row=0,
            column=coluna,
            padx=10,
            sticky="nsew"
        )

        parent.grid_columnconfigure(
            coluna,
            weight=1
        )

        ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 14)
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            card,
            text=valor,
            font=("Arial", 28, "bold")
        ).pack()

    # Categorias

    def abrir_categorias(self):

        self.limpar_conteudo()

        CategoriaView(
            self.conteudo,
            self.categoria_controller
        )

    # Outras

    def abrir_produtos(self):

        self.limpar_conteudo()

        ProdutoView(
            self.conteudo,
            self.categoria_controller,
            self.produto_controller
        )

    def abrir_estoque(self):

        self.limpar_conteudo()

        ctk.CTkLabel(
            self.conteudo,
            text="Estoque",
            font=("Arial", 28, "bold")
        ).pack(pady=40)

    def abrir_movimentacoes(self):

        self.limpar_conteudo()

        ctk.CTkLabel(
            self.conteudo,
            text="Movimentações",
            font=("Arial", 28, "bold")
        ).pack(pady=40)

    def abrir_relatorios(self):

        self.limpar_conteudo()

        ctk.CTkLabel(
            self.conteudo,
            text="Relatórios",
            font=("Arial", 28, "bold")
        ).pack(pady=40)