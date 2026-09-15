from datetime import datetime
from typing import Optional

class AvaliacaoProduto:
    def __init__(self, id_avaliacao: int, nota: int, comentario: str, data_de_avaliacao: Optional[datetime] = None) -> None:
        self._id = id
        self._nota = nota
        self._comentario = comentario
        self._data_de_avaliacao = data_de_avaliacao or datetime.now()

    def validar_nota(self) -> bool:
        return 1 <= self._nota <= 5

    def editar_comentario(self, novo_comentario: str) -> None:
        self._comentario = novo_comentario
        