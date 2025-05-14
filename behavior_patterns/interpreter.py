class Context:
    def __init__(self):
        self.variables = {}

class Expression:
    def interpret(self, context):
        pass

class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.variables.get(self.name, 0)

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

context = Context()
context.variables["x"] = 5
context.variables["y"] = 10

expr = Add(Variable("x"), Variable("y"))
result = expr.interpret(context)
print(f"x + y = {result}")