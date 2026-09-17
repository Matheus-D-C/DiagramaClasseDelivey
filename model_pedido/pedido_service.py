from typing import Optional
from pedido import Pedido
from model_restaurante.produto import Produto

class PedidoService:
    def criar_pedido(self) -> Optional[Pedido]:
        pass

    def adicionar_item_produto(self, id_produto: int, p: Produto, q: int) -> None:
        pass

    def finalizar_pedido(self, pagamento) -> None:
        pass

    def cancelar_pedido(self, id_produto: int) -> bool:
        return True

    def status_do_pedido(self) -> str:
        return ""