class Node:
    
    """
    Each node has the data it stores and a pointer to the next node
    """
    def __init__(self, data) :
        self.next:Node = None
        self.data = data
    
class LinkedList:
    def __init__(self) :
        self.__head:Node = None
        self.__capacity = 0
    def head(self):
        return self.__head
    def capacity(self):
        return self.__capacity
    
    def add_at_front(self, data):
        """
        Adds a new node to the front of the list
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__capacity+=1
        
    def append(self, data):
        """
        Adds a new node to the front of the list
        """
        if(self.is_empty()):
            self.add(data)
            return
            
        new_node = Node(data)
        current = self.__head
        while current.next is not None: # find the last node
            current = current.next
        current.next = new_node
        self.__capacity+=1
    
    def append_after(self, item, data):
        if self.__head is None:
            return
        new_node = Node(data)
        current = self.__head
        while current:
            if current.data == item:
                new_node.next = current.next
                current.next = new_node
                self.__capacity+=1
                return
            current = current.next
            
        print (f"Item {item} is not found in list")

    def is_empty(self):
        return self.__head is None
    
    def show(self):
        if self.is_empty():
            print("Empty list")
            return
        
        current = self.__head
        while current:
            print(current.data, end=" ")
            current = current.next
            
    def remove_head(self):
        head = self.__head
        self.__head = self.__head.next
        return head
    # def remove_at(self, node:Node):
    #     if self.is_empty():
    #         return self.__head
    #     current = self.__head

    #     while current.next:
    #         if current.next.data == node.data:
    #             current.next = current.next.next
    #             current.next.next = None
    #             self.__capacity-=1
    #             return self.__head 
    #         current = current.next
    #     if node== self.__head :
    #         self.__head = None
            


