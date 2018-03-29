"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.matrix = [[0] * n for _ in range(n)]
        self.generateMatrixHelper(0, n - 1, 1)
        return self.matrix

    def generateMatrixHelper(self, s, e, ct):
        if e < s:
            return
        if e == s:
            self.matrix[s][e] = ct
            return
        for j in range(s, e):
            self.matrix[s][j] = ct
            ct += 1

        for i in range(s, e):
            self.matrix[i][e] = ct
            ct += 1

        for j in range(e, s, -1):
            self.matrix[e][j] = ct
            ct += 1

        for i in range(e, s, -1):
            self.matrix[i][s] = ct
            ct += 1

        self.generateMatrixHelper(s + 1, e - 1, ct)

    def generateMatrix_way2(self, n):
        matrix = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for num in range(1, n*n+1):
            matrix[i][j] = num
            if matrix[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di
            i = i + di
            j = j + dj
        return matrix



if __name__ == '__main__':
    s = Solution()
    rt1 = s.generateMatrix(4)
    print rt1

    rt2 = s.generateMatrix_way2(4)
    print rt2