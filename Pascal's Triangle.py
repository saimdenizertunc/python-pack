# Given an integer numRows, return the first numRows of Pascal's triangle.


def generate(numRows):
    s = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for k in range(1, i):
            s[i][k] = s[i-1][k-1]+s[i-1][k]
    return s
