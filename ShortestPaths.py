#
# This module contains several shortest path related functions, including randGeoGraph, which generates a random geometric graph,
# checkPath, which checks to see if a path of at most a certain length can be reached between two verticesin a graph, and
# iterativeDeepening, which finds the shortest path between two vertices.

from random import *
from graphics import *

# Returns a list of vertices and a dictionary mapping each vertex index to a list of indices of adjacent vertices
# Takes in bounds for coordinates (A and B), number of vertices (N), and maximum adjacency distance (D)
def randGeoGraph(A, B, N, D):
    # Return errors if A, B, N, or D are not nonnegative integers
    if isinstance(A, int)==False or A < 0 or isinstance(B, int)==False or B < 0:
        print("Error, A and B must be nonnegative integers")
        return(None, None)
    elif isinstance(N, int)==False or N < 0:
        print("Error, N must be a nonnegative integer")
        return(None, None)
    elif isinstance(D, int)==False or D < 0:
        print("Error, D must be a nonnegative integer")
        return(None, None)
    vertexList = []
    for i in range(N):
        # Creates vertex with random coordinates in the bounds and appends it to the list of vertices
        vertex = [randint(0, A-1), randint(0, B-1)]
        vertexList.append(vertex)
    vertexDict = {}
    for i in range(N):
        # Creates list of adjacent indices for every vertex
        adjList = []
        for j in range(N):
            # If the vertices are not the same and the distance between them is less than or equal to D,
            # append j to the adjacent list
            if i != j and (vertexList[i][0]-vertexList[j][0])**2 + (vertexList[i][1]-vertexList[j][1])**2 <= D**2:
                adjList.append(j)
        # Maps the vertex index to the adjacent list
        vertexDict[i] = adjList
    return vertexList, vertexDict

# Performs DFS up to length L away from startIndex in a graph with adjacencies in dictionary E
# Takes in a list, Larray, that stores the distances of vertices from the original starting index
def checkPathDFS(E, startIndex, Larray, L):
    # The neighbors of startIndex will be one unit farther than it
    newDist = Larray[startIndex] + 1
    # If the neightbors are with L of the original starting vertex
    if newDist <= L:
        # Checks every neighbor
        for i in range(len(E[startIndex])):
            currentNeighbor = E[startIndex][i]
            # If the current neighbor's distance can be shortened, update its distance and run DFS
            if Larray[currentNeighbor] > newDist:
                Larray[currentNeighbor] = newDist
                checkPathDFS(E, currentNeighbor, Larray, L)

# Checks if there is a path of length at most L from vertex S to T in the graph designated by V and E
def checkPath(V, E, S, T, L):
    # Input validation for invalid inputs
    if isinstance(V, list) == False:
        print("Error, V must be a list")
        return(None)
    elif isinstance(E, dict) == False:
        print("Error, E must be a dictionary")
        return(None)
    elif isinstance(L, int) == False or L < 0:
        print("Error, L must be a nonnegative integer")
        return(None)
    elif isinstance(S, list) == False or len(S) != 2:
        print("Error, S must be a list of 2 coordinates")
        return(None)
    elif isinstance(T, list) == False or len(T) != 2:
        print("Error, T must be a list of 2 coordinates")
        return(None)
    # Variables for the corresponding indices of S and T in V
    Sindex = 0
    Tindex = 0
    # If S and T are in V, update Sindex and Tindex. Otherwise, there clearly isn't a path so return False
    found = False
    i = 0
    while found == False and i < len(V):
        if S == V[i]:
            Sindex = i
            found = True
        else:
            i += 1
    if found == False:
        return(False)
    found = False
    i = 0
    while found == False and i < len(V):
        if T == V[i]:
            Tindex = i
            found = True
        else:
            i += 1
    if found == False:
        return(False)
    # Array that stores the distance from S to all the other vertices
    LengthArray = []
    # All vertices are unmarked with a 2*L since DFS will never reach that length, creating a distinction
    for i in range(len(V)):
        LengthArray.append(2*L)
    # Clearly, S is 0 distance from itself
    LengthArray[Sindex] = 0
    # Run DFS
    checkPathDFS(E, Sindex, LengthArray, L)
    # If T is less than or equal to L from S, return True
    if LengthArray[Tindex] <= L:
        return(True)
    else:
        return(False)

# Performs binary search to find the shortest path from S to T in a graph described by V and E within bounds low and high
def pathBinSearch(V, E, S, T, low, high):   
    # Base case: if the low and high indices are equal (i.e. there are no more possible values
    # to search), then we've found our answer and can return it
    if high == low:
        return(low)
    else:
        mid = (low+high)//2
        # Perform checkPath on the middle distance
        result = checkPath(V, E, S, T, mid)
        # If a path of length mid or less cannot be found, we check the higher half of the range
        if result == False:
            return(pathBinSearch(V, E, S, T, mid+1, high))
        # Otherwise, check the lower half
        else:
            return(pathBinSearch(V, E, S, T, low, mid))

# Finds the shortest path from S to T in a graph described by V and E within bounds LB and UB
def iterativeDeepening(V, E, S, T, LB, UB):
    # Input validation for invalid inputs
    if isinstance(V, list) == False:
        print("Error, V must be a list")
        return(None)
    elif isinstance(E, dict) == False:
        print("Error, E must be a dictionary")
        return(None)
    elif isinstance(LB, int) == False or LB < 0:
        print("Error, LB must be a nonnegative integer")
        return(None)
    elif isinstance(UB, int) == False or UB < 0:
        print("Error, UB must be a nonnegative integer")
        return(None)
    elif isinstance(S, list) == False or len(S) != 2:
        print("Error, S must be a list of 2 coordinates")
        return(None)
    elif isinstance(T, list) == False or len(T) != 2:
        print("Error, T must be a list of 2 coordinates")
        return(None)
    # If there is no path with length less than or equal to the upper bound from S to T, then we know no path exist
    if checkPath(V, E, S, T, UB) == False:
        print("No path exists")
        return(None)
    # Otherwise, call the binary search function and return its result
    return(pathBinSearch(V, E, S, T, LB, UB))

