# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

from collections import Counter


def firstUniqChar(self, s: str) -> int:
    count = collections.Counter(s)
    for i, l in enumerate(s):
        if count[l] == 1:
            return i
    return -1
