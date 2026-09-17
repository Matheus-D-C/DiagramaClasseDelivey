from abc import ABC, abstractmethod

class AbstractPagamento(ABC):

    def __init__(self, id: int, valor: float, status: str) -> None:
        self.__id = id
        self.__valor = valor
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, novo_status: str):
        self.__status = novo_status

    @abstractmethod
    def processar(self, valor: float) -> bool:
        pass