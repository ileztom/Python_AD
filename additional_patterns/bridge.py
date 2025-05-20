class Implementation:
    def operation_impl(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_impl(self):
        return "Реализация A"

class ConcreteImplementationB(Implementation):
    def operation_impl(self):
        return "Реализация B"

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return f"Абстракция: {self._implementation.operation_impl()}"

abstraction = Abstraction(ConcreteImplementationA())
print(abstraction.operation())  # Абстракция: Реализация A