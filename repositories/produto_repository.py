from models.produto import Produto
from config.database import conectar


class ProdutoRepository:

    def cadastrar(self, produto):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.callproc("cadastrar_produto", (produto.nome, produto.preco, produto.quantidade, produto.categoria_id))
        
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return True

    def editar(self, produto):

        conexao = conectar()
        cursor = conexao.cursor()

        sql = "UPDATE produto SET nome = %s, preco = %s, quantidade = %s, categoria_id = %s WHERE id = %s"

        valores = (produto.nome, produto.preco, produto.quantidade, produto.categoria_id, produto.id)

        cursor.execute(sql, valores)

        conexao.commit()

        quantidade_alterada = cursor.rowcount

        cursor.close()
        conexao.close()

        return quantidade_alterada > 0
    
    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()       

        cursor.execute("SELECT * FROM produto")
        dados = cursor.fetchall()
        
        cursor.close()
        conexao.close()

        produtos = []

        for dado in dados:
            produtos.append(Produto(dado[0], dado[1], dado[2], dado[3], dado[4]))

        return produtos

    def buscar(self, nome):
        
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM produto WHERE nome LIKE %s"
        valores = (f"%{nome}%",)

        cursor.execute(sql, valores)

        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        produtos = []

        for dado in dados:
            produtos.append(Produto(dado[0], dado[1], dado[2], dado[3], dado[4]))
            
        return produtos
    
    def busca_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM produto WHERE id=%s"
        valores = (id,)
        cursor.execute(sql, valores)

        dado = cursor.fetchone()

        conexao.close()
        cursor.close()

        if dado is None:
            return None

        return Produto(dado[0], dado[1])  

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM produto WHERE id = %s"
        cursor.execute(sql, (id,))

        quantidade_excluida = cursor.rowcount

        conexao.commit()

        cursor.close()
        conexao.close()

        return quantidade_excluida > 0

    def contar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT COUNT(*) FROM produto")
        
        quantidade = cursor.fetchone()[0]
        
        cursor.close()
        conexao.close()

        return quantidade