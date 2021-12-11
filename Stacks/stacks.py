# first in last out system.

class Stack():
    def __init__(self):
        self.lyst = []


    def __str__(self):
        return str(self.lyst)


    def push(self, num):
        self.lyst.append(num)

    
    def pop(self):
        if len(self.lyst) == 0:
            raise SyntaxError
        value = self.lyst[-1]
        del self.lyst[-1]
        return value


    def top(self):
        return self.lyst[-1]


    def size(self):
        return len(self.lyst)


    def clear(self):
        self.lyst = []
