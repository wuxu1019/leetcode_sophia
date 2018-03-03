import unittest

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        ct = {}
        for i in range(len(wall)):
            sect = 0
            for j in range(0, len(wall[i]) - 1):
                sect += wall[i][j]
                ct[sect] = ct.get(sect, 0) + 1

        return len(wall) - max(ct.values()) if ct else len(wall)


class TestBrickWall(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testcase1(self):
        self.assertEqual(self.s.leastBricks([[1],[1]]), 2)

    def testcase2(self):
        self.assertEqual(self.s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]), 2)

if __name__ == '__main__':
    unittest.main()

