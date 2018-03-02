import unittest

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rt = []
        if not matrix:
            return rt
        M, N = len(matrix), len(matrix[0])
        i, j, ct = 0, 0, 0
        while j < N:
            a, b, line = i, j, []
            while 1:
                line.append(matrix[a][b])
                a -= 1
                b += 1
                if a < 0 or b == N:
                    break
            if not ct & 1:
                rt = rt + line[:]
            else:
                rt = rt + line[::-1]
            ct += 1
            if i == M-1:
                j += 1
            else:
                i += 1
        return rt

class TestDiagonalTraverse(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(self.s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1,2,4,7,5,3,6,8,9])

    def testCase2(self):
        self.assertEqual(self.s.findDiagonalOrder([[1, 2, 3], [4, 5, 6]]), [1,2,4,5,3,6])

    def testCase3(self):
        self.assertEqual(self.s.findDiagonalOrder([]), [])

if __name__ == '__main__':
    unittest.main(verbosity=1)