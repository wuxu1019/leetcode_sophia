"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

"""

class Solution(object):
    """answers PredictTheWinner1 & 2 can refer
    https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
    https://www.youtube.com/watch?v=Tw1k46ywN6E&feature=youtu.be&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&t=3622

    answers PredictTheWinner3 & 4 can refer
    https://leetcode.com/problems/predict-the-winner/solution/
    """
    def PredictTheWinner1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for x in range(len(nums)-1, -1, -1):
            for y in range(x, len(nums)):
                a = dp[x+1][y-1] if x+1 <= y-1 else 0
                b = dp[x+2][y] if y >= x+2 else 0
                c = dp[x][y-2] if y-2 >= x else 0
                dp[x][y] = max(nums[x]+min(a, b), nums[y]+min(a, c))
        return 2*dp[0][-1] >= sum(nums)

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(nums, dp, i, j):
            if j < i :
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            a = nums[i] + min(helper(nums, dp, i+1, j-1), helper(nums, dp, i+2, j))
            b = nums[j] + min(helper(nums, dp, i, j-2), helper(nums, dp, i+1, j-1))
            dp[i][j] = max(a, b)
            return dp[i][j]


        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        mybest = helper(nums, dp, 0, n-1)
        return 2*mybest >= sum(nums)

    def PredictTheWinner3(self, nums):
        def help(nums, s, e, turn):
            if s == e:
                return turn * nums[s]
            a = turn * nums[s] + help(nums, s+1, e, turn*(-1))
            b = turn * nums[e] + help(nums, s, e-1, turn*(-1))
            return turn*max(a*turn, b*turn)
        return help(nums, 0, len(nums)-1, 1)>=0

    def PredictTheWinner4(self, nums):
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for s in range(n, -1, -1):
            for e in range(s+1, n):
                a = nums[s] - dp[s+1][e]
                b = nums[e] - dp[s][e-1]
                dp[s][e] = max(a, b)
        return dp[0][-1] >= 0



if __name__ == '__main__':
    s = Solution()

    # test method1
    result1 = s.PredictTheWinner1([8, 15, 3, 7])
    print result1

    result1 = s.PredictTheWinner1([20, 30, 2, 2, 2, 10])
    print result1

    result1 = s.PredictTheWinner1([2, 2, 2, 2])
    print result1

    result1 = s.PredictTheWinner1([1, 5, 2])
    print result1

    # test method2
    result2 = s.PredictTheWinner2([2, 2, 2, 2])
    print result2

    result2 = s.PredictTheWinner2([1, 5, 2])
    print result2

    # test method3
    result3 = s.PredictTheWinner3([2, 2, 2, 2])
    print result3

    result3 = s.PredictTheWinner3([1, 5, 2])
    print result3

    # test method4
    result4 = s.PredictTheWinner4([2, 2, 2, 2])
    print result4

    result4 = s.PredictTheWinner4([1, 5, 2])
    print result4