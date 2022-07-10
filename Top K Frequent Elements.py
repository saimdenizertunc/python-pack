from collections import Counter


def topKFrequent(nums, k):
    freq_table = Counter(nums)
    ans_table = freq_table.most_common()
    ans = []
    for key, _ in ans_table:
        if k <= 0:
            break
        k -= 1
        ans.append(key)
    return ans
