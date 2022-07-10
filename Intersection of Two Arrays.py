from collections import Counter


def intersect(nums1, nums2):
    return (Counter(nums1) & Counter(nums2)).elements()
