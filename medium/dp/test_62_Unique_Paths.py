"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
import math
class Solution(object):
    def uniquePaths_dp1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def helper(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == m and b == n:
                return 1
            ct = 0
            if a < m:
                ct += helper(a+1, b)
            if b < n:
                ct += helper(a, b+1)
            memo[(a, b)] = ct
            return ct
        return helper(1, 1)

    def uniquePaths_dp2(self, m, n):
        dp = [1] * n
        for i in range(m - 1):
            newdp = [1] * n
            for j in range(n - 2, -1, -1):
                newdp[j] = newdp[j + 1] + dp[j]
            dp = newdp[:]
        return dp[0]

    def uniquePaths_math(self, m, n):
        return math.factorial((m-1)+(n-1))/math.factorial(m-1)/math.factorial(n-1)

if __name__ == '__main__':
    s = Solution()
    rt1 = s.uniquePaths_dp1(9, 4)
    rt2 = s.uniquePaths_dp2(9, 4)
    rt3 = s.uniquePaths_math(9, 4)
    print rt1
    print rt2
    print rt3