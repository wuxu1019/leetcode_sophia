"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class UnionFind(object):
    def __init__(self, grid, r, c):
        self.father = [-1] * (r * c)
        self.count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    p = i * c + j
                    self.father[p] = p
                    self.count += 1

    def union(self, a, b):
        a_f = self.find(a)
        b_f = self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            self.count -= 1

    def find(self, p):
        if self.father[p] == p:
            return p
        return self.find(self.father[p])


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        uf = UnionFind(grid, R, C)

        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    for di, dj in move:
                        n_i = i + di
                        n_j = j + dj
                        if 0 <= n_i < R and 0 <= n_j < C and grid[n_i][n_j] == '1':
                            uf.union(i * C + j, n_i * C + n_j)

        return uf.count

