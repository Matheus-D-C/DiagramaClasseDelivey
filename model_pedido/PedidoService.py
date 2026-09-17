from typing import Optional
from datetime import datetime
from Pedido import Pedido
from ItemPedido import ItemPedido
from model_restaurante.Produto import Produto
from model_pagamento.AbstractPagamento import AbstractPagamento

class PedidoService:
    def criarPedido(self, id: int = 1) -> Pedido:
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Pedido(id_pedido=id, data_hora=data_hora_atual, status="CRIADO")

    def adicionarItemProduto(self, pedido: Pedido, p: Produto, q: int) -> None:
        item = ItemPedido(quantidade=q, preco_unitario=p.preco, produto=p)
        pedido.adicionarItem(item)
        print(f"Adicionado {q}x '{p.nome}' ao Pedido ID {pedido.id}.")

    def finalizarPedido(self, pedido: Pedido, pagamento: AbstractPagamento) -> None:
        sucesso = pedido.processarPagamento(pedido.id, pagamento)
        if sucesso:
            print(f"Pedido {pedido.id} finalizado e pago com sucesso!")
        else:
            print(f"Falha ao processar pagamento do pedido {pedido.id}.")

    def cancelarPedido(self, pedido: Pedido) -> bool:
        pedido.status = "CANCELADO"
        print(f"Pedido {pedido.id} foi cancelado.")
        return True

    def statusDoPedido(self, pedido: Pedido) -> str:
        return pedido.status