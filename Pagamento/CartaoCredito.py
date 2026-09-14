from IPagamento import Pagamento

class CartaoCredito(Pagamento):
    def __init__(self, id_pagamento: int, valor: float, numero_cartao: str, validade: str):
        self._id = id_pagamento
        self._valor = valor
        self._status = "PENDENTE"
        self._numeroCartao = numero_cartao
        self._validade = validade

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
    def validade(self) -> str:
        return self._validade

    def validarCartao(self) -> bool:
        
        return len(self._numeroCartao.replace(" ", "")) == 16 and "/" in self._validade

    def processar(self) -> bool:
        if self.validarCartao():
            self._status = "APROVADO"
            return True
        self._status = "RECUSADO"
        return False