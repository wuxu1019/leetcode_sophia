# merge sort
# time complexity is O(nlogn)
# space complexity is n

import sys
import multiprocessing
from heapq import merge

def merge_sort(nums):
    lth = len(nums)
    if lth <= 1:
        return nums
    left = merge_sort(nums[:lth/2])
    right = merge_sort(nums[lth/2:])
    return list(merge(left, right))
    
    
def main():
    nums = [5, 9, 4, 6, 3, 2, 7, 1]
    print nums
    nums = merge_sort(nums)
    print nums

if __name__ == '__main__':
    main()

