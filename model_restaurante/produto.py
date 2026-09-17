class Produto:
    def __init__(self, id_produto: int, nome: str, preco: float, descricao: str = "") -> None:
        self._id = id_produto
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def alterar_preco(self, preco: float) -> None:
        self._preco = preco

    def atualizar_descricao(self, descricao: str) -> None:
        self._descricao = descricao