import unittest


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        rt = []
        for i in range(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for m in res1:
                    for n in res2:
                        rt.append(self.count(int(m), int(n), input[i]))
        return rt

    def count(self, x, y, opt):
        if opt == '+':
            return x+y
        elif opt == '-':
            return x-y
        elif opt == '*':
            return x*y




class TestWayParentheses(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testcase1(self):
        self.assertEqual(sorted(self.s.diffWaysToCompute('2*3-4*5')), sorted([-34, -14, -10, -10, 10]))

    def testcase2(self):
        self.assertEqual(sorted(self.s.diffWaysToCompute('2-1-1')), sorted([0, 2]))
