# Given an integer n, returns true if it is a power of two. Otherwise, returns false


def isPowerOfTwo(n):
    if n == 0:
        return False
    return n & (n-1) == 0
