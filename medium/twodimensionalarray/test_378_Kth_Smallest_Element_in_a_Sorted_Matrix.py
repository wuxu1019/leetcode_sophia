"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9, 10],
   [10, 11, 13, 13],
   [12, 13, 15, 16],
   [13, 15, 17, 19],
],
k = 8,

return 13.

"""
import bisect
import itertools


class Solution(object):
    def kthSmallest_bs(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo

    def kthSmallest_sort(self, matrix, k):
        return sorted(itertools.chain(*matrix))[k-1]

if __name__ == '__main__':
    s = Solution()
    matirx = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
    k = 5
    rt1 = s.kthSmallest_bs(matirx, k)
    print rt1

    rt2 = s.kthSmallest_sort(matirx, k)
    print rt2

