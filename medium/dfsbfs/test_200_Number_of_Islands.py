"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ct = 0
        lr, lc = len(grid), len(grid[0])
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == "1":
                    ct += 1
                    self.makeNeigbours(grid, i, j, lr, lc)
        return ct

    def makeNeigbours(self, grid, i, j, lr, lc):
        l = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        grid[i][j] = "0"
        for a, b in l:
            if a >= 0 and a < lr and b >= 0 and b < lc and grid[a][b] != "0":
                self.makeNeigbours(grid, a, b, lr, lc)
        return

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    rt1 = s.numIslands(grid)
    print rt1