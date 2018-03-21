"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        ugly_num = [1]
        n = n - 1
        p2, p3, p5 = 0, 0, 0
        while n:
            num2, num3, num5 = ugly_num[p2] * 2, ugly_num[p3] * 3, ugly_num[p5] * 5
            umin = min(num2, num3, num5)
            ugly_num.append(umin)
            if umin == num2:
                p2 += 1
            if umin == num3:
                p3 += 1
            if umin == num5:
                p5 += 1
            n -= 1
        return ugly_num[-1]

if __name__ == '__main__':
    s = Solution()
    rt = s.nthUglyNumber(123)
    print rt