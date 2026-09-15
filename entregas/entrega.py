from typing import Optional
from entregador import Entregador
class Entrega: 
    def __init__(self, id_entrega: int, status_entrega: str, valor_frete: float, entregador: Optional[Entregador] = None):
        self._id = id_entrega
        self._status_entrega = status_entrega
        self._valor_frete = valor_frete
        self._entregador = entregador

    def calcular_frete(self, origem: str, destion: str) -> float:
        return self._valor_frete