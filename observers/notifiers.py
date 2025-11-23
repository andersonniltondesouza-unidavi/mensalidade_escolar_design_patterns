from observers.interface import Observer

class EmailNotifier(Observer):
    def __init__(self, email_responsavel):
        self.email = email_responsavel

    def update(self, mensagem: str):
        print(f"📧 [EMAIL para {self.email}]: {mensagem}")

class SistemaLogNotifier(Observer):
    def update(self, mensagem: str):
        print(f"💾 [DB LOG]: Registrando evento -> {mensagem}")