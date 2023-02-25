#
# This module contains Node and Edge classes used in representing a flow network with the Network class. The Network class
# contains methods used for adding nodes and edges, and also has a method, find_residual() that recursivley finds an augmenting
# path. The final method, solve_network() uses find_residual() to find the max flow.
#

# Node class for network
class Node():
    # Constructor that taken in a label for the node, initializes lists of in and out edges
    def __init__(self, name):
        self.label = name
        self.inEdges = []
        self.outEdges = []

    # Adds edge to list of in edges
    def add_inEdge(self, edge):
        self.inEdges.append(edge)

    # Adds edge to list of out edges
    def add_outEdge(self, edge):
        self.outEdges.append(edge)

    # Getter methods for instance variables
    def get_label(self):
        return(self.label)

    def get_inEdges(self):
        return(self.inEdges)

    def get_outEdges(self):
        return(self.outEdges)

# Edge class for network
class Edge():
    # Constructor takes in start and end nodes and capacity, initializes flow to 0
    def __init__(self, startN, endN, cap):
        self.startNode = startN
        self.endNode = endN
        self.capacity = cap
        self.flow = 0
    
    # Sets the flow to f
    def setFlow(self, f):
        self.flow = f
    
    # Getters for instance variables
    def getFlow(self):
        return(self.flow)

    def getCapacity(self):
        return(self.capacity)

    def getStart(self):
        return(self.startNode)
    
    def getEnd(self):
        return(self.endNode)

# Network class
class Network():
    # Constructor initializes list of edges, and dictionary that maps nodes to Node objects with S and T already inside
    def __init__(self):
        self.edgeList = []
        startNode = Node("S")
        endNode = Node("T")
        self.nodeDict = {"S": startNode, "T": endNode}
    
    # Returns list of edges (used in exercise 3)
    def get_edgeList(self):
        return(self.edgeList)
    
    # Adds a node with the given label
    def add_node(self, label):
        newNode = Node(label)
        self.nodeDict[label] = newNode

    # Adds an edge from node a to b with capacity c
    def add_edge(self, a, b, c):
        # Creates new edge
        newEdge = Edge(self.nodeDict[a], self.nodeDict[b], c)
        # Appends the edge to the edgeList as well as the corresponding lists in the start and end nodes
        self.edgeList.append(newEdge)
        self.nodeDict[a].add_outEdge(newEdge)
        self.nodeDict[b].add_inEdge(newEdge)
    
    # Finds augmenting path with at most min_capacity from current to "T". Keeps list of visited nodes.
    def find_residual(self, current, visited, min_capacity):
        currentLabel = current.get_label()
        # If we are currently on T, we are done
        if currentLabel == "T":
            return(visited, min_capacity)
        currentIns = current.get_inEdges()
        currentOuts = current.get_outEdges()
        # Inspect every out edge
        for i in range(len(currentOuts)):
            currentEdge = currentOuts[i]
            nextNode = currentEdge.getEnd()
            if not(nextNode in visited):
                currentFlow = currentEdge.getFlow()
                currentCap = currentEdge.getCapacity()
                # If the potential to increase flow is less than min_capacity, update min_capacity
                if currentCap-currentFlow < min_capacity:
                    new_min_capacity = currentCap-currentFlow
                else:
                    new_min_capacity = min_capacity
                # Only proceed if min_capacity is greater than 0 (i.e. we can still augment along the path)
                if new_min_capacity > 0:
                # Update visited
                    newVisited = visited.copy()
                    newVisited.append(nextNode)
                # Recursive call with the next node, updated visited and min_capacity
                    resVisited, resCapacity = (self.find_residual(nextNode, newVisited, new_min_capacity))
                    # If the recursive call found a path, returns the results of that path
                    if resVisited != "failed":
                        return(resVisited, resCapacity)

        # Inspect every in edge
        for i in range(len(currentIns)):
            currentEdge = currentIns[i]
            nextNode = currentEdge.getStart()
            if not(nextNode in visited):
                currentFlow = currentEdge.getFlow()
                # If the potential to decrease flow (since this is a "backward" edge, we are actually giving a higher max flow)
                # is less than min_capacity, update min_capacity
                if currentFlow < min_capacity:
                    new_min_capacity = currentFlow
                else:
                    new_min_capacity = min_capacity
                # Rest of the procedure is the same as with the out nodes
                if new_min_capacity > 0:
                    newVisited = visited.copy()
                    newVisited.append(nextNode)
                    resVisited, resCapacity = (self.find_residual(nextNode, newVisited, new_min_capacity))
                    if resVisited != "failed":
                        return(resVisited, resCapacity)
        # If a node has no more edges with a remaining capacity >0, it's a dead end so signify it with a unique return statement
        return("failed", "failed")

    def solve_network(self):
        still_Run = True
        # As long as a augmenting path still exists (the min capactiy > 0), keep running
        while still_Run == True:
            # Save the visited array and min capacity from a find_residual call starting from S with insanely high
            # initial min capacity
            visited2, current_min = self.find_residual(self.nodeDict["S"], [self.nodeDict["S"]], 1000000)
            # If the initial call was unable to find a path, we've exhausted all possible paths
            if visited2 == "failed":
                still_Run = False
            else:
                # Iterate through each pair of adjacent nodes in visited2 array
                for i in range(len(visited2)-1):
                    current_node = visited2[i]
                    next_node = visited2[i+1]
                    out_edges = current_node.get_outEdges()
                    in_edges = current_node.get_inEdges()
                    edgeFound = False
                    # Inspect out edges and then in edges, looking for an edge from the current to next node
                    j = 0
                    while edgeFound == False and j < len(out_edges):
                        end = out_edges[j].getEnd()
                        if end == next_node:
                            edgeFound = True
                            # If the desired edge is an out edge, add the min capacity to the current flow of the edge
                            current_flow = out_edges[j].getFlow()
                            out_edges[j].setFlow(current_flow + current_min)
                        else:
                            j += 1
                    j = 0
                    while edgeFound == False and j < len(in_edges):
                        prev = in_edges[j].getStart()
                        if prev == next_node:
                            edgeFound = True
                            # If the desired edge is an in (backwards) edge, subtract the min capacity from the current flow 
                            # of the edge
                            current_flow = in_edges[j].getFlow()
                            in_edges[j].setFlow(current_flow - current_min)
                        else:
                            j += 1
        # To find the max flow, add the flow into the out edges and subtract the flow from the in edges
        max_flow = 0
        for i in range(len(self.nodeDict["S"].outEdges)):
            max_flow += self.nodeDict["S"].outEdges[i].getFlow()
        for i in range(len(self.nodeDict["S"].inEdges)):
            max_flow -= self.nodeDict["S"].inEdges[i].getFlow()
        return(max_flow)

