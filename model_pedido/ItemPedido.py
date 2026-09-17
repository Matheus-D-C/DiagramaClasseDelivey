from model_restaurante.Produto import Produto

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int, preco_unitario: float) -> None:
        self.__produto = produto
        self.__quantidade = quantidade
        self.__precoUnitario = preco_unitario

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @property
    def precoUnitario(self) -> float:
        return self.__precoUnitario


    def calcular_subtotal(self) -> float:
        return self.__quantidade * self.__precoUnitario