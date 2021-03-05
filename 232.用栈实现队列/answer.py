class MyQueue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        if not self.outStack:
            self.in2out()
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            self.in2out()
        return self.outStack[-1]

    def empty(self):
         return not self.inStack and not self.outStack

    def in2out(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())
