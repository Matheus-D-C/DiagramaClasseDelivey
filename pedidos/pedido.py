from typing import List, Optional
from item_pedido import ItemPedido
from entregas.entrega import Entrega

class Pedido:

    def __init__(self, id_pedido: int, data_hora: str, status: str) -> None:
        self._id = id_pedido
        self._data_hora = data_hora
        self._status = status
        self.itens = []
        self.entrega: Optional[Entrega] = None 


    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.itens)

    def processar_pagamento(self, pedido_id: int, pagamento) -> bool:
        return True

    def adicionar_item(self, item: ItemPedido) -> None:
        self.itens.append(item)