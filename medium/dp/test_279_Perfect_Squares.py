"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Seen this question in a real interview before?

"""


class Solution(object):
    def numSquares_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [i * i for i in range(1, n + 1) if i * i <= n]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            m = float('INF')
            for j in l:
                if j <= i:
                    m = min(dp[i - j] + 1, m)
            dp[i] = m
        return dp[-1]

    def numSquares_bfs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [i * i for i in range(1, n + 1) if i * i <= n]
        queue = set([n])
        level = 0
        while 1:
            level += 1
            queue_n = set()
            for q in queue:
                for i in l:
                    if q == i:
                        return level
                    elif q > i:
                        queue_n.add(q - i)
            queue = queue_n

