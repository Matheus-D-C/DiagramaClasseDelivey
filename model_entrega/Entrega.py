from sre_compile import dis
from typing import Optional
from Entregador import Entregador

class Entrega: 
    def __init__(self, id_entrega: int, status_entrega: str, valor_frete: float, entregador: Optional[Entregador] = None, pedido = None):
        self.__id = id_entrega
        self.__statusEntrega = status_entrega
        self.__valorFrete = valor_frete
        self.__entregador = entregador
        self.__pedido = pedido

    @property
    def id(self) -> int:
        return self.__id

    @property
    def statusEntrega(self) -> str:
        return self.__statusEntrega

    @statusEntrega.setter
    def statusEntrega(self, novo_status: str) -> None:
        self.__statusEntrega = novo_status

    @property
    def valorFrete(self) -> float:
        return self.__valorFrete

    @valorFrete.setter
    def valorFrete(self, novoValor: float):
        self.__valorFrete = novoValor

    @property
    def entregador(self) -> Optional[Entregador]:
        return self.__entregador

    @entregador.setter
    def entregador(self, novo_entregador: Entregador) -> Optional[Entregador]:
        self.__entregador = novo_entregador

    @property
    def pedido(self):
        return self.__pedido

    @pedido.setter
    def pedido(self, pedido) -> None:
        self.__pedido = pedido


    def calcular_frete(self, origem: str, destino: str) -> float:
        distancia_estimada = len(origem) + len(destino)
        self.__valorFrete = distancia_estimada * 1.5
        return self.__valorFrete