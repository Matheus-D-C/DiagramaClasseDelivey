from typing import Optional
from model_cliente.Cliente import Cliente

class ControladorCliente:

    def __init__(self) -> None:
        self.__clienteAtual: Optional[Cliente] = None

    def cadastrar_cliente(self, nome: str, email: str, cpf: str) -> Cliente:
        self.__clienteAtual = Cliente(cliente_id=1, nome = nome, email=email, cpf=cpf)
        return self.__clienteAtual

    def validar_cliente(self) -> bool:    
        if self.__clienteAtual and len(self.__clienteAtual.cpf) == 11:
            return True
        return False
