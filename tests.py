from stack import *
import operator


def sizeTest():
    print("Size test")
    stack = Stack()
    stack.push(1)

    if stack.size() == 1:
        print("OK")

    else:
        print("ERROR")

sizeTest()

def popTest():
    print("Pop test")
    stack = Stack()
    stack.push(1)
    stack.pop()

    if stack.size() == 0:
        print("OK")

    else:
        print("ERROR")

popTest()

def pushTest():
    print("Push test")
    stack = Stack()
    stack.push(1)

    if stack.size() == 1:
        print("OK")

    else:
        print("ERROR")

pushTest()

def peekTest():
    print("Peek test")
    stack = Stack()
    stack.push(1)

    if stack.peek() == 1:
        print("OK")

    else:
        print("ERROR")

peekTest()


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

        elif isinstance(a, int):
            stack2.push(a)

        elif isinstance(a, str):
            b = stack2.peek()
            stack2.pop()
            c = stack2.peek()
            d = ops[a](b, c)
            stack2.push(d)

    return result