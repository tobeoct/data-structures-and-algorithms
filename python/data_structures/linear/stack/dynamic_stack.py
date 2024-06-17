from data_structures.linear.linked_list.singly_linked_list import LinkedList as SinglyLinkedList


class Stack:
    def __init__(self) :
        self.__stack = SinglyLinkedList()
    
    def count(self):
        return self.__stack.capacity()

    def push(self, item):
        self.__stack.add_at_front(item)
        
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        head = self.__stack.remove_head()
        return head.data
    
    def is_empty(self):
        return self.count()<=0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__stack.head().data