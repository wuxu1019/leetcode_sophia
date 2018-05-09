"""
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i].

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""

class Solution(object):
    def maxProfitAssignment_1(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        diff_pro = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        diff_pro.sort(key=lambda k:k[0])
        max_p = 0
        for i, v in enumerate(diff_pro):
            max_p = max(max_p, v[1])
            diff_pro[i][1] = max_p
        ans = 0
        difficulty = [k[0] for k in diff_pro]
        for w in worker:
            i = bisect.bisect(difficulty, w) - 1
            if i >= 0:
                ans += diff_pro[i][1]
        return ans

    def maxProfitAssignment_two_pointer(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        max_till_now = 0
        i, ans = 0, 0
        for w in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= w:
                max_till_now = max(max_till_now, jobs[i][1])
                i += 1
            ans += max_till_now
        return ans