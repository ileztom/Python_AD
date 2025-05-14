class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Установка состояния: {state}")
        self._state = state

    def save(self):
        print("Сохранение состояния...")
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"Восстановление состояния: {self._state}")

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

originator = Originator()
caretaker = Caretaker()

originator.set_state("Состояние 1")
caretaker.add_memento(originator.save())

originator.set_state("Состояние 2")
caretaker.add_memento(originator.save())

originator.restore(caretaker.get_memento(0))