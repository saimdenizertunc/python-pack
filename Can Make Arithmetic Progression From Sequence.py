# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


def canMakeArithmeticProgression(arr):
    a = sorted(arr)
    r = a[1] - a[0]
    for i in range(1, len(arr)):
        if((a[0] + i*r) != a[i]):
            return False
    return True
