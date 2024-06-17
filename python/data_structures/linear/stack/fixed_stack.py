class Stack:
    """
    This is a fixed size stack, which requires a maximum size
    """
    
    def __init__(self, size:int=1):
        self.__size = size
        self.__capacity = 0
        self.stack = []

    def count(self):
        return self.__capacity

    def size(self):
        return self.__size

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack.append(item)
        self.__capacity+=1
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        self.__capacity-=1
        return self.stack.pop()
    
    def is_full(self):
        return self.__capacity >= self.__size
    
    def is_empty(self):
        return self.__capacity<=0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.__capacity-1]
    