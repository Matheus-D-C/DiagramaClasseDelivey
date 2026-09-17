from AbstractPagamento import AbstractPagamento

class Pix(AbstractPagamento):
    def __init__(self, id_pagamento: int, valor: float,status: str ,chave_pix: str = "", qr_code: str = ""):
        super().__init__( id_pagamento, valor, status)
        self.__chavePix = chave_pix
        self.__qrCode = qr_code

    @property
    def chavePix(self) -> str:
        return self.__chavePix

    @property
    def qrCode(self) -> str:
        return self.__qrCode

    def gerarChavePix(self) -> bool:
        return len(self.__chavePix) > 0

    def gerarQrCode(self) -> bool:
        return len(self.__qrCode) > 0

    def processar(self, valor: float) -> bool:
        if valor > 0 and self.gerarQrCode():
            self._status = "PAGO"
            return True
        return False