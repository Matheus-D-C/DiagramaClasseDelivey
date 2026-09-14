from abc import ABC, abstractmethod

class Pagamento(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @abstractmethod
    def processar(self) -> bool:
        pass