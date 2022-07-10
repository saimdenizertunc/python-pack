"""

A happy number is a number defined by the following process:

    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.

Returns true if n is a happy number, and false if not.

"""


def isHappy(n):
    res = []

    def getSquare(m):
        x = sum([int(i)**2 for i in str(m)])
        return x

    while(True):
        a = getSquare(n)
        if(a == 1):
            return True
        elif(a not in res):
            res.append(a)
            n = a
        else:
            return False
