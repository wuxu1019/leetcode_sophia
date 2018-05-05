"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.

"""


class Solution(object):
    def updateMatrix_dp(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        R, C = len(matrix), len(matrix[0]);
        max_dist = R * C;

        for i in range(0, R):
            for j in range(0, C):
                if matrix[i][j] != 0:
                    top = matrix[i - 1][j] if i > 0 else max_dist;
                    left = matrix[i][j - 1] if j > 0 else max_dist;
                    matrix[i][j] = min(top, left) + 1;

        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                if matrix[i][j] != 0:
                    bottom = matrix[i + 1][j] if i + 1 < R else max_dist;
                    right = matrix[i][j + 1] if j + 1 < C else max_dist;
                    matrix[i][j] = min(min(bottom, right) + 1, matrix[i][j]);

        return matrix;