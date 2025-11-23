import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.descontos import BolsaMerito, SemDesconto
from observers.notifiers import EmailNotifier, SistemaLogNotifier
from domain.boleto import GeradorBoleto
from infra.config import SystemConfig

def main():
    config = SystemConfig()
    print(f"--- Sistema {config.school_name} ---")
    
    # Setup
    gerador = GeradorBoleto()
    gerador.add_observer(SistemaLogNotifier())
    gerador.add_observer(EmailNotifier("pais_do_anderson@email.com"))

    while True:
        print("\n1. Gerar Boleto Normal (Sem Desconto)")
        print("2. Gerar Boleto Aluno Mérito (20% off)")
        print("3. Gerar Boleto com Atraso (Multa + Juros)")
        print("0. Sair")
        op = input("Opção: ")

        if op == '1':
            gerador.processar_mensalidade(1000.0, SemDesconto(), atrasado=False)
        elif op == '2':
            gerador.processar_mensalidade(1000.0, BolsaMerito(), atrasado=False)
        elif op == '3':
            # Exemplo de integração: Mérito mas pagou atrasado
            gerador.processar_mensalidade(1000.0, BolsaMerito(), atrasado=True)
        elif op == '0':
            break
    
    print("\n------------------------------------------------")
    print("Desenvolvido por: Anderson Nilton de Souza")
    print("------------------------------------------------")

if __name__ == "__main__":
    main()