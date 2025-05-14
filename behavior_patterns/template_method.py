from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation()
        self.required_operation()
        self.hook()

    def base_operation(self):
        print("AbstractClass: Базовая операция")

    @abstractmethod
    def required_operation(self):
        pass

    def hook(self):
        pass

class ConcreteClass(AbstractClass):
    def required_operation(self):
        print("ConcreteClass: Реализация обязательного метода")

    def hook(self):
        print("ConcreteClass: Переопределение хука")

client = ConcreteClass()
client.template_method()