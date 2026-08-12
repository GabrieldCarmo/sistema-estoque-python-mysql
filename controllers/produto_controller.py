from models.produto import Produto
from database.connection import conectar

class ProdutoController:

    def cadastrar(self, nome, preco, quantidade, categoria_id):
        produto = Produto(None, nome, preco, quantidade, categoria_id)
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.callproc("cadastrar_produto", (produto.nome, produto.preco, produto.quantidade, produto.categoria_id,))
        conexao.commit()
        cursor.close()
        conexao.close()
        