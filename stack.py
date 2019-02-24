import operator

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack == []:
            return None

        return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.stack == []:
            return None

        return self.stack[0]


def compareString(str):
    stack1 = Stack()
    stack2 = Stack()
    for i in range(len(str)):
        if str[i] == "(":
            stack1.push(str[i])
        elif str[i] == ")":
            stack2.push(str[i])

    if stack1.size() == stack2.size():
        return True
    else:
        return False

stack = Stack()
stack.push("=")
stack.push("+")
stack.push(9)
stack.push("*")
stack.push(5)
stack.push("+")
stack.push(2)
stack.push(8)

def postfixСalculation(stack):
    ops = {'+': operator.add, '-': operator.sub,
           '*': operator.mul, '/': operator.floordiv}
    stack2 = Stack()
    for i in range(stack.size()):
        a = stack.peek()
        stack.pop()

        if a == "=":
            result = stack2.peek()

        elif isinstance(a,int):
            stack2.push(a)

        elif isinstance(a,str):
            b = stack2.peek()
            stack2.pop()
            c = stack2.peek()
            d = ops[a](b,c)
            stack2.push(d)

    return result


