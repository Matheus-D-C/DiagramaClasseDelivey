class Endereco:

    def __init__(self, rua: str, numero: str, bairro: str, cep: str) -> None:
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cep = cep

    @property
    def rua(self) -> str:
        return self._rua

    @property
    def numero(self) -> str:
        return self._numero

    @property
    def bairro(self) -> str:
        return self._bairro

    @property
    def cep(self) -> str:
        return self._cep

    def validar_cep(self) -> bool:
        """Valida se o CEP possui exatamente 8 dígitos numéricos"""
        cep_limpo = self._cep.replace("-","").strip()
        return len(cep_limpo) == 8 and cep_limpo.isdigit()