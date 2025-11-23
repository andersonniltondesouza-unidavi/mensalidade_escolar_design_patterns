from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular_desconto(self, valor_bruto: float) -> float:
        pass