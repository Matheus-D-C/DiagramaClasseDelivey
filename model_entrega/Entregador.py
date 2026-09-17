class Entregador:
    def __init__(self, id_entregador: int, nome: str, veiculo: str):
        self.__id = id_entregador
        self.__nome = nome
        self.__veiculo = veiculo

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def veiculo(self) -> str:
        return self.__veiculo

    def atualizar_veiculo(self, veiculo: str) -> None:
        self._veiculo = veiculo
        
        