"""
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i.

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.

"""
import itertools

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = set([i for i, j in zip(fronts, backs) if i == j])
        ans = 0

        for i in itertools.chain(fronts, backs):
            if i not in same and (i < ans or ans == 0):
                ans = i
        return ans

if __name__ == '__main__':
    s = Solution()
    fronts = [1, 2, 4, 4, 7]
    backs = [1, 3, 4, 1, 3]
    rt1 = s.flipgame(fronts, backs)
    print rt1