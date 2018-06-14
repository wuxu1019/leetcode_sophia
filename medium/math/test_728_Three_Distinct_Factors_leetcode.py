"""
Given a positive integer n (1 <= n <= 10^18). Check whether a number has exactly three distinct factors, return true if it has exactly three distinct factors, otherwise false.

Have you met this question in a real interview?
Example
Given n = 9, return true
Number 9 has exactly three factors: 1, 3, 9, so return true.

Given n = 10, return false
"""


class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """

    def isThreeDisctFactors(self, n):
        # write your code here
        root = int(math.sqrt(n))
        if not root * root == n:
            return False

        if not self.isPrimeNumber(root):
            return False

        return True

    def isPrimeNumber(self, n):
        if n == 0 or n == 1:
            return False
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True