from typing import Optional
from cardapio import Cardapio

class Restaurante:
    def __init__(self, id_restaurante: int, nome: str, cnpj: str) -> None:
        self._id = id_restaurante
        self._nome = nome
        self._cnpj = cnpj
        self._cardapio: Optional[Cardapio] = None