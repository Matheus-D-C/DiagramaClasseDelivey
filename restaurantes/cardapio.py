from typing import List
from produto import Produto

class Cardapio:
    produtos: List[Produto]

    def __init__(self, id_cardapio: int, nome: str) -> None:
        self._id = id_cardapio
        self._nome = nome
        self.produtos = []

    def cadastrar_produto(self, nome: str, preco: float, descricao: str) -> Produto:  
        novo_produto = Produto(id_produto=1, nome=nome, preco=preco, descricao=descricao)
        self.produtos.append(novo_produto)
        return novo_produto

    def listar_produtos(self) -> str:
        return ""