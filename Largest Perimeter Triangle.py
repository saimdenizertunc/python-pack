# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0

def largestPerimeter(nums):
    nums.sort(reverse=True)
    triangle = 0
    for i in range(0, len(nums)-2):
        if(nums[i] < nums[i+2] + nums[i+1]):
            triangle = max(triangle, nums[i] + nums[i+2] + nums[i+1])
            break
    return triangle
