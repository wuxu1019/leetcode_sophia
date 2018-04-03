"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix_bs(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row0 = matrix[0]
        row1 = matrix[-1]
        p1 = bisect.bisect(row0, target) - 1
        p2 = bisect.bisect(row1, target) - 1
        candi = set(range(p1+1)) and set(range(p2, len(matrix[0])))
        for c in candi:
            col = [matrix[i][c] for i in range(len(matrix))]
            if col[bisect.bisect(col, target)-1] == target:
                return True
        return False

    def searchMatrix_fast(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        i, j = 0, len(matrix[0]) - 1
        while 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
            if j < 0 or i >= len(matrix):
                break
        return False


