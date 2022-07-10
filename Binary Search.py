# Given an array of integers nums which is sorted in ascending order, and an integer target
# Function to search target in nums. If target exists, then return its index. Otherwise, return -1.

def search(nums, target):
    if (nums[0] > target or nums[-1] < target):
        return -1
    for i in range(len(nums)-1):
        if(nums[i] < target and nums[i+1] > target):
            return -1
        if(nums[i] == target):
            return i
    return nums.index(target)
