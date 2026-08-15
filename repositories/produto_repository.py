from models.produto import Produto
from config.database import conectar


class CategoriaRepository:

    def cadastrar(self, categoria):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.callproc("cadastrar_produto", (produto.nome, produto.preco, produto.quantidade, produto.categoria_id))
        
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return True