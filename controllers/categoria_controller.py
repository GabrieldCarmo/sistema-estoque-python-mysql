from models.categoria import Categoria
from repositories.categoria_repository import CategoriaRepository


class CategoriaController:

    def __init__(self):
        self.repository = CategoriaRepository()

    def cadastrar(self, nome):
        categoria = Categoria(None, nome)
        return self.repository.cadastrar(categoria)

    def listar(self):
        return self.repository.listar()

    def buscar(self, id):
        return self.repository.buscar(id)

    def excluir(self, id):
        return self.repository.excluir(id)