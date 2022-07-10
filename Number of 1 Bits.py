#  Function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n):
    return bin(n).count('1')
