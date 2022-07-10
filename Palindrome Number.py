# Given an integer x, returns true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.


def isPalindrome(x):
    if x < 0:
        return False
    rev = str(x)[::-1]
    if(int(rev) == x):
        return True
    else:
        return False
