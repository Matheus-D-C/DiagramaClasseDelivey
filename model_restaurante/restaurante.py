from typing import List
from Cardapio import Cardapio

class Restaurante:
    def __init__(self, id_restaurante: int, nome: str, cnpj: str) -> None:
        self.__id = id_restaurante
        self.__nome = nome
        self.__cnpj = cnpj
        self.__cardapios: List[Cardapio] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def cardapios(self) -> List[Cardapio]:
        return self.__cardapios

    def adicionarCardapio(self, cardapio: Cardapio) -> None:
        self.__cardapios.append(cardapio)
        