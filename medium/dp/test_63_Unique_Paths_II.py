"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles_updown(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[-1][-1]:
            return 0

        R, C = len(obstacleGrid), len(obstacleGrid[0])
        self.memo = [[-1] * C for _ in range(R)]
        self.memo[-1][-1] = 1
        self.dfs(obstacleGrid, 0, 0, R, C)
        return self.memo[0][0] if self.memo[0][0] >= 0 else 0

    def dfs(self, obstacleGrid, i, j, R, C):
        if i < 0 or i >= R or j < 0 or j >= C:
            return 0
        if obstacleGrid[i][j]:
            return 0
        if self.memo[i][j] >= 0:
            return self.memo[i][j]
        self.memo[i][j] = self.dfs(obstacleGrid, i + 1, j, R, C) + self.dfs(obstacleGrid, i, j + 1, R, C)
        return self.memo[i][j]

    def uniquePathsWithObstacles_dp(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[-1][-1]:
            return 0

        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * C for _ in range(R)]
        dp[-1][-1] = 1
        for i in xrange(R - 1, -1, -1):
            for j in xrange(C - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    if i + 1 < R:
                        dp[i][j] += dp[i + 1][j]
                    if j + 1 < C:
                        dp[i][j] += dp[i][j + 1]
        return dp[0][0]



