

class Stack():
    def __init__(self):
        self.stack = []
    def resolve(self): # resolves the effect on top of the
        self.stack.pop(-1).resolve()
