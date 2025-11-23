from abc import ABC, abstractmethod

class CalculadoraMensalidade(ABC):
    @abstractmethod
    def get_valor_final(self) -> float:
        pass

    @abstractmethod
    def get_descricao(self) -> str:
        pass