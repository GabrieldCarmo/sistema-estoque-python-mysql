from models.categoria import Categoria
from config.database import conectar


class CategoriaRepository:

    def cadastrar(self, categoria):
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
            categorias.append(Categoria(dado[0], dado[1]))

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

        return Categoria(dado[0], dado[1])  

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM categoria WHERE id=%s"
        valores = (id,)
        cursor.execute(sql,valores)

        conexao.commit()

        cursor.close()
        conexao.close()
