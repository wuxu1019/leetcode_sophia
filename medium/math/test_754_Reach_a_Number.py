"""

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


class Solution(object):
    def reachNumber_bfs(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        pos, new_pos = set([0]), set()
        step = 1
        while True:
            for i in pos:
                new_pos.add(i + step)
                new_pos.add(i - step)
                if target in new_pos:
                    return step
            pos, new_pos = new_pos, set()
            step += 1

    def reachNumber_math(self, target):

        step = 0
        target = abs(target)
        while target > 0:
            step += 1
            target -= step

        if target % 2 == 0:
            return step
        elif step % 2 == 0:
            return step + 1
        else:
            return step + 2

