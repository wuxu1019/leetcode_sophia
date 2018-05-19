"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

"""


class Solution(object):
    def integerReplacement_dfs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = float('INF')
        self.record = {}
        self.dfs(n, 0)
        return self.ans

    def dfs(self, n, times):
        if n == 1:
            self.ans = min(self.ans, times)
            return
        if n in self.record:
            return self.record[n]
        if n % 2 == 0:
            self.dfs(n / 2, times + 1)
        else:
            self.dfs(n + 1, times + 1)
            self.dfs(n - 1, times + 1)

    def integerReplacement_math(self, n):
        """
        :type n: int
        :rtype: int
        """
        ct = 0
        while n != 1:
            ct += 1
            if n % 2 == 0:
                n = n >> 1
            else:
                if n % 4 == 3 and n != 3:
                    n = n + 1
                else:
                    n = n - 1
        return ct

if __name__ == '__main__':
    s = Solution()
    n = 12345
    rt1 = s.integerReplacement_dfs(n)
    rt2 = s.integerReplacement_math(n)
    print(rt1)
    print(rt2)