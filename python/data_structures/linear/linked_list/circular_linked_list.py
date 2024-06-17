from data_structures.linear.linked_list.models import TraversalType


class Node:
    
    """
    Each node has the data it stores and a pointer to the next node
    """
    def __init__(self, data) :
        self.next:Node = None
        self.data = data
    
class LinkedList:
    def __init__(self) :
        self.__last:Node = None
        self.__capacity=0

    def capacity(self):
        return self.__capacity
    
    def add_at_front(self, data):
        """
        Adds a new node as the first node in the list
        The last node would point to this node in the list
        """
        if self.is_empty():
            return self.add_to_empty(data)
        new_node = Node(data)

        new_node.next = self.__last.next
        self.__last.next = new_node
        self.__capacity+=1
        return self.__last
    
    def append_after(self,item,data):
        if self.__last is None:
            return None
        new_node = Node(data)
        current = self.__last.next # start traversing at the head
        while current is not None:
            if item == current.data:
                new_node.next = current.next
                current.next = new_node
                self.__capacity+=1
                if current == self.__last: # update the last to the new node if inserted after the last node
                    self.__last = new_node
                return self.__last
            current = current.next
            if current==self.__last.next: # check if we are back to the beginning
                print (f"Item {item} not found in the list")
                break
        return None

    def append(self, data):
        """
        Adds a new node as the last node in the list
        This node would point to the first node in the list
        """
        if self.is_empty():
            return self.add_to_empty(data)
        new_node = Node(data)
        new_node.next = self.__last.next
        self.__last.next = new_node
        self.__last = new_node
        self.__capacity+=1
        return self.__last
    
    def is_empty(self):
        return self.__last is None
    
    def add_to_empty(self,data):
        if (self.__last is not None):
            return self.__last
        node = Node(data)
        node.data = data
        self.__last = node
        self.__last.next = self.__last
        self.__capacity+=1
        return self.__last

    def show(self):
        if self.is_empty():
            print ("List is empty")
            return
        
        current = self.__last.next
        while current is not None :
            print(current.data, end=" ")
            current = current.next
            if current == self.__last.next:
                break

    def find(self, item):
        if self.is_empty():
            return None
        
        current = self.__last.next 

        while current is not None:
            if item == current.data:
                return current
            current = current.next
            if current == self.__last.next:
                break
