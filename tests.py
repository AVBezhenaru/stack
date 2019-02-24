from stack import *

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