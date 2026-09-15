from typing import List, Optional
from cliente import Cliente
from endereco import Endereco

class ControladorCliente:

    def __init__(self) -> None:
        self.clientes: List[Cliente] = []
        self._proximo_id = 1

    def cadastrar_cliente(self, nome: str, email: str, cpf: str) -> Cliente:

        novo_cliente = Cliente(self._proximo_id, nome, email, cpf)
        self.clientes.append(novo_cliente)
        self._proximo_id += 1
        return novo_cliente

    def adicionar_endereco(self, cliente_id: int, e: Endereco) -> None:

        cliente = self._buscar_por_id(cliente_id)
        if cliente:
            cliente.adicionar_endereco(e)

    def validar_cliente(self, cliente_id: Optional[int] = None) -> bool:

        if cliente_id is not None:
            cliente = self._buscar_por_id(cliente_id)
            return cliente is not None and len(cliente.enderecos) > 0
        return True

    def _buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:

        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None