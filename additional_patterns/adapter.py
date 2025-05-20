class OldSystem:
    def old_operation(self):
        return "Старая система"

class Adapter:
    def __init__(self, old_system):
        self._old_system = old_system

    def new_operation(self):
        return f"Адаптер: {self._old_system.old_operation()}"

client = Adapter(OldSystem())
print(client.new_operation())