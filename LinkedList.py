#
# Classes for a node in a linked list and a linked list
#

# Class for linked list nodes
class Node:
    # Constructor takes in a value for the nodes, creates instance variables
    # for the value and pointer
    def __init__(self, value):
        self.value = value
        self.next = None

    # Getters for value and next
    def getValue(self):
        return(self.value)
    
    def getNext(self):
        return(self.next)

    # Setter for next
    def setNext(self, newNext):
        self.next = newNext

# Class for linked list
class LinkedList:
    # Constructor with no parameters, creates instance variable for the head
    def __init__(self):
        self.head = None

    # Returns the head node
    def getHead(self):
        return(self.head)

    # Inserts an item into the linked list
    def insert(self, item):
        # Creates a new node with the item
        newNode = Node(item)
        # Make the new node the head
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    # Searches for an item in the linked list
    def search(self, item):
        previous = None
        current = self.head
        # Iterate through the linked list until it's been completely traversed
        # of the item has been found
        while current != None and current.getValue() != item:
            previous, current = current, current.getNext()
        # Return the node containing the item and the node right before it
        return(previous, current)

    # Deletes an item from the linked list
    def delete(self, item):
        previous, current = self.search(item)
        # If the entire linked list was traversed without finding the item,
        # the requested item (or the requested edge, in the context of a graph)
        # is non-existent
        if current == None:
            print("Error, this edge is non-existent")
        # If the requested item is the head, set the new head as the old
        # 'next' node
        elif item == self.head:
            self.head = self.head.getNext()
        # Otherwise adjust the pointers to 'skip over' the deleted node
        else:
            previous.setNext(current.getNext())
