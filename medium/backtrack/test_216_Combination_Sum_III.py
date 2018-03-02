import unittest

class Solution(object):
    def __init__(self):
        pass

    def combinationSum3(self, k, n):
        self.rt = []
        self.combinationHelper(n, k, [], range(1, 10))
        return self.rt

    def combinationHelper(self, left, time, up, list):
        if not left and not time:
            self.rt.append(up)
            return
        if not left or not time:
            return

        for i in range(len(list)):
            d = left - list[i]
            if d >= 0:
                self.combinationHelper(d, time-1, up+[list[i]], list[i+1:])


class TestCombinationSum3(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def testCase1(self):
        self.assertEqual(self.s.combinationSum3(3, 9), [[1,2,6], [1,3,5], [2,3,4]])

    def testCase2(self):
        self.assertEqual(self.s.combinationSum3(3, 7), [[1, 2, 4]])

    def testCase3(self):
        self.assertEqual(self.s.combinationSum3(3, 3), [])

    def tearDown(self):
        self.s = None

if __name__ == '__main__':
    testsuit = unittest.TestLoader().loadTestsFromTestCase(TestCombinationSum3)
    unittest.TextTestRunner(verbosity=2).run(testsuit)

