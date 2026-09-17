from typing import List, Optional
from ItemPedido import ItemPedido
from model_cliente.Cliente import Cliente
from model_entrega.Entrega import Entrega
from model_pagamento.AbstractPagamento import AbstractPagamento

class Pedido:

    def __init__(self, id_pedido: int, data_hora: str,cliente: Optional[Cliente] = None, status: str = "PENDENTE") -> None:
        self.__id = id_pedido
        self.__data_hora = data_hora
        self.__status = status
        self.__cliente = cliente
        self.__entrega = None 
        self.__itens: List[ItemPedido] = []

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def data_hora(self) -> str:
        return self.__data_hora
    
    @property
    def status(self) -> str:
        return self.__status
    
    @status.setter
    def status(self, novo_status: str) -> None:
        self.__status = novo_status
    
    @property
    def cliente(self) -> Optional[Cliente]:
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        self.__cliente = cliente
    
    @property
    def entrega(self):
        return self.__entrega
    
    @entrega.setter
    def entrega(self, entrega) -> None:
        self.__entrega = entrega
    
    @property
    def itens(self) -> List[ItemPedido]:
        return self.__itens

    def adicionarItem(self, item: ItemPedido) -> None:
        self.__itens.append(item)

    def calcularTotal(self) -> float:
        return sum(item.calcular_subtotal() for item in self.itens)

    def processarPagamento(self, pedido_id: int, pagamento) -> bool:
        if self.__id == pedido_id and pagamento.processar(self.calcularTotal()):
            self.__status = "PAGO"
            return True
        return False
