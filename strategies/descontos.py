from strategies.interface import DescontoStrategy

class SemDesconto(DescontoStrategy):
    def calcular_desconto(self, valor_bruto: float) -> float:
        return 0.0

class BolsaMerito(DescontoStrategy):
    def __init__(self, porcentagem=0.20):
        self.porcentagem = porcentagem

    def calcular_desconto(self, valor_bruto: float) -> float:
        return valor_bruto * self.porcentagem

class DescontoIrmaos(DescontoStrategy):
    def calcular_desconto(self, valor_bruto: float) -> float:
        return valor_bruto * 0.10  # 10% fixo para irmãos