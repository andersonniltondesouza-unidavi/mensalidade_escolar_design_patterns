# Trabalho 04 - Design Patterns com OO (Sistema de Mensalidade Escolar)

Este projeto é uma aplicação desenvolvida em **Python**, como parte dos requisitos da disciplina de Linguagens de Programação e Paradigmas. O objetivo principal é demonstrar a aplicação prática de **Design Patterns** (Strategy, Decorator, Observer e Singleton) para resolver problemas de extensibilidade e manutenção em um domínio de negócio (cobrança escolar). O sistema replica a lógica de emissão de boletos, permitindo a troca dinâmica de regras de desconto, a aplicação acumulativa de encargos (multas/juros) e notificações desacopladas.

**Desenvolvido por:**

* Anderson Nilton de Souza [@andersonniltondesouza-unidavi](https://github.com/andersonniltondesouza-unidavi)

## 📂 Arquitetura do Projeto

A aplicação é modularizada para separar as responsabilidades, seguindo uma estrutura que reflete os papéis dos padrões implementados:

```text
mensalidade_escolar/
├── app/
│   └── main.py           # Ponto de entrada, menu CLI e injeção de dependências
├── domain/
│   └── boleto.py         # Contexto do domínio (Subject) e Regras de Negócio
├── strategies/
│   ├── interface.py      # Interface Strategy (DescontoStrategy)
│   └── descontos.py      # Implementações Concretas (Bolsa, Pontualidade, etc.)
├── decorators/
│   ├── interface.py      # Component e Decorator Abstrato
│   └── encargos.py       # Decorators Concretos (Multa, Juros)
├── observers/
│   ├── interface.py      # Interfaces Subject/Observer
│   └── notifiers.py      # Notificadores Concretos (Email, Log)
├── infra/
│   └── config.py         # Singleton (Configuração e Logger centralizado)
├── tests/
│   └── test_patterns.py  # Testes automatizados que provam a integridade dos padrões
└── README.md             # Esta documentação
```

## 🛠️ Como Executar a Aplicação

A aplicação requer o Python 3 para ser executada.

Clone o repositório:

```bash
git clone https://github.com/andersonniltondesouza-unidavi/mensalidade_escolar_design_patterns
```

Acesse o diretório do projeto:

```bash
cd [DIRETORIO ONDE FOI BAIXADO O PROJETO]
```

### Execute os Testes Automatizados:

Para verificar se os padrões estão comportando-se como esperado, execute a suíte de testes:

```bash
python3 -m unittest tests/test_patterns.py
```

### Execute o sistema:

Inicie o menu interativo pelo terminal para simular a geração de boletos.

```bash
python3 app/main.py
```

O menu interativo será exibido no console.

---

## 🧠 Funcionamento e Justificativa dos Padrões

Este projeto substitui condicionais complexas (if/else) e acoplamento rígido por composição de objetos e polimorfismo. Abaixo, as justificativas técnicas para cada padrão escolhido.

### 1. Strategy (Cálculo de Descontos)

Diferente de usar múltiplos condicionais para verificar se o aluno tem "Bolsa Mérito", "Desconto Irmãos" ou "Convênio", foi utilizado o padrão Strategy. Ele define uma família de regras de desconto e os torna intercambiáveis.

Em `strategies/descontos.py`, cada regra é uma classe isolada. O contexto (`GeradorBoleto`) não precisa saber qual regra está sendo usada, ele apenas delega o cálculo:

```python
# O Contexto delega para a Estratégia injetada
desconto = self.strategy.calcular_desconto(valor_bruto)
```

Isso permite adicionar novas regras de negócio (ex: "Desconto Funcionário") sem modificar nenhuma linha da classe principal do boleto (**Princípio Aberto/Fechado**).

### 2. Decorator (Encargos e Multas)

A aplicação de multas e juros precisa ser dinâmica e cumulativa. Um boleto pode ter apenas Multa, apenas Juros, ou ambos. Criar subclasses para cada combinação (ex: `BoletoComMultaEJuros`) causaria uma explosão de classes.

O padrão Decorator resolve isso permitindo "envolver" o objeto de cobrança original dinamicamente.

```python
# Composição dinâmica no runtime:
boleto = MensalidadeBase(1000)
boleto = MultaAtraso(boleto)      # Adiciona R$ 50
boleto = JurosMoratorios(boleto)  # Adiciona 2% sobre (1000 + 50)
```

O sistema calcula o valor final percorrendo a pilha de decoradores, mantendo a mesma interface `CalculadoraMensalidade`.

### 3. Observer (Notificações)

Para atender ao requisito de notificar os pais (Email) e o sistema (Log) sem acoplar bibliotecas de I/O à regra de negócio, foi usado o padrão Observer.

A classe `GeradorBoleto` atua como Subject. Quando um boleto é processado com sucesso, ela notifica automaticamente todos os Observers inscritos na lista.

### 4. Singleton (Infraestrutura)

Utilizado na classe `SystemConfig` em `infra/config.py`.

Justificativa: Garante que configurações globais do sistema (como Nome da Escola, Versão da API ou Logger Central) tenham uma instância única acessível globalmente, evitando conflitos de estado ou múltiplas conexões desnecessárias.

---

## ✅ Cobertura de Testes (`tests/`)

O sistema inclui testes automatizados para validar a implementação técnica dos padrões:

* `test_strategy_desconto`: Prova que injetar estratégias diferentes (Bolsa vs Sem Desconto) altera o resultado final.
* `test_decorator_encargos`: Prova a matemática da composição (Valor Base + Multa + Juros) e a ordem de execução.
* `test_singleton_unicidade`: Verifica se múltiplas chamadas ao `SystemConfig()` retornam a mesma instância de memória (`assertIs`).
