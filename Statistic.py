#
# The module implements an algorithm based off of quicksort which
# returns a requested order statistic of an array
#

# Partition algorithm: takes in the array B to be partitioned and the
# lower and upper bounds, p and r, of the subarray that will be partitioned
def Partition(B, p, r):
    # Sets last element in subarray as pivot
    x = B[r-1]
    i = p-1
    # Iterates through every item other than the pivot
    for j in range(p, r-1):
        # If the element is less than the pivot, switches it with a spot on the
        # low side
        if B[j] <= x:
            i += 1
            oldi = B[i]
            oldj = B[j]
            B[i] = oldj
            B[j] = oldi
    # Moves pivot to just right of low side
    oldi = B[i+1]
    oldr = B[r-1]
    B[i+1] = oldr
    B[r-1] = oldi
    # Return new index of pivot
    return(i+1)

# Takes in an array A and returns the jth order statistic of the array
def statistic(A, j):
    n = len(A)
    # Will only work for a statistic within the range of the array
    if 1 <= j <= n:
        # Sets a variable for the index of the pivot
        q = Partition(A, 0, n)
        # If the index of the pivot is equal to j-1 (since the array begins
        # indexing at 0), returns the pivot value
        if q == j-1:
            return(A[q])
        # If the pivot index is less than j-1, call statistic on the high side
        # of the partition, subtracting q from the requested statistic because we
        # are now only looking at the upper half of the subarray
        elif q < j-1:
            return(statistic(A[q+1: n], j-q-1))
        # If the pivot index is greater than j-1, call statistic on the low side
        else:
            return(statistic(A[0: q], j))
