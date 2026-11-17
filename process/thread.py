class Thread:
    def __init__(self, id, pointer, register, stack, state):
        self.id = id
        self.pointer = pointer
        self.register = register
        self.stack = stack
        self.state = state
