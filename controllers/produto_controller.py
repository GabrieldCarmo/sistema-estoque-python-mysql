from models.produto import Produto
from repositories.categoria_repository import ProdutoRepository

class ProdutoController:

    def cadastrar(self, nome, preco, quantidade, categoria_id):
        produto = Produto(None, nome, preco, quantidade, categoria_id)
        return self.repository
        