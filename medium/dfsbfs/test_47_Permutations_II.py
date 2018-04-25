"""

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

class Solution(object):
    def permuteUnique_bfs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ct = collections.Counter(nums)
        queue = collections.deque([([], ct)])
        rt = []
        while queue:
            base, candi = queue.popleft()
            if all(v == 0 for v in candi.values()):
                rt.append(base)
                continue
            for k, v in candi.items():
                if v > 0:
                    candi_n = copy.copy(candi)
                    base_n = copy.copy(base)
                    base_n.append(k)
                    candi_n[k] -= 1
                    queue.append((base_n, candi_n))
        return rt

    def permuteUnique_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ct = collections.Counter(nums)
        rt = []
        self.dfs([], ct, rt)
        return rt

    def dfs(self, base, ct, rt):
        if all(v == 0 for v in ct.values()):
            rt.append(base)

        for k, v in ct.items():
            if v > 0:
                ct[k] -= 1
                self.dfs(base + [k], ct, rt)
                ct[k] += 1

    def permuteUnique_trick(self, nums):
        if not nums:
            return []
        ans = [[]]
        for n in nums:
            ans_n = []
            for l in ans:
                for i in range(len(l)+1):
                    nex = l[:i] + [n] + l[i:]
                    ans_n.append(nex)
                    if n < len(l) and n == l[i]:
                        break
            ans = ans_n
        return ans_n