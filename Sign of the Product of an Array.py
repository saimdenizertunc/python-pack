#  Given an integer array nums. Let product be the product of all values in the array nums.

def arraySign(nums):
    if(0 in nums):
        return 0
    a = len(list(filter(lambda x: (x < 0), nums)))
    return ((-1)**a)
