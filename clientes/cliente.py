from typing import List,Any
from endereco import Endereco
from avaliacoes.avaliacao_produto import AvaliacaoProduto

class Cliente:

    def __init__(self, cliente_id: int, nome: str, email: str, cpf: str) -> None:
        self._id = cliente_id
        self._nome = nome
        self._email = email
        self._cpf = cpf
        self.enderecos: List[Endereco] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email

    @property
    def cpf(self) -> str:
        return self._cpf

    def adicionar_endereco(self, e: Endereco) -> None:
        self.enderecos.append(e)

    def remover_endereco(self, e: Endereco) -> None:
        """Remove um endereço da lista do cliente, se existir."""
        if e in self.enderecos:
            self.enderecos.remove(e)

    def fazer_avaliacao(self, a: AvaliacaoProduto) -> None:
        print(f"Cliente {self._nome} avaliou com nota {a._nota}: {a._comentario}")
        