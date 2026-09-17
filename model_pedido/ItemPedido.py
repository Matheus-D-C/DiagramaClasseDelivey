from model_restaurante.produto import Produto

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int, preco_unitario: float) -> None:
        self.produto = produto
        self._quantidade = quantidade
        self._preco_unitario = preco_unitario

    def calcular_subtotal(self) -> float:
        return self._quantidade * self._preco_unitario