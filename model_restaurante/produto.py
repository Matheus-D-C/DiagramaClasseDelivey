from typing import List
from AvaliacaoProduto import AvaliacaoProduto

class Produto:
    def __init__(self, id_produto: int, nome: str, preco: float) -> None:
        self.__id = id_produto
        self.__nome = nome
        self.__preco = preco

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    def alterarPreco(self, preco: float) -> None:
        self.__preco = preco

    def atualizarDescricao(self, descricao: str) -> None:
        self.__descricao = descricao