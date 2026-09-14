from IPagamento import Pagamento

class CartaoDebito(Pagamento):
    def __init__(self, id_pagamento: int, valor: float, numero_cartao: str, nome_titular: str):
        self._id = id_pagamento
        self._valor = valor
        self._status = "PENDENTE"
        self._numeroCartao = numero_cartao
        self._nomeTitular = nome_titular

    @property
    def id(self) -> int:
        return self._id

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def status(self) -> str:
        return self._status

    @property
    def numeroCartao(self) -> str:
        return self._numeroCartao

    @property
    def nomeTitular(self) -> str:
        return self._nomeTitular

    def validarCartao(self) -> bool:
        
        return len(self._numeroCartao.replace(" ", "")) == 16 and len(self._nomeTitular) > 0

    def processar(self) -> bool:
        if self.validarCartao():
            self._status = "DEBITADO"
            return True
        self._status = "FALHA_DEBITO"
        return False