class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Обработчик A обработал запрос")
        else:
            super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Обработчик B обработал запрос")
        else:
            super().handle(request)

handler = ConcreteHandlerA(ConcreteHandlerB())
handler.handle("B")