from models.categoria import Categoria
from config.database import conectar

class CategoriaController:

    def cadastrar(self, nome):
        categoria = Categoria(None, nome)
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.callproc("cadastrar_categoria", (categoria.nome,))
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
        
    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()           
        cursor.execute("SELECT * FROM categoria")
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        categorias = []
        for dado in dados:
            categoria = Categoria(dado[0], dado[1])
            categorias.append(categoria)
        return categorias

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
