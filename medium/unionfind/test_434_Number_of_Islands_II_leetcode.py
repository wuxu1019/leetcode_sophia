"""
Description
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Have you met this question in a real interview?
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
"""

#Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b



class UnionFind:

    def __init__(self, grid, R, C):
        self.father = [-1] * (R * C)
        self.count = 0

    def add_group(self, k):
        self.father[k] = k
        self.count += 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def find(self, root):
        if self.father[root] == root:
            return root
        return self.find(self.father[root])


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        grid = [[0] * m for _ in range(n)]
        uf = UnionFind(grid, n, m)
        rt = []
        mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for p in operators:
            x, y = p.x, p.y
            if 0 <= x < n and 0 <= y < m and grid[x][y] != 1:
                grid[x][y] = 1
                k = m * x + y

                uf.add_group(k)
                for dx, dy in mv:
                    n_x, n_y = x + dx, y + dy
                    if 0 <= n_x < n and 0 <= n_y < m and grid[n_x][n_y] == 1:
                        uf.union(k, m * n_x + n_y)
            rt.append(uf.count)
        return rt


if __name__ == '__main__':
    s = Solution()
    n = 4
    m = 5
    operations = [Point(1, 1), Point(0, 1), Point(3, 3), Point(3, 4)]
    rt = s.numIslands2(n, m, operations)
    print rt