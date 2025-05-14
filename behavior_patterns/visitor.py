class Visitor:
    def visit_element_a(self, element):
        pass

    def visit_element_b(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print(f"Посетитель обрабатывает {element.operation_a()}")

    def visit_element_b(self, element):
        print(f"Посетитель обрабатывает {element.operation_b()}")

class Element:
    def accept(self, visitor):
        pass

class ElementA(Element):
    def operation_a(self):
        return "Элемент A"

    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def operation_b(self):
        return "Элемент B"

    def accept(self, visitor):
        visitor.visit_element_b(self)

elements = [ElementA(), ElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)