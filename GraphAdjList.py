#
# This is an implementation of a graph using an adjacency list for each vertex.
# A dictionary is used to map each vertex to an index in an array, which contains
# a corresponsing linked list for each vertex containing all of its neighbors.
# Methods for adding and deleting edges, as well as finding the neighbors of
# a vertex and finding if two vertices are adjacent are included.
#

from LinkedList import Node
from LinkedList import LinkedList

# Class for representing a graph with an adjacency list
class GraphAdjList:
    # Constructor
    def __init__(self):
        # Instance variable adjDict maps each vertex to a value in the array adjList
        # which contains linked lists of the neighbors of each vertex
        self.adjDict = {}
        self.adjList = []
        # nextEmptySlot designates an empty index in the list that a new vertex can
        # map to
        self.nextEmptySlot = 0

    # Adds an edge between vertices u and v
    def addEdge(self, u, v):
        # If u or v is a new vertex, map it to an empty slot in adjList using adjDict
        # Because we always increment nextEmptySlot by 1, we can just append a new
        # linked list to store the new vertex's neighbors
        if u not in self.adjDict:
            self.adjDict[u] = self.nextEmptySlot
            self.nextEmptySlot += 1
            newList = LinkedList()
            self.adjList.append(newList)
        if v not in self.adjDict:
            self.adjDict[v] = self.nextEmptySlot
            self.nextEmptySlot += 1
            newList = LinkedList()
            self.adjList.append(newList)
        # Regardless of whether the vertices are new or not, insert u and v in
        # each other's linked lists.
        self.adjList[self.adjDict[u]].insert(v)
        self.adjList[self.adjDict[v]].insert(u)

    # Deletes an edge between vertices u and v if it exists
    def deleteEdge(self, u, v):
        # If u and v aren't adjacent, the edge won't exist
        if not self.isAdjacent(u, v):
            print("Error, this edge is non-existent")
        # Otherwise, delete u and v from each other's linked lists
        else:
            self.adjList[self.adjDict[u]].delete(v)
            self.adjList[self.adjDict[v]].delete(u)

    # Returns a list of the neighbors of vertex u
    def getNeighbors(self, u):
        returnList = []
        # If u is not an existing vertex, return an empty list
        if (u not in self.adjDict):
            return(returnList)
        # Otherwise, iterate through all the nodes of u's linked list and
        # add their values to returnList
        current = self.adjList[self.adjDict[u]].getHead()
        while current != None:
            returnList.append(current.getValue())
            current = current.getNext()
        return(returnList)

    # Returns if u and v are adjacent or not
    def isAdjacent(self, u, v):
        # If either u or v is not an existing vertex, they won't be adjacent
        if (u not in self.adjDict) or (v not in self.adjDict):
            return(False)
        # Otherwise, if v is found in u's linked list, they are adjacent
        previous, current = self.adjList[self.adjDict[u]].search(v)
        if current == None:
            return(False)
        else:
            return(True)

    # Returns the dictionary of vertex and index pairs
    def getAdjDict(self):
        return(self.adjDict)

