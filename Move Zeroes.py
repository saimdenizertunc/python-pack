# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


def moveZeroes(nums):
    a = nums
    for i in a:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums
