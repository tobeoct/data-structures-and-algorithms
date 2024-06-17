class Node:
    
    """
    Each node has the data it stores and a pointer to the next node
    """
    def __init__(self,data, prev=None, next=None) :
        self.next:Node = next
        self.previous:Node =prev
        self.data = data
    
class LinkedList:
    def __init__(self) :
        self.__head:Node = None
    

    def add_at_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            return
        self.__head.previous = new_node
        new_node.next = self.__head
        self.__head=new_node
    
    def is_empty(self):
        return self.__head is None