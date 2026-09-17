from typing import List
from Produto import Produto

class Cardapio:

    def __init__(self, id_cardapio: int, nome: str) -> None:
        self.__id = id_cardapio
        self.__nome = nome
        self.__produtos: List[Produto] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def produtos(self) -> List[Produto]:
        return self.__produtos

    def cadastrar_produto(self, nome: str, preco: float, descricao: str) -> Produto:  
        novo_id = len(self.__produtos) + 1
        p = Produto(id_produto=novo_id, nome=nome, preco=preco)
        p.atualizarDescricao(descricao)
        self.__produtos.append(p)
        return p

    def listar_produtos(self) -> str:
        if not self.__produtos:
            return "Nenhum produto cadastrado."
        return "\n".join([f"ID: {p.id} | {p.nome} - R$ {p.preco:.2}" for p in self.__produtos])