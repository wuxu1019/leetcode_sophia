"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

class Solution(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}
        for i in xrange(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in hs.iteritems():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []
        
        for x in xrange(len(nums), 0, -1):
            if x in frq:
                
                for i in frq[x]:
                    arr.append(i)
      
        return [arr[x] for x in xrange(0, k)]
    
