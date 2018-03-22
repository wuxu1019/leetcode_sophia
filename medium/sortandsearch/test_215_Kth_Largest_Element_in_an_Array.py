"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement_needmemory(self, k, A):
        pilot = A[0]
        smaller, bigger = [], []
        for a in A[1:]:
            if a < pilot:
                smaller.append(a)
            else:
                bigger.append(a)
        if k == len(bigger) + 1:
            return pilot
        elif k < len(bigger) + 1:
            return self.kthLargestElement_needmemory(k, bigger)
        else:
            return self.kthLargestElement_needmemory(k - len(bigger) - 1, smaller)

    def kthLargestElement_bs(self, k, A):
        def helper(s, e):
            pilot = A[s]
            p, q = s + 1, e
            while p <= q:
                if A[p] > pilot:
                    p += 1
                else:
                    A[p], A[q] = A[q], A[p]
                    q -= 1
            A[s], A[q] = A[q], A[s]

            if q == k:
                return pilot
            elif q > k:
                return helper(s, q-1)
            else:
                return helper(q+1, e)
        k -= 1
        return helper(0, len(A)-1)





if __name__ == '__main__':

    s = Solution()
    k = 10
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rt1 = s.kthLargestElement_bs(k, A)
    print rt1

    A = [2, 3, 5, 7, 3, 2, 8, 3, 9]
    k = 4
    rt2 = s.kthLargestElement_bs(k, A)
    print rt2

    rt3 = s.kthLargestElement_needmemory(k, A)
    print rt3