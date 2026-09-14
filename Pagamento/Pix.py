from IPagamento import Pagamento

class Pix(Pagamento):
    def __init__(self, id_pagamento: int, valor: float, chave_pix: str = "", qr_code: str = ""):
        self._id = id_pagamento
        self._valor = valor
        self._status = "PENDENTE"
        self._chavePix = chave_pix
        self._qrCode = qr_code

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
    def chavePix(self) -> str:
        return self._chavePix

    @property
    def qrCode(self) -> str:
        return self._qrCode

    def gerarChavePix(self) -> bool:
        if not self._chavePix:
            self._chavePix = f"pix-key-{self._id}@banco.com"
            return True
        return False

    def gerarQrCode(self) -> bool:
        if self._chavePix:
            self._qrCode = f"00020126360014BR.GOV.BCB.PIX0114{self._chavePix}"
            return True
        return False

    def processar(self) -> bool:
        if self._chavePix and self._qrCode:
            self._status = "PAGO"
            return True
        self._status = "FALHA"
        return False