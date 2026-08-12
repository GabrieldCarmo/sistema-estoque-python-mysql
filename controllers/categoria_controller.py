from models.categoria import Categoria
from database.connection import conectar

class CategoriaController:

    def cadastrar(self, nome):
        categoria = Categoria(None, nome)
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.callproc("cadastrar_categoria", (categoria.nome))
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()           
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        produtos = []
        for dado in dados:
            produto = Produto(dado[0], dado[1], dado[2], dado[3], dado[4]
            )
        produtos.append(produto)
        return produtos

    def buscar(self, id):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM categoria WHERE id=%s"
        valores = (id,)
        cursor.execute(sql, valores)
        dado = cursor.fetchone()
        conexao.close()
        cursor.close()
        if dado is None:
            return None
        categoria = Categoria(dado[0], dado[1])
        return categoria

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM categoria WHERE id=%s"
        valores = (id,)
        cursor.execute(sql,valores)
        conexao.commit()
        conexao.close()
        cursor.close()
