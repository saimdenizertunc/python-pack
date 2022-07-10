# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge(nums1, m, nums2, n):
    if m == 0:
        nums1[:] = nums2
    elif n == 0:
        nums1[:] = nums1
    else:
        nums1[:] = nums1[0:m]+nums2[0:n]
    nums1.sort()
