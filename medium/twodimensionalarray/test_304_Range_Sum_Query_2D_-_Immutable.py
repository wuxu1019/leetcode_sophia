"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = None
            return
        R, C = len(matrix), len(matrix[0])
        self.matrix = matrix
        for i in range(R):
            for j in range(C):
                up = 0 if i < 1 else self.matrix[ i -1][j]
                left = 0 if j < 1 else self.matrix[i][ j -1]
                up_left = 0 if i < 1 or j < 1 else self.matrix[ i -1][ j -1]
                self.matrix[i][j] = up + left + self.matrix[i][j] - up_left


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        left = 0 if col1 < 1 else self.matrix[row2][col 1 -1]
        up = 0 if row1 < 1 else self.matrix[row 1 -1][col2]
        up_left = 0 if col1 < 1 or row1 < 1 else self.matrix[row 1 -1][col 1 -1]
        return self.matrix[row2][col2] - left - up + up_left


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = None
            return
        R, C = len(matrix), len(matrix[0])
        self.matrix = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                self.matrix[i][j] = self.matrix[i - 1][j] + self.matrix[i][j - 1] + matrix[i - 1][j - 1] - \
                                    self.matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix[row2 + 1][col2 + 1] - self.matrix[row1][col2 + 1] - self.matrix[row2 + 1][col1] + \
               self.matrix[row1][col1]

