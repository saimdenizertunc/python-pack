# Given two non-negative integers low and high.
# Returns the count of odd numbers between low and high(inclusive).

def countOdds(low, high):
    if low % 2 == 0:
        low += 1
    if high % 2 == 0:
        high -= 1
    return int((high-low+2)/2)
