from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Лист"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Ветка({'+'.join(results)})"

tree = Composite()
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())

tree.add(branch1)
tree.add(Leaf())

print(tree.operation())  # Ветка(Ветка(Лист+Лист)+Лист)