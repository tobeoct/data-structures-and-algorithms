# Linear Data Structures 
A type of data structure in computer science where data elements within the structure are arranged or connect to each other sequentially. Each element has a previous and next adjacent, except for the first and last elements. They can be accessed in a single run.

## Stack
A stack is a linear data structure in which data is inserted and retrieved from the same end. 
It follows are Last In First Out approach to retrieving data
The last element inserted is the first to be retrieved
### Operations:
- push: Adds an element to the top of the stack
- pop: Removes the element in the top of the stack
- peek
- isEmpty
- isFull

### Types
Fixed Size: The stack has a predefined size and cannot grow or shrink dynamically. 
Dynamic Size: The stack can grow or shrink dynamically. When the stack is full it increases its size to accomodate more data and when its empty the size reduces. This is implemented using a Linked List