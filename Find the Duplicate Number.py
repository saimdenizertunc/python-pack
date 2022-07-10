# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

def findDuplicate(nums):
    return [k for k, v in collections.Counter(nums).items() if v > 1][0]
