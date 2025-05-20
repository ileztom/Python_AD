class Component:
    def operation(self):
        return "Компонент"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Декоратор({self._component.operation()})"

simple = Component()
decorated = Decorator(simple)
print(decorated.operation())  # Декоратор(Компонент)