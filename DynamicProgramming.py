#
# This module implements two functions that utilize dynamic programming. The first
# evaluates Fibonacci numbers by working its way up from the smallest, storing
# all values as it goes along to ensure faster calculations using the Fibonacci
# definition. The second evaluates if a given target value can be reached using
# a given array of coins by working its way up from smaller values and adding
# coins to the arrangements to obtain larger totals.
#

# Takes as input a nonnegative integer n, returns the nth Fibonacci number
def fibDP(n):
    # Error for invalid inputs
    if isinstance(n, int) == False or n < 0:
        return("Error, n must be a nonnegative integer")
    # If n < 2, then it's a base case so there's no use in creating a DP grid,
    # just return 1
    elif n < 2:
        return(1)
    # All n >= 2
    else:
        # Create a DP grid of size (n+1)*1, filled with 0s as placeholders
        fibGrid = [0]*(n+1)
        # Base cases - first two Fibonacci numbers are 1
        fibGrid[0] = 1
        fibGrid[1] = 1
        # For every value of i from 2 to n, calculate the ith Fibonacci number
        # by adding the previous two and save that value in the grid
        for i in range(2, n+1):
            fibGrid[i] = fibGrid[i-1] + fibGrid[i-2]
        # Return nth Fibonacci number
        return(fibGrid[n])

# Takes in a target value and a list of coin values. Returns true if the target
# can be reached using the coins, returns false otherwise.
def exactChange(target, coins):
    # Error for invalid inputs
    if isinstance(target, int) == False or target < 0:
        return("Error, n must be a nonnegative integer")
    # If target = 0, then it's a base case so there's no use in creating a DP grid,
    # just return True
    elif target == 0:
        return(True)
    else:
        # Create DP grid of size target by n, filled with empty strings initially
        n = len(coins)
        changeGrid = []
        for i in range(n):
            changeGrid.append([])
        for i in range(n):
            for j in range(target+1):
                changeGrid[i].append("")
        # Base case: a target of 0 is reachable by selecting no coins
        for a in range(n):
            changeGrid[a][0] = "No"
        # Iterates through all possible totals from 0 to target
        for k in range(target+1):
            # Only need to check the first row to see if the entire column is blank
            if changeGrid[0][k] != "":
                # Iterates through all coins
                for l in range(n):
                    # If the coin is not used and adding it to the total will still
                    # remain less than target, look at the column that corresponds
                    # to the total plus this new coin
                    if changeGrid[l][k] == "No" and k+coins[l] <= target:
                        x = k+coins[l]
                        # If there has not yet been a valid arrangement found for
                        # this new value, copy in the arrangement for the old total
                        # but make sure the selected coin is now a "yes"
                        if changeGrid[0][x] == "":
                            for m in range(n):
                                changeGrid[m][x] = changeGrid[m][k]
                            changeGrid[l][x] = "Yes"
        # If the column for the target value is not empty, return true. Return
        # false otherwise.
        if changeGrid[0][target] != "":
            return(True)
        else:
            return(False)
        
