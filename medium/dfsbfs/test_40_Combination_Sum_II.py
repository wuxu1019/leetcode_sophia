"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""

import collections
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ct = collections.Counter(candidates)
        l = [[k, v] for k, v in ct.items()]
        l.sort(key=lambda k: k[0])
        result = []
        self.dfs(l, 0, [], target, result)
        return result

    def dfs(self, l, p, base, target, result):
        if target == 0:
            result.append(base)
        if p >= len(l):
            return
        for i in range(p, len(l)):
            k, v = l[i]
            if k <= target:
                l[i][1] -= 1
                if l[i][1] == 0:
                    self.dfs(l, i + 1, base + [k], target - k, result)
                else:
                    self.dfs(l, i, base + [k], target - k, result)
                l[i][1] += 1
            else:
                break

if __name__ == '__main__':
    s = Solution()
    cands = [10,1,2,7,6,1,5]
    target = 8
    rt = s.combinationSum2(cands, target)
    print rt