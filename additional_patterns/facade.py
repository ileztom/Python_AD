class SubsystemA:
    def operation_a(self):
        return "Подсистема A"

class SubsystemB:
    def operation_b(self):
        return "Подсистема B"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        return f"Фасад: {self._subsystem_a.operation_a()}, {self._subsystem_b.operation_b()}"

facade = Facade()
print(facade.operation())  # Фасад: Подсистема A, Подсистема B