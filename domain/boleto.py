from observers.interface import Subject
from strategies.interface import DescontoStrategy
from decorators.encargos import MensalidadeBase, MultaAtraso, JurosMoratorios

class GeradorBoleto(Subject):
    def __init__(self):
        super().__init__()

    def processar_mensalidade(self, valor_bruto: float, strategy: DescontoStrategy, atrasado: bool):
        # 1. Cria o componente base com a Strategy escolhida
        calculo = MensalidadeBase(valor_bruto, strategy)
        
        # 2. Se estiver atrasado, aplica Decorators dinamicamente
        if atrasado:
            calculo = MultaAtraso(calculo)      # Adiciona multa fixa
            calculo = JurosMoratorios(calculo)  # Adiciona juros sobre o total

        valor_final = calculo.get_valor_final()
        desc = calculo.get_descricao()

        # 3. Notifica Observers
        self.notify_observers(f"Boleto gerado. Detalhes: {desc}. Total: R$ {valor_final:.2f}")
        
        return valor_final