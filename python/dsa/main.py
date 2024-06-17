
from data_structures.linear.stack.dynamic_stack import Stack as DynamicStack


def main():
    stack = DynamicStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(f"Top: {stack.peek()}")
    stack.pop()
    stack.pop()
    print(f"Top: {stack.peek()}")