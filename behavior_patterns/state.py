class State:
    def handle(self):
        pass

class StateA(State):
    def handle(self):
        print("Состояние A")
        return StateB()

class StateB(State):
    def handle(self):
        print("Состояние B")
        return StateA()

class Context:
    def __init__(self):
        self._state = StateA()

    def request(self):
        self._state = self._state.handle()

context = Context()
context.request()
context.request()