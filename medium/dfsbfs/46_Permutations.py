import unittest

class Solution(object):
    def __init__(self):
        pass

    def permute(self, nums):
        self.rt = []
        self.helper(nums, [])
        return self.rt

    def helper(self, leftnums, up):
        if not len(leftnums):
            self.rt.append(up)
        for i in leftnums:
            d = leftnums[:]
            d.remove(i)
            self.helper(d, up + [i])

class permulationTests(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
        pass

    def tearDown(self):
        pass

    def testcase1(self):
        result = self.s.permute([1, 2, 3])
        expect = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]
        self.assertTrue(self.ignoreOrder(result, expect))

    def testcase2(self):
        result = self.s.permute([])
        expect = [[]]
        self.assertTrue(self.ignoreOrder(result, expect))

    def ignoreOrder(self, A, B):
        A.sort()
        B.sort()
        if A == B:
            return True
        else:
            return False

if __name__=='__main__':
    unittest.main()


