"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
"""


class Solution(object):
    def minPathSum_recuisive(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        M = len(grid)
        N = len(grid[0])
        memo = {}

        def minPathSumHelper(x, y):
            if x == M - 1 and y == N - 1:
                return grid[x][y]
            if (x, y) in memo:
                return memo[(x, y)]
            p1, p2 = float('INF'), float('INF')
            if x + 1 < M:
                p1 = grid[x][y] + minPathSumHelper(x + 1, y)
            if y + 1 < N:
                p2 = grid[x][y] + minPathSumHelper(x, y + 1)
            m = min(p1, p2)
            memo[(x, y)] = m
            return m

        return minPathSumHelper(0, 0)

    def minPathSum_dp(self, grid):
        if not grid:
            return 0

        dp = [grid[0][0]]
        for v in grid[0][1:]:
            dp.append(dp[-1] + v)

        for i in range(1, len(grid)):
            dp[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,1], [1,5,1], [4,2,1]]

    rt1 = s.minPathSum_dp(grid)
    print rt1