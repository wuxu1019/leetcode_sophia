"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

"""
import bisect
class Solution(object):
    def findClosestElements_diff(self, arr, k, x):
        sorted_arr = sorted(arr, key = lambda m: abs(m - x))

        return sorted(sorted_arr[:k])


    def findClosestElements_bs(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        p = bisect.bisect_left(arr, x)
        ct = k
        a, b = p-1, p
        while a >= 0 and b < len(arr) and ct > 0:
            if x - arr[a] > arr[b] - x:
                b += 1
                ct -= 1
            else:
                a -= 1
                ct -= 1
        if ct == 0:
            return arr[a+1:b]
        if a < 0:
            return arr[:k]
        if b >= len(arr):
            return arr[-k:]

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 3, 4, 5, 6]
    k = 4
    x = 3
    rt1 = s.findClosestElements_bs(arr, k, x)
    print rt1

    rt2 = s.findClosestElements_diff(arr, k, x)
    print rt2
