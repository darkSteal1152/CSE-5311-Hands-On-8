class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == self.size - 1:
            return True
        return False

    def push(self, value):
        if self.is_full():
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def display(self):
        if self.is_empty():
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=' ')
        print()

stack = Stack(6)
stack.push(4)
stack.display()
stack.push(1)
stack.display()
stack.push(3)
stack.display()
stack.pop()
stack.display()
stack.push(8)
stack.display()
stack.pop()
stack.display()
