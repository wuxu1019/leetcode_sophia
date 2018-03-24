"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def numTreesHelper(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            ct = 0
            for i in range(0, n):
                ct += numTreesHelper(i) * numTreesHelper(n - 1 - i)
            memo[n] = ct
            return ct

        return numTreesHelper(n)

    def numTrees1(self, n):
        res = [0] * (n + 1)
        res[0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]