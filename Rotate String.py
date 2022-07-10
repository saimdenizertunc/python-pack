# Given two strings A and B, return true if and only if s can become goal after some number of shifts on A.


def rotateString(A: str, B: str):
    if len(A) != len(B):
        return False
    if len(A) == 0:
        return True

    for s in range(len(A)):
        if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
            return True
    return False
