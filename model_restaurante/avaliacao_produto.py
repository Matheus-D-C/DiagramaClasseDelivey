from datetime import datetime
from typing import Optional

class AvaliacaoProduto:
    def __init__(self, id_avaliacao: int, nota: int, comentario: str, data_de_avaliacao: Optional[datetime] = None):
        self.__id = id_avaliacao
        self.__nota = nota
        self.__comentario = comentario
        self.__data_de_avaliacao = data_de_avaliacao or datetime.now()

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nota(self) -> int:
        return self.__nota
    
    @property
    def comentario(self) -> str:
        return self.__comentario
    
    @property
    def data_de_avaliacao(self) -> datetime:
        return self.__data_de_avaliacao

    def validar_nota(self) -> bool:
        return 1 <= self.__nota <= 5

    def editar_comentario(self, novo_comentario: str) -> None:
        self._comentario = novo_comentario
        