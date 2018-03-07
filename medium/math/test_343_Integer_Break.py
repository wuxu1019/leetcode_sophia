import unittest


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        lastmax = 0
        for m in range(2, n + 1):
            res, rem = divmod(n, m)
            multiply = 1
            for j in range(m):
                if j < rem:
                    multiply = multiply * (res + 1)
                else:
                    multiply = multiply * res
            if multiply >= lastmax:
                lastmax = multiply
            else:
                return lastmax
        return lastmax

    def integerBreak2(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n = n - 3
        product *= n
        return product


class TestIntegerBreak(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testCase1(self):
        self.assertEqual(self.s.integerBreak(10), 36)

    def testCase2(self):
        self.assertEqual(self.s.integerBreak(2), 1)

    def testCase3(self):
        self.assertEqual(self.s.integerBreak(40), 2125764)

    def testCase4(self):
        self.assertEqual(self.s.integerBreak2(10), 36)

    def testCase5(self):
        self.assertEqual(self.s.integerBreak2(2), 1)

    def testCase6(self):
        self.assertEqual(self.s.integerBreak2(40), 2125764)



if __name__ == '__main__':
    unittest.main()
