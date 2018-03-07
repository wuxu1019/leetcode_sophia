import unittest
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        total, ct = 10, 2
        total_dig, dig = 9, 9
        while ct <= n and ct < 11:
            total_dig = total_dig * dig
            dig -= 1
            total = total + total_dig
            ct += 1
        return total

    def countNumbersWithUniqueDigits2(self, n):
        choice = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        product, ans = 1, 1
        for i in range(n if n <= 10 else 10):
            product *= choice[i]
            ans += product
        return ans


class TestCountNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testCase1(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits(2), 91)

    def testCase2(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits(0), 1)

    def testCase3(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits(5), 32491)

    def testCase4(self):
        for i in range(10, 20):
            self.assertEqual(self.s.countNumbersWithUniqueDigits(i), 8877691)

    def testCase5(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits2(2), 91)

    def testCase6(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits2(0), 1)

    def testCase7(self):
        self.assertEqual(self.s.countNumbersWithUniqueDigits2(5), 32491)

    def testCase8(self):
        for i in range(10, 20):
            self.assertEqual(self.s.countNumbersWithUniqueDigits2(i), 8877691)



if __name__ == '__main__':
    unittest.main()