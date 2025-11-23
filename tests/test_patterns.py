import unittest
from strategies.descontos import BolsaMerito, SemDesconto
from decorators.encargos import MensalidadeBase, MultaAtraso, JurosMoratorios
from infra.config import SystemConfig

class TestDesignPatterns(unittest.TestCase):

    def test_strategy_desconto(self):
        """Prova que trocar a Strategy muda o valor final"""
        base_valor = 1000.0
        
        # Sem Desconto
        calculo_normal = MensalidadeBase(base_valor, SemDesconto())
        self.assertEqual(calculo_normal.get_valor_final(), 1000.0)

        # Com Bolsa Mérito (20%)
        calculo_bolsa = MensalidadeBase(base_valor, BolsaMerito(0.20))
        self.assertEqual(calculo_bolsa.get_valor_final(), 800.0)

    def test_decorator_encargos(self):
        """Prova a composição de Decorators (Multa + Juros)"""
        base = MensalidadeBase(1000.0, SemDesconto()) # 1000
        
        com_multa = MultaAtraso(base) # 1000 + 50 = 1050
        self.assertEqual(com_multa.get_valor_final(), 1050.0)

        com_juros = JurosMoratorios(com_multa) # 1050 * 1.02 = 1071
        self.assertEqual(com_juros.get_valor_final(), 1071.0)

    def test_singleton_unicidade(self):
        """Prova que o Singleton retorna a mesma instância"""
        s1 = SystemConfig()
        s2 = SystemConfig()
        self.assertIs(s1, s2)
        s1.school_name = "Nova Escola"
        self.assertEqual(s2.school_name, "Nova Escola")

if __name__ == '__main__':
    unittest.main()