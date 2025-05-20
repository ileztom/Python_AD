class RealSubject:
    def request(self):
        return "Реальный объект"

class Proxy:
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        return f"Прокси: {self._real_subject.request()}"

proxy = Proxy()
print(proxy.request())  # Прокси: Реальный объект