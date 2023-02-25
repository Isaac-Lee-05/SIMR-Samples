#
# This is an implementation of a graph using an adjacency matrix for each vertex.
# A dictionary is used to map each vertex to an index (the same for both columns
# and rows). A given value in the array indicates how many edges exist between
# the vertices that correspond to the row and the column.
# Methods for adding and deleting edges, as well as finding the neighbors of
# a vertex and finding if two vertices are adjacent are included.
#

# Class for representing a graph with an adjacency matrix
class GraphAdjMatrix:
    # Constructor
    def __init__(self):
        # Instance variable adjDict maps each vertex to the same row and column
        # values in the 2D array adjMatrix, whose values indicate how many
        # edges exist between the vertices that are mapped to by the column
        # and row values
        self.adjDict = {}
        self.adjMatrix = []
        # nextEmptySlot designates an empty index that a new vertex can map to
        self.nextEmptySlot = 0

    # Adds an edge between vertices u and v
    def addEdge(self, u, v):
        # If u or v is a new vertex, map it to an empty index using adjDict
        if u not in self.adjDict:
            self.adjDict[u] = self.nextEmptySlot
            self.nextEmptySlot += 1
        # Because we always increment nextEmptySlot by 1, we just add another row and
        # column to the array, initializing all the new values to 0
            self.adjMatrix.append([])
            for i in range(len(self.adjMatrix[0])):
                self.adjMatrix[len(self.adjMatrix)-1].append(0)
            for i in range(len(self.adjMatrix)):
                self.adjMatrix[i].append(0)
        if v not in self.adjDict:
            self.adjDict[v] = self.nextEmptySlot
            self.nextEmptySlot += 1
            self.adjMatrix.append([])
            for i in range(len(self.adjMatrix[0])):
                self.adjMatrix[len(self.adjMatrix)-1].append(0)
            for i in range(len(self.adjMatrix)):
                self.adjMatrix[i].append(0)
        # Regardless of whether the vertices are new or not, increment the two values
        # that correspond to the numbers of edges between u and v
        self.adjMatrix[self.adjDict[u]][self.adjDict[v]] += 1
        self.adjMatrix[self.adjDict[v]][self.adjDict[u]] += 1

    # Deletes an edge between vertices u and v if it exists
    def deleteEdge(self, u, v):
        # If u and v aren't adjacent, the edge won't exist
        if not self.isAdjacent(u, v):
            print("Error, this edge is non-existent")
        # Otherwise, decrement the two values that correspond to the numbers of edges
        # between u and v
        else:
            self.adjMatrix[self.adjDict[u]][self.adjDict[v]] -= 1
            self.adjMatrix[self.adjDict[v]][self.adjDict[u]] -= 1

    # Returns a list of the neighbors of vertex u
    def getNeighbors(self, u):
        returnList = []
        # If u is not an existing vertex, return an empty list
        if (u not in self.adjDict):
            return(returnList)
        # Otherwise, iterate through all the values in u's subarray, appending the
        # corresponding vertices if an edge exists
        for key in self.adjDict:
            if self.adjMatrix[self.adjDict[u]][self.adjDict[key]] > 0:
                returnList.append(key)
        return(returnList)

    # Returns if u and v are adjacent or not
    def isAdjacent(self, u, v):
        # If either u or v is not an existing vertex, they won't be adjacent
        if (u not in self.adjDict) or (v not in self.adjDict):
            return(False)
        # Otherwise, if the value in the array that corresponds to the number of edges
        # between the two vertices is positive, they're adjacent
        if self.adjMatrix[self.adjDict[u]][self.adjDict[v]] > 0:
            return(True)
        else:
            return(False)

    # Returns the dictionary of vertex and index pairs
    def getAdjDict(self):
        return(self.adjDict)

