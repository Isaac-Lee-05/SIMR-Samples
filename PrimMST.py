#
# This module implements a function that performs Prim's Algorithm on an undirected, weighted graph represented by an adjacency
# matrix. The algorithm takes O(V^2) time and returns each edge in the minimum spanning tree along with its weight, and also
# gives the total weight of the MST.
#

# Function that performs Prim's algorithm on an adjacency matrix, returns edges/weights of MST as well as total weight
def PrimMST(G):
    # Number of vertices is equal to number of rows of G
    vertices = len(G)
    # Creates arrays for keys and predecessors of vertices, also Q for extracting vertices from
    keys = []
    pre = []
    Q = []
    # Set all keys to an absurdly high number (basically infinity), all predecessors to -1 (non-existent)
    # Append all vertices to Q
    for i in range(vertices):
        keys.append(1000000000)
        pre.append(-1)
        Q.append(i)
    # Root vertex is 0, so set its key to 0
    keys[0] = 0
    # Runs until Q is empty
    while len(Q) > 0:
        # Finds the vertex with minimum key, as well as that vertex's place in Q
        minKey = 1000000000
        minKeyIndex = -1
        QIndex = -1
        for i in range(len(Q)):
            current = Q[i]
            if keys[current] < minKey:
                minKey = keys[current]
                minKeyIndex = current
                QIndex = i
        # Sets the key of the vertex to an absurdly low number (basically -infinity). This signifies that it will not be in Q
        # anymore when the for loop below runs, since the edge weight will definitely be greater than the key
        keys[minKeyIndex] = -1000000000
        # Removes the vertex from Q
        Q.pop(QIndex)
        for i in range(vertices):
            # If a vertex is a neighbor of the min-key vertex and the edge weight is less than the current key, update the
            # predecessor and key
            if G[minKeyIndex][i] != 0 and G[minKeyIndex][i] < keys[i]:
                pre[i] = minKeyIndex
                keys[i] = G[minKeyIndex][i]
    totalWeight = 0
    print("Edge    Weight")
    # Print out all edges in the MST and their weights, calculating total weight along the way
    for i in range(1, vertices):
        first = pre[i]
        last = i
        weight = G[first][last]
        print("(" + str(first) + ", " + str(last) + ")  " + str(weight))
        totalWeight += weight
    # Print out total MST weight
    print("MST weight: " + str(totalWeight))

