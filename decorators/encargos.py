from decorators.interface import CalculadoraMensalidade

class MensalidadeBase(CalculadoraMensalidade):
    def __init__(self, valor_bruto, desconto_strategy):
        self.valor_bruto = valor_bruto
        self.strategy = desconto_strategy
    
    def get_valor_final(self) -> float:
        desconto = self.strategy.calcular_desconto(self.valor_bruto)
        return self.valor_bruto - desconto

    def get_descricao(self) -> str:
        return f"Mensalidade Base (R$ {self.valor_bruto})"

class MensalidadeDecorator(CalculadoraMensalidade):
    def __init__(self, wrapped: CalculadoraMensalidade):
        self.wrapped = wrapped

    def get_valor_final(self) -> float:
        return self.wrapped.get_valor_final()

    def get_descricao(self) -> str:
        return self.wrapped.get_descricao()

class MultaAtraso(MensalidadeDecorator):
    def get_valor_final(self) -> float:
        return self.wrapped.get_valor_final() + 50.00 # R$ 50 fixo

    def get_descricao(self) -> str:
        return f"{self.wrapped.get_descricao()} + Multa(50.00)"

class JurosMoratorios(MensalidadeDecorator):
    def get_valor_final(self) -> float:
        base = self.wrapped.get_valor_final()
        return base * 1.02 # +2% juros

    def get_descricao(self) -> str:
        return f"{self.wrapped.get_descricao()} + Juros(2%)"