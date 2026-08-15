from models.produto import Produto
from repositories.produto_repository import ProdutoRepository


class ProdutoController:
    
    def __init__(self):
        self.repository = ProdutoRepository()

    def cadastrar(self, nome, preco, quantidade, categoria_id):
        produto = Produto(None, nome, preco, quantidade, categoria_id)
        return self.repository.cadastrar(produto)
        
    def editar(self, id, nome, preco, quantidade, categoria_id):
        produto = Produto(id, nome, preco, quantidade, categoria_id)
        return self.repository.editar(produto)
    
    def excluir(self, id):
        return self.repository.excluir(id)
    
    def listar(self):
        return self.repository.listar()
    
    def buscar(self, nome):
        return self.repository.buscar(nome)
    
    def busca_por_id(self,id): 
        return self.repository.busca_por_id(id)
    
    def contar(self):
        return self.repository.contar()