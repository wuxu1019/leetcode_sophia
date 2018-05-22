"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""


class Solution(object):
    def getPermutation_1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        ans = []
        factor = [1]
        for i in range(2, n):
            factor.append(factor[-1] * i)
        candi = [i for i in range(1, n + 1)]
        i = n - 2
        while candi:
            index, k = divmod(k, factor[i])
            if factor[i] == 1 or k == 0:
                index -= 1
            ans.append(str(candi[index]))
            candi.remove(candi[index])
            i -= 1

        return ''.join(ans)

    def getPermutation_k_subtract_one_first(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        nums = []
        s = 1
        for i in range(n):
            nums.append(i + 1)
            s *= (i + 1)
        k -= 1
        while nums:
            s = s / n
            j, k = divmod(k, s)
            ans += str(nums.pop(j))
            n -= 1
        return ans

