from AbstractPagamento import AbstractPagamento

class CartaoDebito(AbstractPagamento):
    def __init__(self, id_pagamento: int, valor: float,status: str, numero_cartao: str, nome_titular: str):
        super().__init__(id_pagamento, valor, status)
        self.__numeroCartao = numero_cartao
        self.__nomeTitular = nome_titular

    @property
    def numeroCartao(self) -> str:
        return self.__numeroCartao

    @property
    def nomeTitular(self) -> str:
        return self.__nomeTitular

    def validarCartao(self) -> bool:
        
        return len(self.__numeroCartao.replace(" ", "")) == 16 and len(self.__nomeTitular) > 0

    def processar(self, valor: float) -> bool:
        if valor > 0 and self.validarCartao():
            self._status = "Aprovado no Débito"
            return True
        return False