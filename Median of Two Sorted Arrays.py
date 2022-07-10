# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

def findMedianSortedArrays(nums1, nums2):
    n = len(nums1 + nums2)
    s = sorted(nums1 + nums2)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
