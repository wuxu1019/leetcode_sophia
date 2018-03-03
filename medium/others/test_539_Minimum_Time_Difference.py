import unittest


class Solution(object):
    def findMinDifference(self, timePoints):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        timePoints = map(convert, timePoints)
        timePoints.sort()

        return min([(y-x)%(24*60) for x, y in zip(timePoints, timePoints[1:]+timePoints[:1])])



class TestFindMinDiff(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def testCase1(self):
        self.assertEqual(self.s.findMinDifference(["23:59","00:00"]), 1)

    def testCase2(self):
        self.assertEqual(self.s.findMinDifference(["23:59", "00:00", "00:00"]), 0)

    def testCase3(self):
        self.assertEqual(self.s.findMinDifference(["12:30", "18:20", "23:59", "22:00", "10:00"]), 119)
