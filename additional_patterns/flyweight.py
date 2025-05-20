class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        return f"Общее: {self._shared_state}, Уникальное: {unique_state}"

class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, shared_state):
        if shared_state not in cls._flyweights:
            cls._flyweights[shared_state] = Flyweight(shared_state)
        return cls._flyweights[shared_state]

factory = FlyweightFactory()
fw1 = factory.get_flyweight("A")
print(fw1.operation("1"))  # Общее: A, Уникальное: 1

fw2 = factory.get_flyweight("A")
print(fw2.operation("2"))  # Общее: A, Уникальное: 2