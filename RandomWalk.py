#
# This module implements a function, randomWalk, which creates a graph using
# a file as input and makes a simple user interface allowing the user to
# simulate randomly generated walks along the graph.
#

from random import randint
from GraphAdjList import GraphAdjList
from GraphAdjMatrix import GraphAdjMatrix

# Function takes in as parameters graphClass, the class used to create the graph,
# and file, the file from which the list of edges will be read
def randomWalk(graphClass, file):
    graph = graphClass()
    notEmpty = True
    f = open(file, "r")
    # While we don't come across the last line of the file, which is empty,
    # read in the edges
    while notEmpty == True:
        l = f.readline()
        if l == "":
            # If the line is empty, we have reached the end of the file
            notEmpty = False
        else:
            # Add an edge between the two vertices
            a, b = l.split(",")
            b = b[:-1]
            graph.addEdge(a, b)
    f.close()

    status = True
    while status == True:
        print("Options:")
        print("0: Quit")
        print("Anything else: Proceed")
        option = int(input("Option: "))
        # If the user quits, terminate the while loop
        if option == 0:
            status = False
        else:
            check1 = False
            check2 = False
            while check1 == False:
                print("Enter the number of steps")
                n = int(input("Steps: "))
                # If the user enters a valid number of steps, terminate the
                # while loop and move on
                if n >= 0:
                    check1 = True
                # Otherwise, print an error message and run the while loop again
                else:
                    print("Error, the number of steps must be nonnegative")
            while check2 == False:
                print("Enter the starting vertex")
                startVertex = input("Starting vertex: ")
                dictionary = graph.getAdjDict()
                # If the user enters a vertex that exists, terminate the
                # while loop and move on
                if startVertex in dictionary:
                    check2 = True
                # Otherwise, print an error message and run the while loop again
                else:
                    print("Error, please enter an existing vertex")
            # Start by printing the first vertex
            print(startVertex)
            currentVertex = startVertex
            # Iterate n times
            for i in range(n):
                # Choose the next vertex to be a random neighbor of the current
                # vertex
                neighbors = graph.getNeighbors(currentVertex)
                rand = randint(0, len(neighbors)-1)
                currentVertex = neighbors[rand]
                # Print the new vertex
                print(currentVertex)

