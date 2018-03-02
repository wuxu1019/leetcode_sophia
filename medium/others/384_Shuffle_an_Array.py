import unittest
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        self.origin = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.list = self.origin[:]
        return self.list

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.list)):
            index = random.randint(i, len(self.list) - 1)
            self.list[i], self.list[index] = self.list[index], self.list[i]
        return self.list

class testShuffle(unittest.TestCase):
    def setUp(self):
        self.s = Solution([1, 2, 3])
        pass

    def tearDown(self):
        pass

    def testPossibilty(self):
        ct = {}
        diff = []
        for i in range(60000):
            l = self.s.shuffle()
            l_str = ''.join(map(str, l))
            ct[l_str] = ct.get(l_str, 0) + 1
        for v in ct.values():
            diff.append(abs(10000 - v)/10000.0)

        self.assertTrue(all([i < 0.1 for i in diff]))


if __name__ == '__main__':
    unittest.main()


