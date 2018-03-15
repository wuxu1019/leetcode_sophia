"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s = [0]
        exp = 0
        while exp < n:
            s_1= [i^(1<<exp) for i in s[::-1]]
            exp += 1
            s.extend(s_1)
        return s

if __name__ == '__main__':
    s = Solution()
    rt = s.grayCode(4)
    print rt