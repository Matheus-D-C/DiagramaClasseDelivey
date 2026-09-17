from AbstractPagamento import AbstractPagamento

class CartaoCredito(AbstractPagamento):
    def __init__(self, id_pagamento: int, valor: float,status: str, numero_cartao: str, validade: str):
        super().__init__(id_pagamento, valor, status)
        self.__numeroCartao = numero_cartao
        self.__validade = validade

    @property
    def numeroCartao(self) -> str:
        return self.__numeroCartao

    @property
    def validade(self) -> str:
        return self.__validade

    def validarCartao(self) -> bool:
        return len(self.__numeroCartao.replace(" ", "")) == 16 and len(self.__validade) == 5

    def processar(self, valor: float) -> bool:
        if valor > 0 and self.validarCartao:
            self._status = "APROVADO"
            return True
        return False