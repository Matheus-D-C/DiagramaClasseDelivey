from typing import Optional
from Endereco import Endereco
from model_restaurante.AvaliacaoProduto import AvaliacaoProduto

class Cliente:

    def __init__(self, cliente_id: int, nome: str, email: str, cpf: str) -> None:
        self.__id = cliente_id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__endereco: Optional[Endereco] = None
        self.__avaliacoes = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property 
    def enderecos(self) -> Optional[Endereco]:
        return self.__endereco

    def adicionarEndereco(self, e: Endereco) -> None:
        if self.__endereco is not None:
            raise ValueError(
                "O cliente já possui um endereço cadastrado!"
                "Remove o endereço atual antes de adicionar um novo"
            )
        self.__endereco = e
        print(f"Endereço adicionado com sucesso para {self.__nome}.")

    def removerEndereco(self) -> None:
        if self.__endereco is None:
            print("Não há endereço para remover.")
        else:
            self.__endereco = None
            print("Endereço Antigo removido com sucesso")

    def fazer_avaliacao(self, a: AvaliacaoProduto) -> None:
        if a.validar_nota():
            self.__avaliacoes.append(a)
            print(f"Cliente {self.__nome} avaliou com nota {a.__nota}: {a.__comentario}.")
        else:
            print("Avaliação inválida. A nota deve ser entre 1 e 5.")
        