"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(t, cands):
            rt = []
            for i, c in enumerate(cands):
                if c < t:
                    cmb = helper(t - c, cands[i:])
                    for i in cmb:
                        rt.append(i + [c])
                elif c == t:
                    rt.append([c])
            return rt

        return helper(target, sorted(candidates, reverse=1))

if __name__ == '__main__':
    s = Solution()
    cand = [2, 3, 4, 7]
    target = 7
    rt1 = s.combinationSum(cand, target)
    print rt1