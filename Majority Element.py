# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

import collections


def majorityElement(nums):
    h = []
    n = len(nums)
    a = collections.Counter(nums)
    b = dict(a)
    for k, v in b.items():
        if v > (n//3):
            h.append(k)
    return h
