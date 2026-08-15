class Produto:

    def __init__(
        self,
        id,
        nome,
        preco,
        quantidade,
        categoria_id
    ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria_id = categoria_id