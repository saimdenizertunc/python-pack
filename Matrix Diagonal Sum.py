# Given a square matrix mat, return the sum of the matrix diagonals.

def diagonalSum(mat):
    n = len(mat)
    revers = [i[::-1] for i in mat]
    res = 0
    middle = (n+1)//2
    while(n >= 1):
        res += int(mat[n-1][n-1])
        res += int(revers[n-1][n-1])
        n -= 1
    if(len(mat) % 2 != 0):
        f = mat[middle-1][middle-1]
        res -= f

    return res
