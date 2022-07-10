# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.


def sumOddLengthSubarrays(arr):
    result = 0
    for i in range(1, len(arr)+1, 2):
        for j in range(len(arr)):
            if(j+i <= len(arr)):
                result += sum(arr[j:i+j])
    return result
