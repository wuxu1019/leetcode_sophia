"""
give a array, and a target number, check how many pair numbers can sum to target number
1. brute force sum O(n2)
2. use two sum method O(n), O(n)
"""
import collections

def two_sum(nums, target):
    ct = 0
    mp = collections.Counter(nums)
    print mp
    for num in mp.keys():
        comp = target - num
        if comp in mp:
           if comp != num:
               m = min(mp[num], mp[comp])
               ct += m**2
           else:
               ct += mp[num]*(mp[num]-1)
    return ct 

data = [1, -4, 3, 9, 0, 12, 1, 2, 3, -3, -2, -1, 1, 2, -1, -3]
target = 0
ct = two_sum(data, target)
print ct
