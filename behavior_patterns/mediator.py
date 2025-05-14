class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, comp1, comp2):
        self._comp1 = comp1
        self._comp2 = comp2
        self._comp1.mediator = self
        self._comp2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Посредник реагирует на A и запускает B")
            self._comp2.do_b()
        elif event == "B":
            print("Посредник реагирует на B и запускает A")
            self._comp1.do_a()

class BaseComponent:
    def __init__(self):
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class ComponentA(BaseComponent):
    def do_a(self):
        print("Компонент A делает A")
        self._mediator.notify(self, "A")

class ComponentB(BaseComponent):
    def do_b(self):
        print("Компонент B делает B")
        self._mediator.notify(self, "B")

comp1 = ComponentA()
comp2 = ComponentB()
mediator = ConcreteMediator(comp1, comp2)

comp1.do_a()