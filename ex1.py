class Stack:

    def __init__(self, stack):
        self.stack = stack

    def isempty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True


    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()
        return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

example = '(((([{}]))))'
example = list(example)
stack = Stack(example)
stack.isempty()
stack.push(']')
stack.pop()
stack.peek()
stack.size()
